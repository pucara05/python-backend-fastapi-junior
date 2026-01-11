from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Avatar(Base):
    __tablename__= "avatars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    tone = Column(String, nullable=True)

    