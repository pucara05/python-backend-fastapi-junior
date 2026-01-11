from app.modules.avatar.schemas.avatar import AvatarCreate, AvatarUpdate
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.modules.avatar.services import avatar_service


router = APIRouter (
    prefix="/avatars",
    tags=["avatars"]
)

@router.get("/")
def get_avatars(db: Session = Depends(get_db)):

    return avatar_service.get_all_avatars(db)


@router.get("/{avatar_id}")
def get_avatar(avatar_id: int, db: Session = Depends(get_db)):

    avatar = avatar_service.get_avatar_by_id(db, avatar_id)
    if not avatar:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avatar not found")

    return avatar


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_avatar(avatar: AvatarCreate, db: Session = Depends(get_db)):
    return avatar_service.create_avatar(db, avatar)


@router.put("/{avatar_id}")
def update_avatar(avatar_id: int, avatar: AvatarUpdate, db: Session = Depends(get_db)):

    updated = avatar_service.update_avatar(db, avatar_id, avatar)

    if not updated:

        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Avatar not found")

    return updated


@router.delete("/{avatar_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_avatar(avatar_id: int, db: Session = Depends(get_db)):

    deleted = avatar_service.delete_avatar(db, avatar_id)

    if not deleted:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avatar not found")

        return deleted
