from sqlalchemy import Column, Integer, String, Text, Boolean, JSON
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    total_pages = Column(Integer)
    total_questions = Column(Integer, default=0)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(Integer)

    type = Column(String)

    question_text = Column(Text)

    options = Column(JSON)

    correct_index = Column(Integer)

    ai_answer = Column(Text)

    order_index = Column(Integer)


class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(Integer)

    question_id = Column(Integer)

    user_answer = Column(String)

    is_correct = Column(Boolean)