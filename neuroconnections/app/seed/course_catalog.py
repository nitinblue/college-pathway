COURSE_CATALOG = {
    "UIC": {
        "neuroscience_core": ["NEUR 220: Neuroscience I", "NEUR 221: Neuroscience II"],
        "computational": ["CS 111: Introduction to Computer Science", "BIOS 302: Biostatistics"],
        "ethics": ["PHIL 102: Introductory Philosophy", "NEUR 310: Neuroethics"],
        "low_load": ["NEUR 101: Intro to Brain & Behavior"],
        # New: Bundles (list of dicts: {'name': str, 'courses': list, 'rationale': str, 'careers': str})
        "bundles": [
            {
                "name": "AI/Tech Track",
                "courses": ["NEUR 220: Neuroscience I", "CS 111: Introduction to Computer Science", "BIOS 302: Biostatistics"],
                "rationale": "Builds skills in modeling brain data for AI—perfect for tech innovation.",
                "careers": "Neurotech engineer, data scientist at Neuralink-like firms, grad school in comp neuro."
            },
            {
                "name": "Clinical/Med Track",
                "courses": ["NEUR 221: Neuroscience II", "PSCH 242: Abnormal Psychology", "BIOS 110: Biology of Populations"],
                "rationale": "Focuses on brain disorders and human biology for patient-facing work.",
                "careers": "Neurologist, therapist, med school (e.g., UIC's program), clinical research."
            },
            {
                "name": "Ethics/Policy Track",
                "courses": ["NEUR 310: Neuroethics", "PHIL 102: Introductory Philosophy", "POLS 101: Intro to Politics"],
                "rationale": "Explores moral questions in brain science, like AI consciousness or neural privacy.",
                "careers": "Bioethicist, policy advisor (e.g., FDA), law school with neuro focus."
            }
        ]
    },
    "PITT": {  # University of Pittsburgh
        "neuroscience_core": ["NROSCI 1000: Intro to Neuroscience", "NROSCI 1010: Systems Neuroscience"],
        "computational": ["CS 1530: Principles of Computer Science", "STAT 1000: Basic Statistics"],
        "ethics": ["PHIL 0010: Intro to Philosophy", "NROSCI 0080: Neuroethics"],
        "low_load": ["NROSCI 1005: Brain Health"],
        "bundles": [
            {
                "name": "AI/Tech Track",
                "courses": ["NROSCI 1000: Intro to Neuroscience", "CS 1530: Principles of Computer Science", "STAT 1000: Basic Statistics"],
                "rationale": "Combines brain wiring with coding/stats for simulating neural networks.",
                "careers": "Computational neuroscientist, AI researcher at Pitt's Center for Neural Basis of Cognition."
            },
            {
                "name": "Clinical/Med Track",
                "courses": ["NROSCI 1010: Systems Neuroscience", "PSY 0310: Abnormal Psychology", "BIO 1611: Biological Concepts"],
                "rationale": "Dives into brain-behavior links for diagnostics and treatment.",
                "careers": "Psychiatrist, clinical trials coordinator, Pitt Med School pathway."
            },
            {
                "name": "Ethics/Policy Track",
                "courses": ["NROSCI 0080: Neuroethics", "PHIL 0010: Intro to Philosophy", "LAW 5001: Intro to Law (if cross-reg)"],
                "rationale": "Tackles debates like brain-computer interfaces and equity in neuro research.",
                "careers": "Science policy analyst, ethicist at think tanks, public health advocacy."
            }
        ]
    },
    "BOWDOIN": {  # Bowdoin College (Brunswick, ME) – more liberal arts, fewer formal neuro courses
        "neuroscience_core": ["PSY 2030: Neuroscience", "BIOL 2263: Animal Physiology"],
        "computational": ["COS 1101: Intro to Computer Science", "MATH 2200: Probability"],
        "ethics": ["PHIL 2000: Moral Theory", "PSY 3010: Philosophy of Mind"],
        "low_load": ["PSY 1001: Intro to Psych"],
        "bundles": [
            {
                "name": "AI/Tech Track",
                "courses": ["PSY 2030: Neuroscience", "COS 1101: Intro to Computer Science", "MATH 2200: Probability"],
                "rationale": "Blends brain science with coding for data-driven insights (Bowdoin's strong in this).",
                "careers": "Tech consultant, grad programs at MIT/Harvard, startup founder in edtech."
            },
            {
                "name": "Clinical/Med Track",
                "courses": ["BIOL 2263: Animal Physiology", "PSY 2100: Behavioral Neuroscience", "CHEM 1040: Organic Chem I"],
                "rationale": "Emphasizes biological mechanisms for health sciences.",
                "careers": "Physician assistant, research in mental health, med school (Bowdoin alums excel here)."
            },
            {
                "name": "Ethics/Policy Track",
                "courses": ["PHIL 2000: Moral Theory", "PSY 3010: Philosophy of Mind", "ENVS 1101: Environmental Studies"],
                "rationale": "Links neuro to broader societal issues like climate impacts on cognition.",
                "careers": "Environmental neuro policy, nonprofit leader, law/grad school in ethics."
            }
        ]
    }
}