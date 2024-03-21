from fastapi import FastAPI

from backend.src.story import models
from backend.src.database import engine
from backend.src.story import routes as story_routes


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(story_routes.router, prefix="/stories", tags=["stories"])



