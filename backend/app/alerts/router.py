from fastapi import APIRouter, Depends, HTTPException

from app.users.schemas import CurrentUser, get_current_user
from app.alerts.service import AlertService
from app.alerts.schemas import AlertCreate, AlertResponse
from app.core.uow import IUnitOfWork
from app.core.dependencies import get_uow

router = APIRouter(tags=["alerts"])

@router.get("/alerts", response_model=list[AlertResponse])
async def get_alerts(uow: IUnitOfWork = Depends(get_uow)):
    # Placeholder implementation - replace with actual logic to fetch alerts for the user  
    async with uow:
      alerts = await AlertService.get_alerts(uow)
      return alerts

@router.get("/alerts/{alert_id}", response_model=AlertResponse)
async def get_alert_by_id(alert_id: int, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
       alert = await AlertService.get_alert_by_id(alert_id, uow)
       return alert    

@router.post("/alerts", response_model=AlertResponse)
async def create_alert(alert: AlertCreate, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        new_alert = await AlertService.create_alert(alert, uow)
        return new_alert    

@router.put("/alerts/{alert_id}", response_model=AlertResponse)
async def update_alert(alert_id: int, alert_data: AlertCreate, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        updated_alert = await AlertService.update_alert(alert_id, alert_data.dict(exclude_unset=True), uow)
        if not updated_alert:
            raise HTTPException(status_code=404, detail="Alert not found")
        return updated_alert

@router.delete("/alerts/{alert_id}")
async def delete_alert(alert_id: int, uow: IUnitOfWork = Depends(get_uow)):
    async with uow:
        success = await AlertService.delete_alert(alert_id, uow)
        if not success:
            raise HTTPException(status_code=404, detail="Alert not found")
        return {"success": success}
