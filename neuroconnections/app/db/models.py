from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from neuroconnections.app.db.base import Base


class Journey(Base):
    __tablename__ = "journeys"
    id = Column(Integer, primary_key=True)
    student_name = Column(String)
    university = Column(String)


    steps = relationship("ExplorationStep", back_populates="journey")


class ExplorationStep(Base):
    __tablename__ = "steps"
    id = Column(Integer, primary_key=True)
    theme = Column(String)
    reflection = Column(Text)
    journey_id = Column(Integer, ForeignKey("journeys.id"))


    journey = relationship("Journey", back_populates="steps")
    actions = relationship("ActionItem", back_populates="step")


class ActionItem(Base):
    __tablename__ = "actions"
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    completed = Column(Boolean, default=False)
    step_id = Column(Integer, ForeignKey("steps.id"))
    is_bundle = Column(Boolean, default=False)  # New field to identify bundles
    parent_bundle = Column(String, nullable=True)  # New field to link to bundle name if applicable

    step = relationship("ExplorationStep", back_populates="actions")