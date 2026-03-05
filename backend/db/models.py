from sqlalchemy import Column, Integer, String, Float, DateTime
from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)


class Professional(Base):
    __tablename__ = "professionals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    career_archetype = Column(String)
    title = Column(String)
    company = Column(String)
    reputation_score = Column(Float)


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer)
    professional_id = Column(Integer)
    slot_time = Column(DateTime)

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    professional_id = Column(Integer)
    title = Column(String)
    description = Column(String)
    scheduled_time = Column(DateTime)