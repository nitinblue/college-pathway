import streamlit as st
from sqlalchemy.orm import Session
import io
import tempfile
import os

from neuroconnections.app.db.session import SessionLocal
from neuroconnections.app.db.models import Journey, ExplorationStep, ActionItem
from neuroconnections.app.services.recommendation_service import recommend
from neuroconnections.app.services.journey_service import add_exploration_step, get_stream_details, add_stream_exploration
from neuroconnections.app.services.stream_service import STREAMS, get_all_streams  # Import the STREAMS constant for stream details
from neuroconnections.app.services.career_service import get_spark, CAREER_SPARKS  # New import for Career Sparks
import networkx as nx
import matplotlib.pyplot as plt

# Voice Reflections: Requires pip install openai-whisper
try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False
    st.error("For voice reflections, install: pip install openai-whisper")

st.set_page_config(page_title="NeuroConnections", layout="wide")
st.title("🧠 NeuroConnections")
st.caption("A guided exploration space — no pressure, no premature decisions")

db: Session = SessionLocal()

# -----------------------------
# Sidebar – Journey Selection & Progress
# -----------------------------
st.sidebar.header("Journey")

journeys = db.query(Journey).all()
journey_map = {f"{j.student_name} ({j.university})": j.id for j in journeys}

selected_journey_label = st.sidebar.selectbox(
    "Select existing journey",
    options=["Create New"] + list(journey_map.keys())
)

journey = None  # Default to None

if selected_journey_label == "Create New":
    st.sidebar.subheader("Create New Journey")
    student_name = st.sidebar.text_input("Student name")
    #university = st.sidebar.selectbox("University", ["UIC", "PITT", "BOWDOIN"])  # Added BOWDOIN
    university = st.sidebar.selectbox(
        "University (or intended)", 
        ["UIC", "PITT", "BOWDOIN", "Rutgers New Brunswick", "DePaul", "WashU", "Rutgers Camden"]
    )
    if st.sidebar.button("Create Journey"):
        from neuroconnections.app.services.journey_service import create_journey  # Use service for consistency
        journey = create_journey(db, student_name, university)
        st.sidebar.success("Journey created! Refreshing...")
        st.rerun()
else:
    journey_id = journey_map[selected_journey_label]
    journey = db.query(Journey).get(journey_id)

# Progress Pulse (if journey exists)
if journey:
    steps = db.query(ExplorationStep).filter_by(journey_id=journey.id).all()
    total_actions = sum(len(step.actions) for step in steps)
    # Fixed: Handle potential None in completed (treat as False/0)
    completed_actions = sum(1 if action.completed else 0 for step in steps for action in step.actions)
    progress = (completed_actions / max(total_actions, 1)) * 100
    st.sidebar.metric("Exploration Progress", f"{progress:.0f}%", delta=None)
    st.sidebar.progress(progress / 100)

if journey is None:
    st.warning("Please select or create a journey.")
    st.stop()

# New tab order — Discover Streams first
tab, tab1, tab2, tab3 = st.tabs(["🧭 Discover Streams", "🛤️ My Path", "📚 Course Bundles", "🔥 Career Sparks"])

# Now check and render
if journey is None:
    st.warning("Please select or create a journey to continue.")
    st.stop()

# Tabs for cohesion
# tab1, tab2, tab3 = st.tabs(["My Path", "Add Spark", "Career Sparks"])

with tab:
    st.subheader("What can you do with a Neuroscience major?")
    st.caption("Explore different streams. Click to learn real professions and what life after graduation looks like.")

    streams = get_all_streams()
    cols = st.columns(3)

    for i, (name, data) in enumerate(streams.items()):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"### {data['icon']} {name}")
                st.write(data['description'][:120] + "...")
                if st.button("Explore this stream →", key=f"btn_{name}"):
                    add_stream_exploration(db, journey.id, name)
                    st.success(f"Added **{name}** to My Path!")
                    st.rerun()

    # Deep dive
    st.markdown("---")
    selected_stream = st.selectbox("Deep dive into one stream", options=list(streams.keys()))
    if selected_stream:
        data = get_stream_details(selected_stream, journey.university)
        st.markdown(f"## {data['icon']} {selected_stream}")
        st.write(data["description"])

        st.markdown("### What to Expect After Graduation")
        st.info(data["post_grad"])

        st.markdown("### Real Professions & A Day in the Life")
        for prof in data["professions"]:
            with st.expander(prof["title"]):
                st.write(prof.get("vignette", "Vignette coming soon..."))
                if "salary" in prof:
                    st.caption(f"Starting salary range: {prof['salary']}")

        st.markdown("### Ways to Explore This at " + journey.university)
        for action in data["recommended_actions"]:
            if st.checkbox(action, key=f"chk_{selected_stream}_{action[:30]}"):
                # Optional: auto-add as action item
                pass

        if st.button("Add these exploration ideas to My Path"):
            add_stream_exploration(db, journey.id, selected_stream)
            st.success("Added to your journey!")
            
with tab1:
    # -----------------------------
    # Journey Overview
    # -----------------------------
    st.subheader(f"Journey: {journey.student_name} – {journey.university}")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Add Exploration Step")

        theme = st.selectbox(
            "Exploration Theme",
            ["Curiosity", "Skill", "Ethics", "Low Load"]
        )

        # Voice Reflections Feature
        st.markdown("#### 🎙️ Voice Reflection (Optional)")
        audio_input = st.audio_input("Record your thoughts aloud (tap to start recording)")
        transcribed_text = ""
        if audio_input and WHISPER_AVAILABLE:
            # Transcribe audio
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                tmp_file.write(audio_input.getvalue())
                tmp_file_path = tmp_file.name
            
            try:
                model = whisper.load_model("base")  # Use 'tiny' for faster, 'base' for better accuracy
                result = model.transcribe(tmp_file_path)
                transcribed_text = result["text"]
                st.success("Transcription ready! (Review & edit below.)")
            except Exception as e:
                st.error(f"Transcription error: {e}")
            finally:
                os.unlink(tmp_file_path)  # Clean up temp file

        reflection = st.text_area(
            "Reflection (text or transcribed from voice)",
            value=transcribed_text,  # Pre-fill with transcription if available
            height=150,
            placeholder="What felt interesting? Confusing? Energizing?"
        )
        
        use_bundles = st.checkbox("Suggest full course combinations? (for career paths)")
        
        if st.button("Add Step"):
            mode = "combinations" if use_bundles else "single"
            add_exploration_step(db, journey.id, theme, reflection, mode=mode)  # Full service call
            st.success("Step added with recommendations!")
            st.rerun()

    with col2:
        st.markdown("### Why This Matters")
        st.info(
            "- No decisions required\n"
            "- Reflection builds clarity\n"
            "- Actions stay small & reversible\n"
            "- History reduces anxiety"
        )

        st.markdown("### 🌿 Quick Path Preview")
        if st.button("Generate Neuroscience + Complements"):
            bundles = recommend(theme, journey.university, mode="combinations")
            for bundle in bundles[:2]:  # Show top 2 to keep light
                with st.expander(f"{bundle['name']} – {bundle['rationale'][:50]}..."):
                    st.write("**Courses:**")
                    for course in bundle['courses']:
                        st.write(f"- {course}")
                    st.info(f"**Sparks:** {bundle['careers']}")

    # -----------------------------
    # History Timeline
    # -----------------------------
    st.markdown("---")
    st.markdown("## 🕰️ Exploration History")

    steps = (
        db.query(ExplorationStep)
        .filter_by(journey_id=journey.id)
        .order_by(ExplorationStep.id.desc())
        .all()
    )

    if not steps:
        st.write("No exploration steps yet. Add one above!")
    else:
        for step in steps:
            with st.expander(f"{step.theme} – Step #{step.id}", expanded=False):
                st.markdown("**Reflection**")
                st.write(step.reflection)

                st.markdown("**Action Items**")
                actions_by_bundle = {}
                for action in step.actions:
                    bundle_key = action.parent_bundle if action.parent_bundle else "General"
                    if bundle_key not in actions_by_bundle:
                        actions_by_bundle[bundle_key] = []
                    actions_by_bundle[bundle_key].append(action)

                for bundle_key, actions in actions_by_bundle.items():
                    if bundle_key != "General":
                        st.markdown(f"### {bundle_key} Bundle")
                    for action in actions:
                        # Fixed: Handle None in value by defaulting to False
                        action_value = action.completed if action.completed is not None else False
                        checked = st.checkbox(
                            action.description,
                            value=action_value,
                            key=f"action_{action.id}"
                        )
                        if checked != action_value:
                            action.completed = checked
                            db.commit()

    # Mind Map Button
# Mind Map Button - Improved version
if st.button("🌟 Show Mind Map"):
    G = nx.Graph()
    
    # More meaningful nodes based on the streams we have in the app
    G.add_edges_from([
        ("Neuroscience Major", "Academic Research"),
        ("Neuroscience Major", "Clinical & Healthcare"),
        ("Neuroscience Major", "Neurotechnology & BCI"),
        ("Neuroscience Major", "Biotech & Pharma"),
        ("Neuroscience Major", "Computational & Data Science"),
        ("Neuroscience Major", "Policy, Ethics & Communication"),
        
        ("Academic Research", "Lab Technician / Research Assistant"),
        ("Academic Research", "PhD → Professor"),
        
        ("Clinical & Healthcare", "Clinical Research Coordinator"),
        ("Clinical & Healthcare", "Therapist / Clinician"),
        
        ("Neurotechnology & BCI", "Neurotech Specialist"),
        ("Neurotechnology & BCI", "BCI Engineer"),
        
        ("Biotech & Pharma", "Research Associate"),
        ("Biotech & Pharma", "Regulatory Affairs"),
        
        ("Computational & Data Science", "Neuroscience Data Analyst"),
        
        ("Policy, Ethics & Communication", "Science Policy Advisor"),
        ("Policy, Ethics & Communication", "Science Writer"),
    ])
    
    # Better layout and styling
    pos = nx.spring_layout(G, seed=42)  # Consistent layout
    fig, ax = plt.subplots(figsize=(11, 7))  # Much bigger and better proportions
    
    nx.draw(
        G, 
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=2800,
        font_size=9,
        font_weight="bold",
        edge_color="gray",
        width=1.5,
        alpha=0.9,
        ax=ax
    )
    
    # Optional: highlight the central node
    nx.draw_networkx_nodes(G, pos, nodelist=["Neuroscience Major"], 
                           node_color="lightcoral", node_size=3200, ax=ax)
    
    plt.title("Your Neuroscience Exploration Map", fontsize=14, pad=20)
    plt.tight_layout()
    st.pyplot(fig)
    
    st.caption("🧭 This is a high-level view of possible paths. "
               "Your added steps and sparks will appear in 'My Path' history. "
               "Paths branch — explore what feels interesting!")
with tab2:
    # -----------------------------
    # Focused Bundle Generator (Add Spark Tab)
    # -----------------------------
    st.markdown("### 🔍 Deeper Dive: Course Bundles for Careers")
    st.caption("Generate full combos tailored to your school—pick a theme to start.")

    theme_for_bundles = st.selectbox("Theme for Bundles", ["Curiosity", "Skill", "Ethics", "Low Load"])
    if st.button("Generate Bundles"):
        bundles = recommend(theme_for_bundles, journey.university, mode="combinations")
        for bundle in bundles:
            with st.expander(f"{bundle['name']}"):
                st.write(f"**Rationale:** {bundle['rationale']}")
                st.write("**Courses:**")
                for course in bundle['courses']:
                    st.write(f"- {course}")
                st.info(f"**Post-Grad:** {bundle['careers']}")
                
                if st.checkbox(f"Add {bundle['name']} to My Actions?"):
                    # Quick add as ActionItem
                    db.add(ActionItem(
                        description=f"Bundle: {bundle['name']} – {bundle['rationale']}",
                        completed=False,
                        step_id=None,  # Standalone
                        is_bundle=True,
                        parent_bundle=bundle['name']
                    ))
                    for course in bundle['courses']:
                        db.add(ActionItem(
                            description=f"• {course}",
                            completed=False,
                            step_id=None,
                            parent_bundle=bundle['name']
                        ))
                    db.commit()
                    st.success(f"{bundle['name']} added to your history!")

with tab3:
    # -----------------------------
    # Career Sparks
    # -----------------------------
    st.markdown("### 👥 Career Sparks: A Day in the Life + College Prep")
    st.caption("Peek into real roles post-undergrad—no MS needed. Claim sparks to your Journey.")

    roles = list(CAREER_SPARKS.keys()) # ["Researcher", "Consultant", "Clinician"]

    selected_role = st.selectbox("Choose a Role:", roles)
    
    spark_data = get_spark(selected_role, journey.university)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"**A Day as a {selected_role}**")
        st.write(spark_data["vignette"])
    
    with col_b:
        st.markdown("**Prep in College (Your School)**")
        for tip in spark_data["prep"]:
            st.checkbox(tip, key=f"prep_{selected_role}_{hash(tip)}")
        
        if st.button(f"Claim '{selected_role}' Spark"):
            # Add to DB as special ActionItem (link to a "Career" step if exists, or standalone)
            latest_step = steps[-1] if steps else None
            step_id = latest_step.id if latest_step else None
            db.add(ActionItem(
                description=f"{selected_role} Spark: {spark_data['vignette'][:100]}... | Prep: {', '.join(spark_data['prep'])}",
                completed=False,
                step_id=step_id,
                is_bundle=False,
                parent_bundle=f"Career: {selected_role}"
            ))
            db.commit()
            st.success(f"Spark added! Check 'My Path' history.")
            st.rerun()

    st.markdown("---")
    st.info("Tip: These tie to your bundles—e.g., AI Track sparks Consultant roles. Start small!")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption(
    f"NeuroConnections for {journey.student_name}: Exploration over optimization. "
    "Clarity comes from motion, not certainty. 🧠"
)