from fastapi import FastAPI
from app.modules.avatar.routes.avatar import router as avatar_router 



app = FastAPI()

app.include_router(avatar_router)

@app.get("/")
def root():
    return {"message": "API is running"}
    