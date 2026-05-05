from pydantic import BaseModel, ConfigDict
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
    id: int
    title: str
    description: str | None = None
    status: str
    severity: str
    source: str | None = None
    category: str | None = None
    ai_summary: str | None = None
    ai_confidence: float | None = None
    analysis: str | None = None
    created_at: datetime
    updated_at: datetime
    resolved_at: datetime | None = None

    
    model_config = ConfigDict(from_attributes=True)
    
    
class IncidentReviewCreateUpdate(BaseModel):
    # user_id: int
    # incident_id: int
    what_happened: Optional[str] = None
    what_went_wrong: Optional[str] = None
    analysis: Optional[str] = None
    recommendations: Optional[str] = None


class IncidentReviewResponse(BaseModel):
    id: int
    user_id: int
    incident_id: int
    what_happened: Optional[str]
    what_went_wrong: Optional[str]
    analysis: Optional[str]
    recommendations: Optional[str]
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)    


class IncidentDecisionCreate(BaseModel):
    user_id: int
    incident_id: int
    decision: str
    

# class IncidentResponse(BaseModel):
#     id: int
#     title: str
#     description: Optional[str] = None
#     status: Optional[str] = None
#     severity: Optional[str] = None
#     source: Optional[str] = None
#     analysis: Optional[str] = None
#     created_at: Optional[datetime] = None
#     updated_at: Optional[datetime] = None

#     model_config = ConfigDict(from_attributes=True)