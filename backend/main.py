from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.incidents.router import router as incidents_router
from app.health.route import router as health_router
from app.alerts.router import router as alerts_router
from fastapi.responses import JSONResponse
import traceback

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
     allow_origins=[
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_methods=["*"],
    allow_headers=["*"],        
)

# app.include_router([
#     incidents_router,
#     health_router
#     ])

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print("UNHANDLED EXCEPTION:", repr(exc))
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )

app.include_router(health_router)
app.include_router(incidents_router)
app.include_router(alerts_router)
# @app.on_event("startup")
# async def startup_event():
#     # Initialize database connection, repositories, etc.
#     db.init_db()  # Ensure database tables are created

# @app.get("/")
# def read_root(db: Session = Depends(get_db)):
#     return {"Hello": "World v2"}