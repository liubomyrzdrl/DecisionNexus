from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

IncidentStatus = Literal["open", "in_review", "resolved", "archived"]
SeverityLevel = Literal["low", "medium", "high", "critical"]

class IncidentCreate(BaseModel):
    title: str
    description: Optional[str] = None
    severity: SeverityLevel = "medium"
    source: Optional[str] = "manual"

class IncidentResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: IncidentStatus
    severity: SeverityLevel
    source: Optional[str]
    created_at: datetime
    updated_at: datetime