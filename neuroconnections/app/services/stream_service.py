# neuroconnections/app/services/stream_service.py
# Core data for neuroscience streams/paths

STREAMS = {
    "Academic & Laboratory Research": {
        "icon": "🔬",
        "description": "Deep scientific discovery through experiments, data analysis, and theory-building. Often leads to research careers or academia.",
        "post_grad": "BS → Research technician or lab assistant ($45K–$65K). Most continue to PhD (5–7 years) for senior roles. Long-term: Principal investigator, professor, or industry scientist. Lifestyle: Flexible but intense during experiments; strong community of curious people.",
        "professions": [
            {
                "title": "Research Technician / Lab Manager",
                "vignette": "8 AM: Prep brain slices or run behavioral tests on mice. Afternoon: Analyze imaging data in Python/R. Team meetings to discuss findings. Mix of hands-on lab work, stats, and writing. Rewarding when you see a pattern emerge.",
                "salary": "$48K–$70K starting"
            },
            {
                "title": "PhD Student / Postdoc → Professor",
                "vignette": "Design your own experiments, mentor undergrads, write grants and papers. Travel to conferences. High autonomy once established, but competitive."
            }
        ],
        "undergrad_actions": {
            "UIC": ["Join a faculty lab early (e.g., brain plasticity or neuroimaging)", "Take advanced lab courses + stats", "Apply for summer research programs (SURF or similar)"],
            "PITT": ["Dietrich REU or undergrad research in neuroscience labs", "Build strong stats/programming foundation"],
            "BOWDOIN": ["Work with professors on thesis-level projects", "Intern at Bigelow Lab or similar"]
        }
    },

    "Clinical & Healthcare": {
        "icon": "🩺",
        "description": "Applying neuroscience to patient care — neurology, psychiatry, therapy, or clinical research.",
        "post_grad": "BS → Clinical research coordinator, medical assistant, or tech roles ($50K–$70K). Common next steps: MD, PA, nursing, speech-language pathology, or counseling programs. Lifestyle: People-focused, meaningful impact, often structured hours.",
        "professions": [
            {
                "title": "Clinical Research Coordinator",
                "vignette": "Screen participants for studies on anxiety/depression, collect data (EEG, surveys), work with doctors. Blend of science and direct patient interaction."
            },
            {
                "title": "Neurologist or Psychiatrist (after MD)",
                "vignette": "Diagnose and treat brain-related conditions. Combine latest research with real human stories."
            },
            {
                "title": "Speech-Language Pathologist or Therapist",
                "vignette": "Help people recover communication or cognitive skills after stroke/trauma."
            }
        ],
        "undergrad_actions": {
            "UIC": ["Volunteer at UI Health (psych ward or neurology)", "Take Abnormal Psych + neuroscience clinical courses"],
            "PITT": ["Shadow at Falk Medical Center", "Pursue CBT or clinical volunteering"],
            "BOWDOIN": ["Electives in health humanities", "Summer at Maine Medical Center"]
        }
    },

    "Neurotechnology & Brain-Computer Interfaces": {
        "icon": "🤖",
        "description": "Building tech that interfaces with the brain — Neuralink-style devices, prosthetics, AI + neuroscience.",
        "post_grad": "BS → Neurotech research assistant or software role in neuro startups ($70K–$100K+). Often MS/PhD or strong coding portfolio helps. Fast-moving, innovative field.",
        "professions": [
            {
                "title": "Neurotech Research Engineer / BCI Specialist",
                "vignette": "Test brain-computer interfaces, analyze neural signals, collaborate with engineers and neuroscientists. Exciting mix of hardware, software, and biology."
            },
            {
                "title": "Data Scientist in Neurotech",
                "vignette": "Turn massive brain datasets into insights for device improvement."
            }
        ],
        "undergrad_actions": {
            "UIC": ["Take computational neuroscience + programming courses", "Join engineering/neuro clubs"],
            "PITT": ["Leverage strong engineering programs nearby"],
            "BOWDOIN": ["Combine neuro with data science or physics"]
        }
    },

    "Biotech, Pharma & Industry R&D": {
        "icon": "🧪",
        "description": "Translating neuroscience into real-world products — drugs, therapies, diagnostics.",
        "post_grad": "BS → Lab scientist or clinical trial associate ($60K–$85K). MS often helps for advancement. Corporate or startup pace; good pay and resources.",
        "professions": [
            {
                "title": "Scientist in Biotech/Pharma",
                "vignette": "Develop new treatments for neurological disorders. Lab work + team projects + regulatory knowledge."
            },
            {
                "title": "Clinical Trial Manager",
                "vignette": "Oversee studies testing new brain therapies."
            }
        ],
        "undergrad_actions": {
            "UIC": ["Intern at Chicago biotech firms", "Take pharmacology-related courses"],
            "PITT": ["Strong pharma presence nearby"],
            "BOWDOIN": ["Focus on research experience"]
        }
    },

    "Computational Neuroscience & Data Science": {
        "icon": "📊",
        "description": "Using code, modeling, and big data to understand the brain.",
        "post_grad": "BS → Data analyst or junior data scientist in neuroscience contexts ($80K–$110K). Very strong job market; coding + neuro is powerful.",
        "professions": [
            {
                "title": "Neuroscience Data Scientist",
                "vignette": "Analyze fMRI, EEG, or single-cell data. Build models that predict brain behavior."
            }
        ],
        "undergrad_actions": {
            "All": ["Double minor or take heavy programming/stats", "Projects with real neuro datasets"]
        }
    },

    "Policy, Ethics & Science Communication": {
        "icon": "📜",
        "description": "Using neuroscience knowledge for policy, ethics, law, journalism, or public education.",
        "post_grad": "BS → Science writer, policy analyst, or ethics roles ($55K–$80K). Often master’s (MPH, science comms, law) helps.",
        "professions": [
            {
                "title": "Science Policy Advisor / Neuroethicist",
                "vignette": "Advise on brain-related regulations (e.g., neurotech ethics, mental health policy)."
            },
            {
                "title": "Science Journalist / Communicator",
                "vignette": "Write about breakthroughs in accessible ways — podcasts, articles, outreach."
            }
        ],
        "undergrad_actions": {
            "UIC": ["Chicago Council on Global Affairs internships", "Neuroethics courses"],
            "PITT": ["Comms minor + policy clubs"],
            "BOWDOIN": ["Liberal arts strength — writing + neuro"]
        }
    }
}

def get_all_streams():
    return STREAMS

def get_stream_details(stream_name: str, university: str):
    stream = STREAMS.get(stream_name)
    if not stream:
        return None
    actions = stream.get("undergrad_actions", {}).get(university) or stream.get("undergrad_actions", {}).get("All", [])
    return {**stream, "recommended_actions": actions}