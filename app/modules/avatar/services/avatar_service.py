from sqlalchemy.orm import Session
from app.modules.avatar.models.avatar import Avatar
from app.modules.avatar.schemas.avatar import AvatarCreate, AvatarUpdate





def get_all_avatars(db: Session):
    return db.query(Avatar).all()


def get_avatar_by_id(db: Session, avatar_id: int):
    return db.query(Avatar).filter(Avatar.id == avatar_id).first()


def create_avatar(db: Session, avatar_data:AvatarCreate):
   avatar = Avatar(
    name=avatar_data.name,
    role=avatar_data.role,
    tone=avatar_data.tone
   )
   db.add(avatar)
   db.commit()
   db.refresh(avatar)
   return avatar


def update_avatar(db: Session, avatar_id: int, avatar_data: AvatarUpdate):
    avatar = get_avatar_by_id(db, avatar_id)
    if not avatar:
        return None

    if avatar_data.name is not None:
        avatar.name = avatar_data.name
    if avatar_data.role is not None:
        avatar.role = avatar_data.role
    if avatar_data.tone is not None:
        avatar.tone = avatar_data.tone

    db.commit()
    db.refresh(avatar)
    return avatar


def delete_avatar(db: Session,avatar_id: int):
    avatar = get_avatar_by_id(db, avatar_id)
    if not avatar:
        return None

    db.delete(avatar)
    db.commit()
    return True
