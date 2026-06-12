from fastapi import FastAPI

from database import Base, engine
import models

app = FastAPI(title="ILuvQ API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "ILuvQ backend is live!"
    }