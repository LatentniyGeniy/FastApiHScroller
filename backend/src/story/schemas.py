from pydantic import BaseModel


class StoryBase(BaseModel):
    tale: str


class StoryCreate(StoryBase):
    pass


class Story(StoryBase):
    id: int
    description: str | None = None

    class Config:
        orm_mode = True