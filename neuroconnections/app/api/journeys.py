from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from neuroconnections.app.db.session import SessionLocal
from neuroconnections.app.db.models import Journey

router = APIRouter(prefix="/journeys", tags=["Journeys"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_journey(
    student_name: str,
    university: str,
    db: Session = Depends(get_db)
):
    if not student_name:
        raise HTTPException(status_code=400, detail="Student name required")

    journey = Journey(
        student_name=student_name,
        university=university
    )
    db.add(journey)
    db.commit()
    db.refresh(journey)

    return {
        "id": journey.id,
        "student_name": journey.student_name,
        "university": journey.university
    }


@router.get("/")
def list_journeys(db: Session = Depends(get_db)):
    journeys = db.query(Journey).all()
    return [
        {
            "id": j.id,
            "student_name": j.student_name,
            "university": j.university
        }
        for j in journeys
    ]
