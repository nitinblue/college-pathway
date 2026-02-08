# Seeds "day in the life" stories + prep tips, tied to universities/bundles
CAREER_SPARKS = {
    "Researcher": {
        "vignette": "Meet Alex, post-undergrad lab tech at a Chicago biotech (think UIC spin-off). 8 AM: Brew coffee, check mouse behaviors in the neural imaging suite—today's tracking how stress rewires teen brains (nod to your apps anxiety!). 10 AM: Run stats on data (Python script, 20% 'aha' moments). Noon: Team huddle—debate if this leads to ADHD therapies. Afternoon: Pipette preps (tedious but rhythmic), end with emailing mentors for feedback. Evenings? Podcast on new fMRI tech. It's 60% curiosity, 40% grind—flex hours, but weekends sacred.",
        "prep_tips": {
            "UIC": ["Join LAS Neuroscience Club freshman year—shadow labs on brain plasticity."],
            "PITT": ["Apply to Dietrich REU summer program; build stats skills via free Coursera."],
            "BOWDOIN": ["Coordinate neuro major with data sci—intern at Bigelow Lab for coastal neuro links."]
        }
    },
    "Consultant": {
        "vignette": "Sarah, neuro consultant at a marketing firm (HeyHuman-style, post-Pitt BS). 9 AM: Zoom with client—'How can brain science boost ad recall for eco-brands?' Brainstorm neuromarketing experiments (EEG on focus). 11 AM: Dive into lit review—'Dopamine hits from green visuals?' Lunch: Walk in Grant Park, ideate. Afternoon: Deck-building—slides on 'ethical nudges' for behavior change. 4 PM: Pitch to team, tweak based on feedback. Wrap by 6, freelance gig on AI ethics. High-energy, travel (Chicago conferences), $70K start—blends science + storytelling.",
        "prep_tips": {
            "UIC": ["Take BUS 101 + NEUR ethics; intern at Chicago Council on Global Affairs for policy angles."],
            "PITT": ["Minor in comms; join consulting club—mock cases on neurotech startups."],
            "BOWDOIN": ["Pair with econ; volunteer for Maine Behavioral Health talks."]
        }
    },
    "Clinician": {  # E.g., therapist/research hybrid
        "vignette": "Jordan, entry-level neuro clinician at a Pitt-affiliated clinic (after BS). 7:30 AM: Review patient charts—today's a teen with anxiety, linking to prefrontal tweaks. 9 AM: Session—guide mindfulness exercises, tie to latest neuro studies (low-stakes chats build trust). Noon: Collaborate with docs on trial data (e.g., psilocybin for depression). Afternoon: Write notes, read journals over tea. Evenings: Yoga to decompress. Patient wins feel electric—$55K, steady 9-5, paths to PA school if hooked.",
        "prep_tips": {
            "UIC": ["Volunteer at UI Health psych ward; take PSCH 242 Abnormal Psych."],
            "PITT": ["Shadow via Falk Med Center; cert in CBT via online modules."],
            "BOWDOIN": ["Elect med humanities; summer at Maine Med neuro unit."]
        }
    }
}

def get_spark(role: str, university: str):
    spark = CAREER_SPARKS.get(role, {})
    tips = spark.get("prep_tips", {}).get(university, ["Explore general neuro clubs!"])
    return {
        "vignette": spark.get("vignette", "Spark coming soon—add your thoughts!"),
        "prep": tips,
        "actions": [f"Reflect: Which part excites me? ({role})"]  # Auto-add to Journey
    }