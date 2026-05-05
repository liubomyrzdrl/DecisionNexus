from select import select

from app.alerts.models import Alert
from  app.core.uow import IUnitOfWork
from app.alerts.repository import AlertRepository


class AlertService:
    @staticmethod
    async def get_alerts(uow: IUnitOfWork) -> list[Alert]:
        async with uow:
            return await uow.alerts.get_alerts()
        
    @staticmethod
    async def get_alert_by_id(alert_id: int, uow: IUnitOfWork) -> Alert:
        async with uow:
            return await uow.alerts.get_alert_by_id(alert_id)
        
    @staticmethod
    async def create_alert(alert_data, uow: IUnitOfWork) -> Alert:
        async with uow:
            return await uow.alerts.create_alert(alert_data)
    
    @staticmethod
    async def update_alert(alert_id: int, update_data: dict, uow: IUnitOfWork) -> Alert:
        async with uow:
            return await uow.alerts.update_alert(alert_id, update_data)
            
    @staticmethod
    async def delete_alert(alert_id: int, uow: IUnitOfWork) -> bool:
        async with uow:
            return await uow.alerts.delete_alert(alert_id)