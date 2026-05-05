from abc import ABC, abstractmethod
from app.incidents.repository import IncidentRepository
from app.core.database import AsyncSessionLocal
from app.alerts.repository import AlertRepository


class IUnitOfWork(ABC):
    incidents: IncidentRepository
    alerts: AlertRepository

    @abstractmethod
    async def __aenter__(self): ...
    
    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = AsyncSessionLocal

    async def __aenter__(self):
        self.session = self.session_factory()
        self.incidents = IncidentRepository(self.session)
        self.alerts = AlertRepository(self.session)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()