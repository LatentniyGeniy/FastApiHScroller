from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.src.story import crud, schemas
from backend.src.database import get_db

router = APIRouter()

@router.post("/stories/", response_model=schemas.Story)
def create_story(story: schemas.StoryCreate, db: Session = Depends(get_db)):
    return crud.create_story(db=db, story=story)


@router.get("/stories/", response_model=list[schemas.Story])
def read_stories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stories = crud.get_stories(db, skip=skip, limit=limit)
    return stories


@router.get("/stories/{story_id}", response_model=schemas.Story)
def read_story(story_id: int, db: Session = Depends(get_db)):
    db_story = crud.get_story(db, story_id=story_id)
    if db_story is None:
        raise HTTPException(status_code=404, detail="story not found")
    return db_story
