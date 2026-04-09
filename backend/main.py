from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from .routers import user_router, post_router
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://dn:lybomyr1985@localhost:5432/dn_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],        
)


@app.get("/")
def read_root():
    return {"Hello": "World"}