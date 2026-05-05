from app.core.uow import IUnitOfWork
from app.incidents.models import Incident
from app.incidents.repository import IncidentRepository


class IncidentService:
    @staticmethod
    async def get_incidents(uow: IUnitOfWork) -> list[Incident]:
        print("Service: Fetching incidents using UnitOfWork...")
        async with uow:
            return await uow.incidents.get_incidents()
        
    @staticmethod
    async def get_incident_by_id(incident_id: int, uow: IUnitOfWork) -> Incident:
        async with uow:
            return await uow.incidents.get_incident_by_id(incident_id)
        
    @staticmethod
    async def create_incident(incident_data, uow: IUnitOfWork) -> Incident:
        async with uow:
            return await uow.incidents.create_incident(incident_data)
    
    @staticmethod
    async def update_incident(incident_id: int, update_data: dict, uow: IUnitOfWork) -> Incident:
        async with uow:
            return await uow.incidents.update_incident(incident_id, update_data)
            
    @staticmethod
    async def delete_incident(incident_id: int, uow: IUnitOfWork) -> bool:
        async with uow:
            return await uow.incidents.delete_incident(incident_id)

    @staticmethod
    async def create_review(incident_id: int, user_id: int, review_data: dict, uow: IUnitOfWork):
        async with uow:
            return await uow.incidents.create_reviews(incident_id, user_id, review_data)    
    
    @staticmethod
    async def get_reviews(incident_id: int, uow: IUnitOfWork):
        async with uow:
            return await uow.incidents.get_reviews(incident_id)       
        
    @staticmethod
    async def update_review(review_id: int, update_data: dict, uow: IUnitOfWork):
        async with uow:
            return await uow.incidents.update_review(review_id, update_data)

    @staticmethod
    async def get_decision_by_id(decision_id: int, uow: IUnitOfWork):
        async with uow:
            return await uow.incidents.get_decision_by_id(decision_id)
        
    @staticmethod   
    async def create_decision(incident_id: int, user_id: int, decision_data: dict, uow: IUnitOfWork):
        async with uow:
            return await uow.incidents.create_decision(incident_id, user_id, decision_data)
        
    # def __init__(self, repository):
    #     self.repository = repository

    # async def create_incident(self, incident_data):
    #     return await self.repository.create_incident(incident_data)