from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # One user can have one donor profile
    donor = relationship("Donor", back_populates="user", uselist=False)


class Donor(Base):
    __tablename__ = "donors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    blood_type = Column(String, nullable=False)   # e.g. "O+", "AB-"
    city = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    last_donated = Column(Date, nullable=True)
    is_available = Column(Boolean, default=True)

    user = relationship("User", back_populates="donor")


class BloodRequest(Base):
    __tablename__ = "blood_requests"

    id = Column(Integer, primary_key=True, index=True)
    hospital_name = Column(String, nullable=False)
    blood_type = Column(String, nullable=False)   # e.g. "B+", "AB-"
    city = Column(String, nullable=False)
    units_needed = Column(Integer, nullable=False)
    urgency = Column(String, default="normal")    # "normal" | "high" | "critical"
    status = Column(String, default="open")       # "open" | "fulfilled" | "cancelled"