from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

from app.core.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String(1000), nullable=True)

    severity: Mapped[str] = mapped_column(String(20), nullable=False, default="low")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="new")
    source: Mapped[str] = mapped_column(String(50), nullable=False, default="manual")

    category: Mapped[str | None] = mapped_column(String(100), nullable=True)

    signal_data: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    ai_summary: Mapped[str | None] = mapped_column(String(2000), nullable=True)
    ai_confidence: Mapped[float | None] = mapped_column(nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

# from datetime import datetime
# from enum import Enum
# from sqlalchemy import DateTime, func

# from sqlalchemy import String
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy.dialects.postgresql import JSONB

# from sqlalchemy import Enum as SQLAlchemyEnum

# from app.core.database import Base

# class Status(Enum):
#     NEW = "new"
#     IN_PROGRESS = "in_progress"
#     RESOLVED = "resolved"
#     CLOSED = "closed"

# class Source (Enum):
#     MANUAL = "manual"
#     MONITORING = "monitoring"
#     AI_DETECTED = "ai_detected"
#     LOGS = "logs"
#     EXTERNAL = "external"
#     INTEGRATION = "integration"
    
# class Severity(Enum):
#     LOW = "low"
#     MEDIUM = "medium"
#     HIGH = "high"
#     CRITICAL = "critical"
    
# class Alert (Base):
#     __tablename__ = "alerts"
    
#     id: Mapped[int] = mapped_column(primary_key=True, index=True)
#     title: Mapped[str] = mapped_column(String(255), nullable=False)
#     description: Mapped[str] = mapped_column(String(1000), nullable=True)
#     severity: Mapped[Severity] = mapped_column(
#         SQLAlchemyEnum(Severity, name="severity", native_enum=True), 
#         default=Severity.LOW
#     )
#     status: Mapped[Status] = mapped_column(
#         SQLAlchemyEnum(Status, name="status", native_enum=True), 
#         default=Status.NEW
#     )
#     source: Mapped[Source] = mapped_column(
#         SQLAlchemyEnum(Source, name="source", native_enum=True), 
#         default=Source.MANUAL
#     )
#     signal_data: Mapped[dict] = mapped_column(JSONB, nullable=True)
#     category: Mapped[str | None] = mapped_column(String(100), nullable=True)
#     ai_summary: Mapped[str | None] = mapped_column(String(2000), nullable=True)
#     ai_confidence: Mapped[float | None] = mapped_column(nullable=True)
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now())   
#     updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), onupdate=func.now())