from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, DateTime
from app.db.database import Base

class Statistics(Base):
    __tablename__ = "statistics"
    id = Column(Integer, primary_key=True, index=True)
    goal_id = Column(Integer, nullable=False)
    percent_obtained = Column(Integer, nullable=False)
    required_percent = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)