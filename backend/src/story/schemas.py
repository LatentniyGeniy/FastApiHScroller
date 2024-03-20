from pydantic import BaseModel


class StoryBase(BaseModel):
    tale: str
    description: str | None = None

class StoryCreate(StoryBase):
    pass


class Story(StoryBase):
    id: int
    

    class Config:
        orm_mode = True