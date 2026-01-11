from fastapi import FastAPI
from app.modules.avatar.routes.avatar import router as avatar_router 
from app.db.session import engine
from app.db.base import Base




app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(avatar_router)

@app.get("/")
def root():
    return {"message": "API is running"}
    