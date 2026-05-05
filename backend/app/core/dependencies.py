from app.core.uow import UnitOfWork

async def get_uow():
    return UnitOfWork()