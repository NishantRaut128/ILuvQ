from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
import pdfplumber
import io

import models
from database import get_db

router = APIRouter()

PAGE_LIMIT = 30


@router.post("/upload")
def upload_pdf(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    contents = file.file.read()

    try:
        with pdfplumber.open(
            io.BytesIO(contents)
        ) as pdf:
            total_pages = len(pdf.pages)

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid PDF file"
        )

    if total_pages >= PAGE_LIMIT:
        raise HTTPException(
            status_code=403,
            detail="PDF exceeds free 30-page limit"
        )

    session = models.Session(
        filename=file.filename,
        total_pages=total_pages
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    chunks = []

    with pdfplumber.open(
        io.BytesIO(contents)
    ) as pdf:

        chunk_size = 4

        for i in range(
            0,
            total_pages,
            chunk_size
        ):

            chunk_pages = pdf.pages[
                i:i + chunk_size
            ]

            text = "\n".join(
                [
                    page.extract_text() or ""
                    for page in chunk_pages
                ]
            )

            chunks.append({
                "chunk_index": len(chunks),
                "page_start": i + 1,
                "page_end": min(
                    i + chunk_size,
                    total_pages
                ),
                "text": text
            })

    return {
        "session_id": session.id,
        "filename": file.filename,
        "total_pages": total_pages,
        "total_chunks": len(chunks),
        "chunks": chunks
    }