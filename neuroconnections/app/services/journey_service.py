from sqlalchemy.orm import Session

from neuroconnections.app.db.models import (
    Journey,
    ExplorationStep,
    ActionItem,
)
from neuroconnections.app.services.recommendation_service import recommend


def create_journey(
    db: Session,
    student_name: str,
    university: str,
) -> Journey:
    journey = Journey(
        student_name=student_name,
        university=university,
    )
    db.add(journey)
    db.commit()
    db.refresh(journey)
    return journey


def add_exploration_step(
    db: Session,
    journey_id: int,
    theme: str,
    reflection: str, mode: str = "single"
) -> ExplorationStep:
    journey = db.query(Journey).get(journey_id)
    if not journey:
        raise ValueError("Journey not found")

    step = ExplorationStep(
        theme=theme,
        reflection=reflection,
        journey_id=journey_id,
    )
    db.add(step)
    db.flush()

    recommendations = recommend(theme, journey.university, mode=mode)
    
    if mode == "combinations":
        for bundle in recommendations:
            # Add bundle overview as an ActionItem
            db.add(
                ActionItem(
                    description=f"**Explore Bundle: {bundle['name']}** - {bundle['rationale']}\nWhat Next? {bundle['careers']}",
                    step_id=step.id,
                    is_bundle=True  # Flag for UI (add to model if needed)
                )
            )
            # Add individual courses
            for course in bundle['courses']:
                db.add(
                    ActionItem(
                        description=f"• {course}",
                        step_id=step.id,
                        parent_bundle=bundle['name']  # For grouping in UI
                    )
                )
    else:
        # Existing single-course logic
        for course in recommendations:
            db.add(
                ActionItem(
                    description=f"Explore course: {course}",
                    step_id=step.id
                )
            )

    db.commit()
    db.refresh(step)
    return step


def get_journey_steps(
    db: Session,
    journey_id: int,
):
    return (
        db.query(ExplorationStep)
        .filter_by(journey_id=journey_id)
        .order_by(ExplorationStep.id.desc())
        .all()
    )
