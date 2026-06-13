ILuvQ 

AI-Powered PDF Question Extraction and Test Platform

Overview

ILuvQ is a web application that converts PDF documents into interactive practice tests. Users can upload PDF files, extract questions, review answers, and attempt tests through a clean and user-friendly interface.

The project consists of a FastAPI backend and a modern HTML/CSS/JavaScript frontend.


Features

 Authentication

* User Signup
* User Login
* JWT Token Generation
* Secure Password Hashing using bcrypt

 PDF Processing

* Upload PDF files
* Automatic page counting
* Page limit validation
* PDF chunking for large documents

 Question Extraction

* AI Extraction Workflow
* MCQ and Paragraph Question Support
* Answer Explanations
* Structured Question Format

 Test System

* Practice Mode
* Test Mode
* Automatic Score Calculation
* Result Analysis

 Backend

* FastAPI REST API
* SQLAlchemy ORM
* SQLite Database
* Modular Architecture

Tech Stack

 Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* pdfplumber

 Frontend

* HTML5
* CSS3
* JavaScript

 Tools

* Git
* GitHub
* Postman

 Project Structure

ILuvQ/

-- frontend/

    -> index.html
    
    -> extraction.html
   
    -> review.html
   
    -> practice.html
   
    -> test.html
   
    -> results.html
   
    -> auth.html
  
    -> 404.html


-- backend/
  
    -> main.py
    
    -> auth.py
    
    -> database.py
    
    -> models.py
    
    -> upload.py
    
    -> extract.py
    
    -> session_routes.py
    
    -> schemas.py
    
    -> requirements.txt
    
    -> iluvq.db


--README.md


API Endpoints

 Authentication

    POST /auth/signup
    POST /auth/login
 
 PDF Processing

    POST /upload
    POST /extract/chunk

 Sessions

    GET  /session/{id}
    POST /session/{id}/submit


 Installation

 Clone Repository
    
    git clone https://github.com/NishantRaut128/ILuvQ.git
    cd ILuvQ

Create Virtual Environment

    cd backend
    python -m venv venv


Activate Environment

    Windows:
      venv\Scripts\activate

Install Dependencies

    pip install -r requirements.txt

Run Application

    uvicorn main:app --reload

Open Swagger Docs
    http://127.0.0.1:8000/docs


## Future Improvements

* Anthropic Claude API Integration
* PostgreSQL Support
* Railway Deployment
* Advanced Analytics Dashboard
* AI-Based Answer Validation
* User Progress Tracking
* Cloud File Storage

## Learning Outcomes

This project helped me gain hands-on experience with:

* REST API Development
* FastAPI Framework
* Authentication & Authorization
* SQLAlchemy ORM
* Database Design
* File Upload Handling
* Git & GitHub Workflow
* Backend Architecture

## Author

Nishant Raut

GitHub: https://github.com/NishantRaut128
