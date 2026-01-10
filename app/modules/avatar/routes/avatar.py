from app.modules.avatar.schemas.avatar import AvatarCreate, AvatarUpdate
from fastapi import APIRouter, HTTPException
from app.modules.avatar.services import avatar_service

router = APIRouter (
    prefix="/avatars",
    tags=["avatars"]
)

@router.get("/")
def get_avatars():
    return avatar_service.get_all_avatars()

@router.get("/{avatar_id}")
def get_avatar(avatar_id: int):
    avatar = avatar_service.get_avatar_by_id(avatar_id)
    if not avatar:
        raise HTTPException(status_code=404, detail="Avatar not found")
    return avatar


@router.post("/")
def create_avatar(avatar: AvatarCreate):
    return avatar_service.create_avatar(avatar)


@router.put("/{avatar_id}")
def update_avatar(avatar_id: int, avatar: AvatarUpdate):
    updated = avatar_service.update_avatar(avatar_id, avatar)
    if not updated:
        raise HTTPException(status_code=404, detail="Avatar not found")
    return updated


@router.delete("/{avatar_id}")
def delete_avatar(avatar_id: int):
    deleted = avatar_service.delete_avatar(avatar_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Avatar not found")
        return deleted
