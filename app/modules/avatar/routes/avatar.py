from fastapi import APIRouter

router = APIRouter (
    prefix="/avatars",
    tags=["avatars"]
)

@router.get("/")
def get_avatars():
    return {"message": "avatar list endpoint"}