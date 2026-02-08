import streamlit as st
from sqlalchemy.orm import Session

from neuroconnections.app.db.session import SessionLocal
from neuroconnections.app.db.models import Journey, ExplorationStep, ActionItem
from neuroconnections.app.services.recommendation_service import recommend
from neuroconnections.app.services.journey_service import add_exploration_step
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="NeuroConnections", layout="wide")
st.title("🧠 NeuroConnections")
st.caption("A guided exploration space — no pressure, no premature decisions")

db: Session = SessionLocal()

# -----------------------------
# Sidebar – Journey Selection
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
    university = st.sidebar.selectbox("University", ["UIC", "PITT"])

    if st.sidebar.button("Create Journey"):
        journey = Journey(student_name=student_name, university=university)
        db.add(journey)
        db.commit()
        st.sidebar.success("Journey created. Refresh selection.")
        st.rerun()  # Use st.rerun() instead of st.stop() for Streamlit 1.28+ (refreshes without stopping)
else:
    journey_id = journey_map[selected_journey_label]
    journey = db.query(Journey).get(journey_id)

# Now check and render
if journey is None:
    st.warning("Please select or create a journey to continue.")
    st.stop()

# Main content (safe to access journey now)
st.subheader(f"Journey: {journey.student_name} – {journey.university}")

tab1, tab2, tab3 = st.tabs(["My Path", "Add Spark", "Career Sparks"])

# -----------------------------
# Main – Journey Overview
# -----------------------------
st.subheader(f"Journey: {journey.student_name} – {journey.university}")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Add Exploration Step")

    theme = st.selectbox(
        "Exploration Theme",
        ["Curiosity", "Skill", "Ethics", "Low Load"]
    )

    reflection = st.text_area(
        "Reflection (student’s thoughts, doubts, interests)",
        height=150,
        placeholder="What felt interesting? Confusing? Energizing?"
    )
    
    use_bundles = st.checkbox("Suggest full course combinations? (for career paths)")
    if st.button("Add Step"):
        step = ExplorationStep(
            theme=theme,
            reflection=reflection,
            journey_id=journey.id
        )
        db.add(step)
        db.flush()
        mode = "combinations" if use_bundles else "single"  # New
        # Call updated service: from neuroconnections.app.services.journey_service import add_exploration_step
        add_exploration_step(db, journey.id, theme, reflection, mode=mode)  # Use service for consistency
        
        db.commit()
        st.success("Step added with recommendations!")
        st.rerun()
    
        courses = recommend(theme, journey.university)
        for course in courses:
            db.add(
                ActionItem(
                    description=f"Explore course: {course}",
                    step_id=step.id
                )
            )

        db.commit()
        st.success("Exploration step added")
        st.rerun()  # Refresh the UI to show the new step

with col2:
    st.markdown("### Why This Matters")
    st.info(
        "- No decisions required\n"
        "- Reflection builds clarity\n"
        "- Actions stay small & reversible\n"
        "- History reduces anxiety"
    )

    st.markdown("### 🌿 Suggested Paths")
    if st.button("Generate Neuroscience + Complements for This School"):
        bundles = recommend("combinations", journey.university, mode="combinations")  # Direct call
        for bundle in bundles:
            with st.expander(f"{bundle['name']} – Why? {bundle['rationale']}"):
                st.write("**Courses to Explore:**")
                for course in bundle['courses']:
                    st.write(f"- {course}")
                st.info(f"**Post-Grad Sparks:** {bundle['careers']}")

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
    st.write("No exploration steps yet.")
else:
    for step in steps:
        with st.expander(f"{step.theme} – Step #{step.id}", expanded=False):
            st.markdown("**Reflection**")
            st.write(step.reflection)

            st.markdown("**Action Items**")
            actions_by_bundle = {}  # Group logic here
            checked = None  # Initialize checked variable
            for action in step.actions:
                if hasattr(action, 'is_bundle') and action.is_bundle:
                    actions_by_bundle[action.parent_bundle] = actions_by_bundle.get(action.parent_bundle, []) + [action]
                else:
                    checked = st.checkbox(
                        action.description,
                        value=action.completed,
                        key=f"action_{action.id}"
                )
                if checked != action.completed:
                    action.completed = checked
                    db.commit()
if st.button("🌟 Show Anushka's Mind Map"):
    G = nx.Graph()
    # Simple nodes/edges from your catalog
    G.add_edges_from([
        ("Neuroscience Core", "AI/Tech Track"),
        ("AI/Tech Track", "Careers: Data Scientist @ Neuralink"),
        ("Clinical Track", "Med School Path"),
        # Add more based on her reflections
    ])
    fig, ax = plt.subplots()
    nx.draw(G, with_labels=True, node_color="lightblue", ax=ax)
    st.pyplot(fig)
    st.caption("Click nodes to expand—your paths are branching, not a straight line!")
# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption(
    "NeuroExplorer is about exploration, not optimization. "
    "Clarity comes from motion, not certainty."
)
