from sqlalchemy.orm import Session

from backend.src.story import models, schemas


def get_story(db: Session, story_id: int):
    return db.query(models.Story).filter(models.Story.id == story_id).first()


def get_stories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Story).offset(skip).limit(limit).all()


def create_story(db: Session, story: schemas.StoryCreate):
    db_story = models.Story(description=story.description, tale=story.tale)
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story
