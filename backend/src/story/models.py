from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.src.database import Base


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True)
    description = Column(String, index=True)
    tale = Column(String, unique=False, index=True)
    

    