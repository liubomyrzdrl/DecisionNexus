from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

# IncidentStatus = Literal["open", "in_review", "resolved", "archived"]
# SeverityLevel = Literal["low", "medium", "high", "critical"]



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
    
# class SEVERITY(Enum):
#     LOW = "low"
#     MEDIUM = "medium"
#     HIGH = "high"
    # CRITICAL = "critical"

AlertStatus = Literal["new", "in_progress", "resolved", "closed"]
AlertSource = Literal["manual", "monitoring", "ai_detected", "logs", "external", "integration"]
AlertSeverity = Literal["low", "medium", "high", "critical"]    
    
    

class Alert(BaseModel):
    title: str
    description: Optional[str] = None
    severity: Optional[AlertSeverity] = "low"
    source: Optional[AlertSource] = "manual"
    status: Optional[AlertStatus] = "new"
    signal_data: Optional[dict] = None
    ai_summary: Optional[str] = None
    ai_confidence: Optional[float] = None
    
    
class AlertCreate(Alert):
    title: str
    description: str
    severity: Optional[AlertSeverity] = "low"
    source: Optional[AlertSource] = "manual"  
    category: Optional[str] = None 
    
class AlertResponse(Alert):
    id: int
    status: Optional[AlertStatus] = "new"
    title: str
    description: Optional[str] = None
    severity: Optional[AlertSeverity] = "low"
    source: Optional[AlertSource] = "manual"   
    signal_data: Optional[dict] = None
    ai_summary: Optional[str] = None
    ai_confidence: Optional[float] = None     
    created_at: datetime
    updated_at: datetime
    
    
# class IncidentCreate(BaseModel):
#     title: str
#     description: Optional[str] = None
#     severity: SeverityLevel = "medium"
#     source: Optional[str] = "manual"

# class IncidentResponse(BaseModel):
#     id: str
#     title: str
#     description: Optional[str]
#     status: IncidentStatus
#     severity: SeverityLevel
#     source: Optional[str]
#     created_at: datetime
#     updated_at: datetime