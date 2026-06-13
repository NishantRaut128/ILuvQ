def extract_questions(text: str):
    return [
        {
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
        },
        {
            "type": "para",
            "question": "Explain OOP.",
            "options": None,
            "correct_index": None,
            "ai_answer": "Object-Oriented Programming organizes code using objects and classes."
        }
    ]