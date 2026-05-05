from fastapi import APIRouter, Depends

from app.users.schemas import CurrentUser, get_current_user
from app.incidents.schemas import IncidentCreate, IncidentResponse, IncidentReviewCreateUpdate, IncidentReviewResponse
from app.incidents.service import IncidentService

from app.core.uow import IUnitOfWork
from app.core.dependencies import get_uow

router = APIRouter(tags=["incidents"])

@router.get("/incidents", response_model=list[IncidentResponse])
async def get_incidents(uow: IUnitOfWork = Depends(get_uow)):
    print("Router: Fetching incidents using UnitOfWork...")
    incidents = await IncidentService.get_incidents(uow)
    return incidents

@router.get("/incidents/{incident_id}", response_model=IncidentResponse)
async def get_incident_by_id(incident_id: int, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        incident = await IncidentService.get_incident_by_id(incident_id, uow)
        return incident

@router.post("/incident", response_model=IncidentResponse)
async def create_incident(incident: IncidentCreate, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        return await IncidentService.create_incident(incident, uow)
    
@router.patch("/incidents/{incident_id}", response_model=IncidentResponse)
async def update_incident(incident_id: int, update_data: dict, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        return await IncidentService.update_incident(incident_id, update_data, uow) 

@router.delete("/incidents/{incident_id}")
async def delete_incident(incident_id: int, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        success = await IncidentService.delete_incident(incident_id, uow)
        return {"success": success}
    
# Reviews--------------------------- 
    
@router.post("/incidents/{incident_id}/reviews", response_model=IncidentReviewResponse)
async def create_review(
    incident_id: int, 
    review_data: IncidentReviewCreateUpdate, 
    current_user: CurrentUser = Depends(get_current_user), 
    uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        return await IncidentService.create_review(incident_id, current_user.id, review_data, uow)
    
@router.get("/incidents/{incident_id}/reviews", response_model=list[IncidentReviewResponse])
async def get_reviews(incident_id: int, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        return await IncidentService.get_reviews(incident_id, uow)

@router.patch("/incidents/reviews/{review_id}", response_model=IncidentReviewResponse)
async def update_review(review_id: int, update_data: IncidentReviewCreateUpdate, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        return await IncidentService.update_review(review_id, update_data, uow)

@router.get("/incidents/decisions/{decision_id}")
async def get_decision(decision_id: int, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        return await IncidentService.get_decision_by_id(decision_id, uow)   

@router.post("/incidents/{incident_id}/decisions")
async def create_decision(incident_id: int, user_id: int, decision_data: dict, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        return await IncidentService.create_decision(incident_id, user_id, decision_data, uow)  