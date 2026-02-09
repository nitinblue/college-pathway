# neuroconnections/app/services/career_service.py
# Comprehensive "day in the life" sparks for neuroscience paths post-BS

CAREER_SPARKS = {
    "Research Technician / Lab Assistant": {
        "vignette": "Meet Alex, post-undergrad research tech at a Chicago biotech spin-off (UIC connection). 8:30 AM: Check on the mouse colony, run quick health checks. Morning: Behavioral testing—tracking how stress affects learning (links to anxiety research you might relate to). Afternoon: Brain imaging data analysis in Python/MATLAB, prepping slides, and pipetting. 3 PM: Lab meeting—debate results with the team. End of day: Clean up, email mentor feedback, maybe listen to a neuroscience podcast on the train home. Mix of hands-on lab work, data crunching, and collaboration. Flexible hours, but focused weeks. $50K–$68K starting.",
        "prep_tips": {
            "UIC": ["Join LAS Neuroscience Club freshman year and shadow labs on brain plasticity or neuroimaging", "Seek undergrad research assistant positions early—many PIs hire sophomores", "Build stats and Python skills via coursework or free Coursera"],
            "PITT": ["Apply to Dietrich REU or similar summer research programs", "Volunteer in a cognitive neuroscience or behavioral lab", "Take advanced lab courses and learn data analysis tools"],
            "BOWDOIN": ["Coordinate neuroscience major with data science or biology for stronger lab skills", "Pursue research internships at Bigelow Lab or similar nearby facilities"]
        }
    },

    "Clinical Research Coordinator": {
        "vignette": "Jordan coordinates neuroscience clinical trials at a university-affiliated hospital. 7:45 AM: Review overnight emails and patient schedules. Morning: Screen and consent new participants for a study on anxiety treatments. Midday: Run study visits—collect surveys, run cognitive tests, or assist with EEG. Afternoon: Data entry into secure systems, adverse event reporting, and team coordination with doctors and sponsors. Late day: Prep regulatory documents. Patient interactions feel meaningful; some days are admin-heavy. Steady 9–5 with purpose. $55K–$75K starting.",
        "prep_tips": {
            "UIC": ["Volunteer at UI Health psych ward or neurology clinics", "Take Abnormal Psychology and research methods courses", "Look for clinical trial coordinator internships in Chicago"],
            "PITT": ["Shadow at Falk Medical Center or UPMC neuroscience studies", "Pursue certifications like Good Clinical Practice (GCP) online", "Join research clubs focused on mental health or neurology"],
            "BOWDOIN": ["Electives in health humanities or psychology", "Summer opportunities at Maine Medical Center or similar clinical sites"]
        }
    },

    "Clinician / Behavioral Health Specialist": {
        "vignette": "Taylor works as an entry-level neuro-informed therapist or behavioral specialist (often after BS + certification). 8 AM: Review patient notes—today's focus on a teen with ADHD and prefrontal cortex insights. Sessions: Guide mindfulness or cognitive exercises tied to latest brain science. Afternoon: Collaborate with psychiatrists on treatment plans, write progress notes, read new studies over lunch. Evenings: Decompress with yoga or journaling. High emotional reward when patients improve. Paths to PA, counseling, or further clinical roles. $52K–$70K starting.",
        "prep_tips": {
            "UIC": ["Volunteer at UI Health psych services; take PSCH 242 Abnormal Psych", "Pursue peer counseling or crisis hotline experience"],
            "PITT": ["Shadow via Falk or UPMC; get CBT or mental health first aid certification", "Join psychology/neuroscience clubs"],
            "BOWDOIN": ["Elect med humanities; summer clinical volunteering at Maine Med or community health centers"]
        }
    },

    "Neuromarketing / Consulting Specialist": {
        "vignette": "Sam works in neuromarketing consulting (post-Pitt BS). 9 AM: Client Zoom—'How can brain science improve our eco-brand ads?' Morning: Design EEG or eye-tracking studies on consumer attention. Afternoon: Literature review on dopamine and decision-making, build presentation slides on 'ethical nudges'. Late day: Pitch insights to team. Blends science, storytelling, and business. Travel to conferences, creative energy. $68K–$90K starting.",
        "prep_tips": {
            "UIC": ["Take business + neuroscience ethics courses; intern at Chicago policy or consulting firms"],
            "PITT": ["Minor in communications; join consulting or entrepreneurship clubs", "Mock cases on neurotech or consumer behavior"],
            "BOWDOIN": ["Pair neuroscience with economics; volunteer for behavioral health or policy talks"]
        }
    },

    "Neuroscience Data Analyst / Computational Specialist": {
        "vignette": "Riley analyzes brain data for a research institute or neurotech company. Morning: Clean and process large EEG/fMRI datasets. Midday: Run statistical models or machine learning scripts in Python/R to find patterns in memory or attention. Afternoon: Visualize results, collaborate with neuroscientists on interpretations. Some days involve presenting findings. Intellectual, flexible, high demand. $75K–$105K starting.",
        "prep_tips": {
            "UIC": ["Heavy focus on computational neuroscience and programming electives", "Projects with real datasets"],
            "PITT": ["Strong stats and coding foundation; Coursera specializations"],
            "BOWDOIN": ["Combine neuro major with data science or computer science minor"]
        }
    },

    "Neurotechnology / BCI Specialist (Entry-level)": {
        "vignette": "Casey is a research assistant in brain-computer interfaces at a neurotech startup. Morning: Calibrate EEG or implant hardware for testing. Midday: Run signal processing scripts, test with participants (e.g., thought-controlled cursors). Afternoon: Debug code, document results, team brainstorming on improving accuracy. Exciting, cutting-edge work—mix of hardware, software, and human testing. Fast-paced. $80K–$110K starting in many hubs.",
        "prep_tips": {
            "UIC": ["Take engineering-adjacent or computational neuro courses; join maker/engineering clubs"],
            "PITT": ["Leverage nearby tech and engineering resources"],
            "BOWDOIN": ["Pair with physics, CS, or data science; seek neurotech-related internships"]
        }
    },

    "Biotech / Pharma Research Associate": {
        "vignette": "Morgan works in R&D at a biotech firm developing neurological therapies. 8 AM: Cell culture or molecular assays. Morning: Test drug compounds on neural models. Afternoon: Data analysis, protocol updates, team huddles on next experiments. Some lab grunt work, but real impact on future treatments. Corporate resources, good benefits. $65K–$85K starting.",
        "prep_tips": {
            "UIC": ["Intern at Chicago-area biotech companies", "Pharmacology or cell biology electives"],
            "PITT": ["Strong pharma/biotech ecosystem nearby"],
            "BOWDOIN": ["Focus on lab research experience"]
        }
    },

    "Science Writer / Communicator": {
        "vignette": "Avery is a science writer or content creator focused on neuroscience. Morning: Research latest papers on neuroplasticity or AI ethics. Afternoon: Write articles, scripts for videos/podcasts, or social media explainers. Some days involve interviewing researchers. Creative, flexible, public-facing. $55K–$80K starting (higher with freelancing).",
        "prep_tips": {
            "UIC": ["Writing-intensive courses + neuro; Chicago journalism/science comms scene"],
            "PITT": ["Communications minor; student media or science outreach"],
            "BOWDOIN": ["Liberal arts strength—excellent writing foundation"]
        }
    },

    "Science Policy / Neuroethics Advisor": {
        "vignette": "Jordan works in policy or ethics at a think tank or government office. Morning: Review new neurotech regulations. Afternoon: Draft briefs on brain privacy, attend meetings on mental health policy, synthesize research for non-scientists. Intellectual, impactful, less lab time. $65K–$95K starting.",
        "prep_tips": {
            "UIC": ["Intern at Chicago Council on Global Affairs or policy organizations", "Neuroethics or philosophy of science courses"],
            "PITT": ["Policy or public health clubs"],
            "BOWDOIN": ["Strong liberal arts + advocacy experience"]
        }
    },

    "Regulatory Affairs Specialist (Neuro devices/drugs)": {
        "vignette": "Taylor ensures neuroscience products (devices, drugs) meet FDA standards. Day involves reviewing clinical data, preparing submissions, coordinating with teams and regulators. Detail-oriented, high responsibility, good work-life balance in many roles. $70K–$95K starting.",
        "prep_tips": {
            "UIC": ["Courses in regulatory science or ethics; Chicago pharma presence"],
            "PITT": ["Strong health sciences ecosystem"],
            "BOWDOIN": ["Focus on research + writing skills"]
        }
    }
}

def get_spark(role: str, university: str):
    spark = CAREER_SPARKS.get(role, {})
    tips = spark.get("prep_tips", {}).get(university, ["Explore general neuroscience clubs and informational interviews!"])
    return {
        "vignette": spark.get("vignette", "Spark coming soon—feel free to add your own reflections!"),
        "prep": tips,
        "actions": [f"Reflect: Which parts of this role feel exciting or surprising? ({role})"]
    }