from fastapi import APIRouter, HTTPException

router = APIRouter (
    prefix="/avatars",
    tags=["avatars"]
)

@router.get("/")
def get_avatars():
    return {"message": "avatar list endpoint  (not implemented yet)"}

@router.get("/{avatar_id}")
def get_avatar(avatar_id: int):
    return {"message": f"get avatar {avatar_id} (not implemented yet)"}


@router.post("/")
def create_avatar():
    return {"message": "Create avatar (not implemented yet)"}

@router.put("/{avatar_id}")
def update_avatar(avatar_id: int):
    return {"message": f"update avatar {avatar_id} "}

@router.delete("/{avatar_id}")
def delete_avatar(avatar_id: int):
     return {"message": f"Delete avatar {avatar_id} (not implemented yet)"}
