# neuroconnections/app/seed/course_catalog.py

COURSE_CATALOG = {
    "UIC": {
        "neuroscience_core": ["NEUS 484: Neuroscience I", "NEUS 485: Neuroscience II", "BIOS 286: Biology of the Brain"],
        "computational": ["CS 111: Intro to Computer Science", "BIOS 302: Biostatistics", "NEUS 444: Data Literacy in Neuroscience"],
        "ethics": ["PHIL 102: Introductory Philosophy", "NEUS 310: Neuroethics (or PHIL cross-list)"],
        "low_load": ["NEUS 101: Intro to Neuroscience"],
        "bundles": [
            {"name": "AI/Tech Track", "courses": ["NEUS 484", "CS 111", "BIOS 302", "NEUS 444"], "rationale": "Strong foundation for modeling brain data and neuro-AI applications.", "careers": "Neurotech, data science, computational neuroscience roles"},
            {"name": "Clinical/Med Track", "courses": ["NEUS 485", "PSCH 242: Abnormal Psychology", "BIOS 110"], "rationale": "Prepares for patient-facing or clinical research paths.", "careers": "Med school, PA, clinical research coordinator, therapist"},
            {"name": "Neuro + Finance/Business", "courses": ["NEUS 484", "ACTG 210: Intro to Accounting", "ECON 120: Principles of Microeconomics"], "rationale": "Combines brain science with business for neuromarketing or biotech startups.", "careers": "Neuromarketing consultant, biotech venture roles, neuroeconomics"},
            {"name": "Neuro + Law & Policy", "courses": ["NEUS 310 Neuroethics", "POLS 101", "PHIL 102"], "rationale": "Explores legal/ethical issues in brain tech and mental health policy.", "careers": "Neurolaw, science policy, regulatory affairs, ethics consulting"},
            {"name": "Neuro + Communications", "courses": ["NEUS 484", "COMM 101: Intro to Communication", "ENGL 160: Academic Writing"], "rationale": "Builds skills to communicate complex neuroscience to the public.", "careers": "Science writer, science communicator, outreach/education"},
            {"name": "Low Load Exploratory", "courses": ["NEUS 101", "PSCH 100: Intro to Psych", "BIOS 100"], "rationale": "Gentle intro with minimal workload to test interest.", "careers": "Any path — great for first-year exploration"}
        ]
    },

    "PITT": {
        "neuroscience_core": ["NROSCI 1000: Intro to Neuroscience", "NROSCI 1011: Functional Neuroanatomy", "NROSCI 1012: Neurophysiology"],
        "computational": ["CS 1530: Principles of Computer Science", "STAT 1000", "NROSCI 1250: Human Physiology"],
        "ethics": ["PHIL 0010", "NROSCI 0080: Neuroethics"],
        "low_load": ["NROSCI 0080: Brain and Behavior"],
        "bundles": [
            {"name": "AI/Tech Track", "courses": ["NROSCI 1000", "CS 1530", "STAT 1000"], "rationale": "Excellent for neural modeling and Pitt’s strong cognitive science ties.", "careers": "Computational neuro, AI/neurotech research"},
            {"name": "Clinical/Med Track", "courses": ["NROSCI 1011", "PSY 0310: Abnormal Psych", "BIO 1611"], "rationale": "Strong pre-med foundation with clinical neuroscience focus.", "careers": "Med school, clinical roles, psychiatry paths"},
            {"name": "Neuro + Finance/Business", "courses": ["NROSCI 1000", "BUS 0100: Intro to Business", "ECON 0100"], "rationale": "Neuro meets markets — great for neuromarketing or pharma business roles.", "careers": "Consulting, biotech business development"},
            {"name": "Neuro + Law & Policy", "courses": ["NROSCI 0080", "PHIL 0010", "PS 0100: Intro to Politics"], "rationale": "Policy and ethical dimensions of brain science.", "careers": "Science policy, advocacy, neurolaw"},
            {"name": "Neuro + Communications", "courses": ["NROSCI 1000", "COMM 0100", "ENGCMP 0200"], "rationale": "Science storytelling skills alongside core neuro.", "careers": "Journalism, science communication, outreach"},
            {"name": "Low Load Exploratory", "courses": ["NROSCI 0080", "PSY 0010"], "rationale": "Light introduction to test the waters."}
        ]
    },

    "BOWDOIN": {
        "neuroscience_core": ["PSY 2030: Neuroscience", "BIOL 2263: Animal Physiology", "PSY 2100: Behavioral Neuroscience"],
        "computational": ["COS 1101: Intro to CS", "MATH 2200: Probability & Stats"],
        "ethics": ["PHIL 2000: Moral Theory", "PSY 3010: Philosophy of Mind"],
        "low_load": ["PSY 1001: Intro to Psychology"],
        "bundles": [
            {"name": "AI/Tech Track", "courses": ["PSY 2030", "COS 1101", "MATH 2200"], "rationale": "Liberal arts strength + tech for unique neurotech profiles.", "careers": "Grad programs, startups, data roles"},
            {"name": "Clinical/Med Track", "courses": ["BIOL 2263", "PSY 2100", "CHEM 1040"], "rationale": "Solid pre-health foundation.", "careers": "Med/PA school, clinical research"},
            {"name": "Neuro + Finance/Business", "courses": ["PSY 2030", "ECON 1101", "GOV 1100"], "rationale": "Neuroeconomics and decision-making focus.", "careers": "Consulting, fintech with behavioral insights"},
            {"name": "Neuro + Law & Policy", "courses": ["PHIL 2000", "GOV 1100", "PSY 3010"], "rationale": "Ethics and policy through a liberal arts lens.", "careers": "Law school, policy, advocacy"},
            {"name": "Neuro + Communications", "courses": ["PSY 2030", "ENGL 1101", "THEA 1101"], "rationale": "Storytelling and public engagement skills.", "careers": "Science writing, media, education"}
        ]
    },

    "Rutgers New Brunswick": {
        "neuroscience_core": ["01:146:245: Fundamentals of Neurobiology", "01:146:447: Clinical Neurobiology", "01:830:210: Intro to Neuroscience"],
        "computational": ["01:198:111: Intro to Computer Science", "01:960:285: Intro to Statistics"],
        "ethics": ["01:730:101: Intro to Philosophy", "01:146:465: Neurobiology of Pain & Addiction (ethics angle)"],
        "low_load": ["01:146:295: Essentials of Cell Biology & Neuroscience"],
        "bundles": [
            {"name": "AI/Tech Track", "courses": ["01:146:245", "01:198:111", "01:960:285"], "rationale": "Strong Rutgers CS + neuro synergy.", "careers": "Neurotech, data science, BCI roles"},
            {"name": "Clinical/Med Track", "courses": ["01:146:447", "01:830:210", "01:119:115"], "rationale": "Excellent pre-med pipeline.", "careers": "Med school, clinical research"},
            {"name": "Neuro + Finance/Business", "courses": ["01:146:245", "33:010:272: Intro to Financial Accounting", "01:220:102: Microeconomics"], "rationale": "Behavioral finance and neuromarketing.", "careers": "Fintech, consulting, biotech business"},
            {"name": "Neuro + Law & Policy", "courses": ["01:730:101", "01:790:101: Intro to Politics", "01:146:465"], "rationale": "Policy and legal issues in neuroscience.", "careers": "Law school, regulatory affairs, advocacy"},
            {"name": "Neuro + Communications", "courses": ["01:146:245", "04:189:101: Intro to Communication", "01:355:101: College Writing"], "rationale": "Public communication of science.", "careers": "Science journalism, outreach"}
        ]
    },

    "DePaul": {
        "neuroscience_core": ["PSY 377: Behavioral Neuroscience", "BIO 250: Cell Biology", "PSY 106: Intro to Neuroscience"],
        "computational": ["CSC 241: Intro to Computer Science", "MAT 242: Elements of Statistics"],
        "ethics": ["PHL 200: Intro to Philosophy", "PSY 380: Psychology and Law"],
        "low_load": ["PSY 105: Intro to Psychology"],
        "bundles": [
            {"name": "AI/Tech Track", "courses": ["PSY 377", "CSC 241", "MAT 242"], "rationale": "Chicago tech scene + DePaul CS strength.", "careers": "Neurotech startups, data roles"},
            {"name": "Clinical/Med Track", "courses": ["PSY 377", "PSY 347: Abnormal Psychology"], "rationale": "Strong clinical psychology ties.", "careers": "Therapy, med school pathways"},
            {"name": "Neuro + Finance/Business", "courses": ["PSY 377", "FIN 310: Intro to Finance", "MKT 301: Principles of Marketing"], "rationale": "Neuromarketing and consumer behavior focus.", "careers": "Marketing research, consulting"},
            {"name": "Neuro + Law & Policy", "courses": ["PHL 200", "PSY 380", "POL 101"], "rationale": "Law and ethics emphasis.", "careers": "Neurolaw, policy"}
        ]
    },

    "WashU": {
        "neuroscience_core": ["Biol 3411: Principles of the Nervous System", "Psych 360: Cognitive Neuroscience", "Biol 3058: Physiological Control Systems"],
        "computational": ["CSE 131: Intro to Computer Science", "Math 3200: Elementary to Intermediate Statistics"],
        "ethics": ["Phil 120: Problems in Philosophy", "Bioethics cross-list options"],
        "low_load": ["Psych 100: Intro to Psychology"],
        "bundles": [
            {"name": "AI/Tech Track", "courses": ["Biol 3411", "CSE 131", "Math 3200"], "rationale": "WashU’s elite computational and engineering resources.", "careers": "Top grad programs, neurotech R&D"},
            {"name": "Clinical/Med Track", "courses": ["Biol 3411", "Psych 360", "Chem 105"], "rationale": "Outstanding pre-med reputation.", "careers": "Medicine, research physician paths"},
            {"name": "Neuro + Finance/Business", "courses": ["Biol 3411", "Mgmt 100", "Econ 101"], "rationale": "Olin Business School synergy.", "careers": "Biotech entrepreneurship, consulting"},
            {"name": "Neuro + Law & Policy", "courses": ["Phil 120", "Bioethics", "Pol Sci 101"], "rationale": "Strong policy and ethics programs.", "careers": "Law school, government/neuro policy"}
        ]
    },

    "Rutgers Camden": {
        "neuroscience_core": ["50:830:201: Intro to Neuroscience", "50:120:245: Fundamentals of Neurobiology (cross-campus options)"],
        "computational": ["50:198:111: Intro to CS", "50:960:183: Intro to Statistics"],
        "ethics": ["50:730:101: Intro to Philosophy", "50:830:320: Psychology and Law"],
        "low_load": ["50:830:101: Intro to Psychology"],
        "bundles": [
            {"name": "AI/Tech Track", "courses": ["50:830:201", "50:198:111", "50:960:183"], "rationale": "Accessible entry to computational paths.", "careers": "Data roles, further study"},
            {"name": "Clinical/Med Track", "courses": ["50:830:201", "50:830:340: Abnormal Psychology"], "rationale": "Strong psych focus.", "careers": "Clinical, counseling paths"},
            {"name": "Neuro + Finance/Business", "courses": ["50:830:201", "52:390:101: Intro to Finance"], "rationale": "Business school access.", "careers": "Behavioral finance, consulting"},
            {"name": "Neuro + Law & Policy", "courses": ["50:730:101", "50:830:320"], "rationale": "Law and psychology intersection.", "careers": "Law school, advocacy"}
        ]
    }
}