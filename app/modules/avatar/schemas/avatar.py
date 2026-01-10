from pydantic import BaseModel
from typing import Optional

class AvatarBase(BaseModel):
    name: str
    role: str
    tone: str

class AvatarCreate(AvatarBase):
    pass

class AvatarUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    tone: Optional[str] = None

    class AvatarResponse(AvatarBase):
        id: int

        