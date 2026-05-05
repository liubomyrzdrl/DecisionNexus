from datetime import datetime
from enum import Enum
from sqlalchemy import DateTime, func

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Status(Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"
    
class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    
# type SourceType =
#   | "manual"        // створив користувач
#   | "alert"         // з monitoring system
#   | "ai_detected"   // AI знайшов anomaly
#   | "log"           // з логів
#   | "external"      // клієнт / користувач повідомив
#   | "integration"   // з іншого сервісу (Slack, PagerDuty)
class SourceType(Enum):
    MANUAL = "manual"
    ALERT = "alert"
    AI_DETECTED = "ai_detected"
    LOG = "log"
    EXTERNAL = "external"
    INTEGRATION = "integration"

class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=True)
    
    severity: Mapped[Severity] = mapped_column(String(20), nullable=False, default=Severity.LOW.value)
    status: Mapped[Status] = mapped_column(String(20), nullable=False, default=Status.OPEN.value)
    
    source: Mapped[SourceType] = mapped_column(String(50), nullable=True, default=SourceType.MANUAL.value)
    
    category: Mapped[str | None] = mapped_column(String(100), nullable=True)
    ai_summary: Mapped[str | None] = mapped_column(String(2000), nullable=True)
    ai_confidence: Mapped[float | None] = mapped_column(nullable=True)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())    
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    resolved_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    # started_at  : Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    # team_id: Mapped[int] = mapped_column(nullable=True)
    # assigned_to: Mapped[int] = mapped_column(nullable=True)
    
    
class IncidentReview(Base):
    __tablename__ = "incident_reviews"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    incident_id: Mapped[int] = mapped_column(nullable=False)  # Foreign key to Incident.id
    user_id: Mapped[int] = mapped_column(nullable=False)  # Foreign key to User.id
    what_happened: Mapped[str] = mapped_column(String(1000), nullable=True)
    what_went_wrong: Mapped[str] = mapped_column(String(1000), nullable=True)
    analysis: Mapped[str] = mapped_column(String(1000), nullable=True)
    recommendations: Mapped[str] = mapped_column(String(1000), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
        
    
class SelectedAction(Enum):
    ROLLBACK = "rollback"   
    RESTART = "restart"
    INVESTIGATE = "investigate"
    IGNORE = "ignore"
    SCALE_UP = "scale_up"    
    
    
class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

    
class  IncidentDecision(Base):
    __tablename__ = "incident_decisions"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    incident_id: Mapped[int] = mapped_column(nullable=False)  # Foreign key to Incident.id
    selected_action: Mapped[SelectedAction] = mapped_column(String(20), nullable=False)
    rationale: Mapped[str] = mapped_column(String(1000), nullable=True)
    expected_outcome: Mapped[str] = mapped_column(String(1000), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())