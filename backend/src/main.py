from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from backend.src.story import crud, models, schemas
from backend.src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/stories/", response_model=schemas.Story)
def create_story(story: schemas.StoryCreate, db: Session = Depends(get_db)):
    return crud.create_story(db=db, story=story)


@app.get("/stories/", response_model=list[schemas.Story])
def read_stories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stories = crud.get_stories(db, skip=skip, limit=limit)
    return stories


@app.get("/stories/{story_id}", response_model=schemas.Story)
def read_story(story_id: int, db: Session = Depends(get_db)):
    db_story = crud.get_story(db, story_id=story_id)
    if db_story is None:
        raise HTTPException(status_code=404, detail="story not found")
    return db_story
