from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession

from datetime import datetime

from app.alerts.models import Alert
# from app.alerts.models import  Severity

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AlertRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_alerts(self):
        result = await self.session.execute(select(Alert))
        alerts = result.scalars().all()
        logger.info(f"Retrieved {len(alerts)} alerts from the database")
        
        return alerts

    async def get_alert_by_id(self, alert_id: int):
        result = await self.session.execute(select(Alert).where(Alert.id == alert_id))
        logger.info(f"Retrieving alert with ID: {alert_id}")
        logger.debug(f"Debug Alert query result: {result}")
        return result.scalar()  
    
    async def create_alert(self, alert_data) -> Alert:
        new_alert = Alert(
            title=alert_data.title,
            description=alert_data.description,
            severity=alert_data.severity,
            source=alert_data.source,
            category=alert_data.category or "general",
            # created_at=datetime.now(),
            # updated_at=datetime.now(),
        )
        self.session.add(new_alert)
        await self.session.commit()
        await self.session.refresh(new_alert)
        return new_alert    
    
    async def update_alert(self, alert_id: int, update_data: dict) -> Alert:
        result = await self.session.execute(select(Alert).where(Alert.id == alert_id))
        alert = result.scalar()
        if not alert:
            return None
         
        for key, value in update_data.items():
            setattr(alert, key, value)
        
        alert.updated_at = datetime.now()
        
        self.session.add(alert)
        await self.session.commit()
        await self.session.refresh(alert)
        return alert
    
    async def delete_alert(self, alert_id: int) -> bool:
        result = await self.session.execute(select(Alert).where(Alert.id == alert_id))
        alert = result.scalar()
        if not alert:
            return False
        
        await self.session.delete(alert)
        await self.session.commit()
        return True