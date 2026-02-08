from neuroconnections.app.seed.course_catalog import COURSE_CATALOG


def recommend(theme: str, university: str, mode: str = "single"):  # New: mode param
    catalog = COURSE_CATALOG.get(university, {})
    
    if mode == "combinations":
        # Return all bundles for exploration
        return catalog.get("bundles", [])
    
    # Backward-compatible single recommendations
    if theme == "Curiosity":
        return catalog.get("neuroscience_core", [])[:1]
    if theme == "Skill":
        return catalog.get("computational", [])[:1]
    if theme == "Ethics":
        return catalog.get("ethics", [])[:1]
    if theme == "Low Load":
        return catalog.get("low_load", [])[:1]
    
    return []