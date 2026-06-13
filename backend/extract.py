from fastapi import APIRouter
from pydantic import BaseModel

from claude_service import extract_questions

router = APIRouter()


class ExtractChunkSchema(BaseModel):
    text: str
    session_id: int


@router.post("/extract/chunk")
def extract_chunk(data: ExtractChunkSchema):

    questions = extract_questions(
        data.text
    )

    return {
        "questions": questions,
        "count": len(questions)
    }