from typing import List, Dict
from app.modules.avatar.schemas.avatar import AvatarCreate, AvatarUpdate


# Simulación de almacenamiento (temporal)
avatars_db: List[dict] = []


def get_all_avatars():
    return avatars_db


def get_avatar_by_id(avatar_id: int):
    for avatar in avatars_db:
        if avatar["id"] == avatar_id:
            return avatar

            return None

def create_avatar(data:AvatarCreate):
    new_avatar = {
        "id": len(avatars_db) + 1,
        "name": data.name,
        "role": data.role,
        "tone": data.tone,
    }
    avatars_db.append(new_avatar)
    return new_avatar


def update_avatar(avatar_id: int, data: AvatarUpdate):
    for avatar in avatars_db:
        if avatar["id"] == avatar_id:
            if data.name is not None:
                avatar["name"] = data.name
            if data.role is not None:
                avatar["role"] = data.role
            if data.tone is not None:
                avatar["tone"] = data.tone
            return avatar
    return None

def delete_avatar(avatar_id: int):
    for index, avatar in enumerate(avatars_db):
        if avatar["id"] == avatar_id:
            return avatars_db.pop(index)
    return None
