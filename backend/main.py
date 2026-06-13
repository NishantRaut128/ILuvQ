from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from upload import router as upload_router
from extract import router as extract_router
from session_routes import router as session_router


import models
from database import Base, engine, get_db
from auth import (
    hash_password,
    verify_password,
    create_access_token
)
from schemas import SignupSchema, LoginSchema

app = FastAPI(title="ILuvQ API")

Base.metadata.create_all(bind=engine)

app.include_router(upload_router)
app.include_router(extract_router)
app.include_router(session_router)


@app.get("/")
def root():
    return {
        "message": "ILuvQ backend is live!"
    }


@app.post("/auth/signup")
def signup(
    data: SignupSchema,
    db: Session = Depends(get_db)
):
    existing = (
        db.query(models.User)
        .filter(models.User.email == data.email)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user = models.User(
        name=data.name,
        email=data.email,
        hashed_password=hash_password(
            data.password
        )
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(
        {"sub": str(user.id)}
    )

    return {
        "token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }


@app.post("/auth/login")
def login(
    data: LoginSchema,
    db: Session = Depends(get_db)
):
    user = (
        db.query(models.User)
        .filter(models.User.email == data.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": str(user.id)}
    )

    return {
        "token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }