from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class SubmitSchema(BaseModel):
    answers: dict


@router.get("/session/{session_id}")
def get_session(session_id: int):

    return {
        "session_id": session_id,
        "questions": [
            {
                "id": 1,
                "type": "mcq",
                "question": "What is Python?",
                "options": [
                    "Programming Language",
                    "Snake",
                    "Operating System",
                    "Browser"
                ],
                "correct_index": 0,
                "ai_answer": "Python is a programming language."
            }
        ]
    }


@router.post("/session/{session_id}/submit")
def submit_test(
    session_id: int,
    data: SubmitSchema
):

    return {
        "score": 1,
        "total": 1,
        "percentage": 100,
        "results": [
            {
                "question_id": 1,
                "is_correct": True
            }
        ]
    }