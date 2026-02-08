# NeuroExplorer

A personal, long-lived exploration app to help a student (and parent) navigate **neuroscience, skills, and future pathways** without premature career pressure.

This project is intentionally designed as:

* Personal-first
* Reflection-driven
* Exploration > optimization

---

## 1. What This App Does

* Creates a **Learning Journey** for a student
* Lets the student add **Exploration Steps** (curiosity, skills, ethics, workload)
* Automatically suggests:

  * Light, low-pressure **action items**
  * Relevant **courses** (university-specific)
* Builds **history over time** (thoughts, actions, growth)

---

## 2. Tech Stack

* Python 3.11+
* Streamlit (UI)
* FastAPI (API layer – optional early)
* SQLite (local persistence)
* SQLAlchemy ORM

---

## 3. Folder Structure

```text
neuroexplorer/
├── README.md
├── requirements.txt
├── data/
│   └── neuroexplorer.db
├── app/
│   ├── main.py
│   ├── config.py
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models.py
│   ├── services/
│   │   ├── journey_service.py
│   │   └── recommendation_service.py
│   └── seed/
│       └── course_catalog.py
├── ui/
│   └── streamlit_app.py
└── scripts/
    └── init_db.py
```

---

## 4. Setup Instructions

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python neuroconnections/scripts/init_db.py
streamlit run neuroconnections/ui/streamlit_app.py
```

uvicorn app.main:app --reload


---

## 5. Design Philosophy

* No forced decisions
* Low workload bias
* Skills > credentials
* History matters more than outcomes

---

## 6. Future Extensions

* Semester planner
* Skill graph
* Career story modules
* AI reflection prompts
* Multi-student support

---

## 7. Guiding Principle

> This app is not about choosing a career.
> It is about learning how to think, explore, and grow with confidence.
