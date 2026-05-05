from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession

from app.incidents.schemas import IncidentCreate, IncidentResponse, IncidentReviewCreateUpdate, IncidentDecisionCreate
from app.incidents.models import Incident, IncidentReview, IncidentDecision, Status
from datetime import datetime

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class IncidentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        logger.debug("IncidentRepository initialized")  
        
    async def get_incidents(self):
        logger.info("Executing get_incidents query")
        result = await self.session.execute(select(Incident))
        incidents = result.scalars().all()

        return incidents
    
    async def get_incident_by_id(self, incident_id: int):
        result = await self.session.execute(select(Incident).where(Incident.id == incident_id))
        logger.info(f"Retrieving incident with ID: {incident_id}")
        return result.scalar()    
        

    async def create_incident(self, incident: IncidentCreate) -> IncidentResponse:
        new_incident = Incident(
            title=incident.title,
            description=incident.description,
            severity=incident.severity,
            status="open",
            source=incident.source or "manual",
            # analysis=incident.analysis if hasattr(incident, "analysis") else None,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self.session.add(new_incident)
        await self.session.commit()
        await self.session.refresh(new_incident)
        return new_incident
    
    async def update_incident(self, incident_id: int, update_data: dict) -> IncidentResponse:
        result = await self.session.execute(select(Incident).where(Incident.id == incident_id))
        incident = result.scalar()
        if not incident:
            return None
         
        for key, value in update_data.items():
            setattr(incident, key, value)
        
        incident.updated_at = datetime.now()
        
        self.session.add(incident)
        await self.session.commit()
        await self.session.refresh(incident)
        return incident
    
    async def delete_incident(self, incident_id: int) -> bool:
        result = await self.session.execute(select(Incident).where(Incident.id == incident_id))
        incident = result.scalar()
        if not incident:
            return False
        
        await self.session.delete(incident)
        await self.session.commit()
        return True
    #  REVIEW RELATED METHODS
    async def create_reviews(self, incident_id: int, user_id: int, review: IncidentReviewCreateUpdate) -> IncidentResponse:
        result = await self.session.execute(select(Incident).where(Incident.id == incident_id))
        incident = result.scalar()
        if not incident:
            return None
        
        logger.debug(f"PRINT !!!! Review data: {type(review)}, {review}")  # Додайте цей рядок для виведення типу та вмісту review
        new_review = IncidentReview(
            incident_id=incident_id,
            user_id=user_id,
            what_happened=review.what_happened,
            what_went_wrong=review.what_went_wrong,
            analysis=review.analysis,
            recommendations=review.recommendations,
        )    
        
        self.session.add(new_review)
        await self.session.commit()
        await self.session.refresh(new_review)
        return new_review 
    
    async def get_reviews(self, incident_id: int):
        result = await self.session.execute(select(IncidentReview).where(IncidentReview.incident_id == incident_id))
        reviews = result.scalars().all()
        return reviews
    
    async def update_review(self, review_id: int, update_data: dict):
        result = await self.session.execute(select(IncidentReview).where(IncidentReview.id == review_id))
        review = result.scalar()
        if not review:
            return None
        
        for key, value in update_data.items():
            setattr(review, key, value)
        
        review.updated_at = datetime.now().isoformat()
        
        self.session.add(review)
        await self.session.commit()
        await self.session.refresh(review)
        return review   
    # DECISION RELATED METHODS
    async def create_decision(self, incident_id: int, user_id: int, decision: IncidentDecisionCreate) -> IncidentResponse:
        result = await self.session.execute(select(Incident).where(Incident.id == incident_id))
        incident = result.scalar()
        if not incident:
            return None
        
        # Create and add decision to the database (not implemented here)
        new_decision = IncidentDecision(
            incident_id=incident_id,
            user_id=user_id,
            selected_action=decision.selected_action,
            rationale=decision.rationale,
            expected_outcome=decision.expected_outcome,
        )    
        
        self.session.add(new_decision)

        # Ось тут змінюємо incident
        incident.status = Status.RESOLVED.value
        incident.resolved_at = datetime.now()
        incident.updated_at = datetime.now()

        await self.session.commit()
        await self.session.refresh(new_decision)

        return new_decision
    
    async def get_decision_by_id(self, decision_id: int):
        result = await self.session.execute(select(IncidentDecision).where(IncidentDecision.id == decision_id))
        decision = result.scalar()
        return decision 