import uuid
from sqlalchemy import Column, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from db import Base

class Run(Base):
    __tablename__ = "runs"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    mode = Column(String(50), nullable=False, default="Summarise")

    # Stored input can be blank in no_store mode
    input_text = Column(Text, nullable=False, default="")

    status = Column(String(20), nullable=False, default="queued")  # queued|running|done|failed
    result = Column(Text, nullable=True)
    error = Column(Text, nullable=True)

    # Privacy controls
    no_store = Column(Boolean, nullable=False, default=False)
    pii_detected = Column(Boolean, nullable=False, default=False)
    pii_summary = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
