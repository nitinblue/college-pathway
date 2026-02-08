from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from neuroconnections.app.db.session import SessionLocal
from neuroconnections.app.db.models import (
    Journey,
    ExplorationStep,
    ActionItem,
)
from neuroconnections.app.services.recommendation_service import recommend

router = APIRouter(prefix="/steps", tags=["Exploration Steps"])


# -----------------------------
# Dependency
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# Create Exploration Step
# -----------------------------
@router.post("/")
def create_step(
    journey_id: int,
    theme: str,
    reflection: str,
    db: Session = Depends(get_db),
):
    journey = db.query(Journey).get(journey_id)
    if not journey:
        raise HTTPException(status_code=404, detail="Journey not found")

    step = ExplorationStep(
        theme=theme,
        reflection=reflection,
        journey_id=journey_id,
    )
    db.add(step)
    db.flush()  # ensures step.id is available

    # Generate recommendations
    courses = recommend(theme, journey.university)

    for course in courses:
        action = ActionItem(
            description=f"Explore course: {course}",
            step_id=step.id,
        )
        db.add(action)

    db.commit()
    db.refresh(step)

    return {
        "step_id": step.id,
        "theme": step.theme,
        "reflection": step.reflection,
        "actions_created": len(step.actions),
    }


# -----------------------------
# List Steps for a Journey
# -----------------------------
@router.get("/{journey_id}")
def list_steps(
    journey_id: int,
    db: Session = Depends(get_db),
):
    journey = db.query(Journey).get(journey_id)
    if not journey:
        raise HTTPException(status_code=404, detail="Journey not found")

    steps = (
        db.query(ExplorationStep)
        .filter_by(journey_id=journey_id)
        .order_by(ExplorationStep.id.desc())
        .all()
    )

    return [
        {
            "id": step.id,
            "theme": step.theme,
            "reflection": step.reflection,
            "actions": [
                {
                    "id": action.id,
                    "description": action.description,
                    "completed": action.completed,
                    "is_bundle": getattr(action, 'is_bundle', False)  # Handle potential missing attribute
                    "parent_bundle": getattr(action, 'parent_bundle', None)  # Handle potential missing attribute
                }
                for action in step.actions
            ],
        }
        for step in steps
    ]
