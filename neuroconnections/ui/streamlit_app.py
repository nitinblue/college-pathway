import streamlit as st
from sqlalchemy.orm import Session
import io
import tempfile
import os

from neuroconnections.app.db.session import SessionLocal
from neuroconnections.app.db.models import Journey, ExplorationStep, ActionItem
from neuroconnections.app.services.recommendation_service import recommend
from neuroconnections.app.services.journey_service import add_exploration_step, add_stream_exploration
from neuroconnections.app.services.stream_service import get_all_streams, get_stream_details
from neuroconnections.app.services.career_service import get_spark, CAREER_SPARKS
import networkx as nx
import matplotlib.pyplot as plt

# Voice Reflections
try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False

st.set_page_config(page_title="NeuroConnections", layout="wide")
st.title("🧠 NeuroConnections")
st.caption("Exploration over optimization • College is the stage — you are the director")

db: Session = SessionLocal()

# ----------------------------- Sidebar -----------------------------
st.sidebar.header("Journey")

journeys = db.query(Journey).all()
journey_map = {f"{j.student_name} ({j.university})": j.id for j in journeys}

selected_journey_label = st.sidebar.selectbox(
    "Select existing journey",
    options=["Create New"] + list(journey_map.keys())
)

journey = None

if selected_journey_label == "Create New":
    st.sidebar.subheader("Create New Journey")
    student_name = st.sidebar.text_input("Student name")
    university = st.sidebar.selectbox(
        "University (or intended)",
        ["UIC", "PITT", "BOWDOIN", "Rutgers New Brunswick", "DePaul", "WashU", "Rutgers Camden"]
    )
    if st.sidebar.button("Create Journey"):
        from neuroconnections.app.services.journey_service import create_journey
        journey = create_journey(db, student_name, university)
        st.sidebar.success("Journey created! Refreshing...")
        st.rerun()
else:
    journey_id = journey_map[selected_journey_label]
    journey = db.query(Journey).get(journey_id)

if journey is None:
    st.warning("Please select or create a journey to continue.")
    st.stop()

# Progress
steps = db.query(ExplorationStep).filter_by(journey_id=journey.id).all()
total_actions = sum(len(step.actions) for step in steps)
completed_actions = sum(1 for step in steps for action in step.actions if action.completed)
progress = (completed_actions / max(total_actions, 1)) * 100
st.sidebar.metric("Exploration Progress", f"{progress:.0f}%")
st.sidebar.progress(progress / 100)

# ============================== TABS ==============================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🧭 Discover Streams",
    "🛤️ My Path",
    "📚 Course Bundles",
    "🔥 Career Sparks",
    "🔑 Ownership Journey"
])

# ----------------------------- 1. Discover Streams -----------------------------
with tab1:
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
            st.checkbox(action, key=f"chk_{selected_stream}_{action[:30]}")

        if st.button("Add these exploration ideas to My Path"):
            add_stream_exploration(db, journey.id, selected_stream)
            st.success("Added to your journey!")

# ----------------------------- 2. My Path -----------------------------
with tab2:
    st.subheader(f"Journey: {journey.student_name} – {journey.university}")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### Add Exploration Step")
        theme = st.selectbox("Exploration Theme", ["Curiosity", "Skill", "Ethics", "Low Load"])
        
        st.markdown("#### 🎙️ Voice Reflection (Optional)")
        audio_input = st.audio_input("Record your thoughts")
        transcribed_text = ""
        if audio_input and WHISPER_AVAILABLE:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                tmp_file.write(audio_input.getvalue())
                tmp_file_path = tmp_file.name
            try:
                model = whisper.load_model("base")
                result = model.transcribe(tmp_file_path)
                transcribed_text = result["text"]
            except Exception as e:
                st.error(f"Transcription error: {e}")
            finally:
                os.unlink(tmp_file_path)

        reflection = st.text_area("Reflection", value=transcribed_text, height=150)
        use_bundles = st.checkbox("Suggest full course combinations?")
        
        if st.button("Add Step"):
            mode = "combinations" if use_bundles else "single"
            add_exploration_step(db, journey.id, theme, reflection, mode=mode)
            st.success("Step added!")
            st.rerun()

    with col2:
        st.info("- No decisions required\n- Reflection builds clarity\n- Actions stay small & reversible")

    # History
    st.markdown("---")
    st.markdown("## 🕰️ Exploration History")
    if not steps:
        st.write("No steps yet. Add one above!")
    else:
        for step in steps:
            with st.expander(f"{step.theme} – Step #{step.id}"):
                st.write(step.reflection)
                for action in step.actions:
                    checked = st.checkbox(action.description, value=action.completed, key=f"action_{action.id}")
                    if checked != action.completed:
                        action.completed = checked
                        db.commit()

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

# ----------------------------- 3. Course Bundles -----------------------------
with tab3:
    st.markdown("### 🔍 Course Bundles for Careers")
    theme_for_bundles = st.selectbox("Theme", ["Curiosity", "Skill", "Ethics", "Low Load"])
    if st.button("Generate Bundles"):
        bundles = recommend(theme_for_bundles, journey.university, mode="combinations")
        for bundle in bundles:
            with st.expander(bundle['name']):
                st.write(bundle['rationale'])
                for course in bundle['courses']:
                    st.write(f"- {course}")
                st.info(bundle['careers'])

# ----------------------------- 4. Career Sparks -----------------------------
with tab4:
    st.markdown("### 👥 Career Sparks")
    roles = list(CAREER_SPARKS.keys())
    selected_role = st.selectbox("Choose a Role", roles)
    spark_data = get_spark(selected_role, journey.university)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write(spark_data["vignette"])
    with col_b:
        for tip in spark_data["prep"]:
            st.checkbox(tip)
        if st.button(f"Claim '{selected_role}' Spark"):
            st.success("Spark added!")

# ----------------------------- 5. Ownership Journey -----------------------------
with tab5:
    st.subheader("🔑 You Are the Director")
    st.markdown("""
    **College gives you the stage — the classes, labs, clubs, and professors.**  
    **You are the one who writes the script and directs the play.**  

    You don’t need to have everything figured out right now.  
    Real direction comes from **taking small actions + reflecting honestly**.  
    This is your command center for owning the process.
    """)

    st.markdown("### Weekly Commitment")
    commitment = st.text_input("What one small exploration will you do this week?")
    if st.button("Lock in this week's commitment"):
        latest_step = steps[-1] if steps else None
        step_id = latest_step.id if latest_step else None
        db.add(ActionItem(description=f"Weekly Commitment: {commitment}", step_id=step_id, parent_bundle="Ownership"))
        db.commit()
        st.success("Commitment saved!")

    st.markdown("### Experiment Builder")
    experiments = {
        "Informational Interview": "Message 1–2 people working in a stream you’re curious about.",
        "Lab / Club Visit": "Attend one lab meeting or club event this month.",
        "Online Micro-Course": "Complete one short module on Coursera/edX related to a stream.",
        "Reflection Deep Dive": "Journal for 30 minutes about what felt energizing lately."
    }
    for name, desc in experiments.items():
        if st.checkbox(f"**{name}**: {desc}"):
            if st.button(f"Add {name} to My Path", key=f"exp_{name}"):
                add_exploration_step(db, journey.id, "Ownership", f"Experiment: {name}")
                st.success("Added!")

    st.markdown("### Quarterly Review")
    if st.button("Start Quarterly Reflection"):
        st.text_area("What surprised or energized me most recently?")
        st.text_area("What felt draining?")
        st.text_area("What is one new experiment I want to try next?")
        if st.button("Save Reflection"):
            st.success("Reflection saved to My Path.")

# Footer
st.markdown("---")
st.caption(f"NeuroConnections for {journey.student_name} • College is the stage. You are the director. 🧠")