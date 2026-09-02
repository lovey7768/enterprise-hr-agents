from typing import List
from ..schemas import ScreeningResult, InterviewQuestion

def generate_interview_questions(screen: ScreeningResult, n: int = 8) -> List[InterviewQuestion]:
    """
    Generate basic technical and behavioral questions based on screening.
    Replace with targeted LLM prompts / LangGraph agent chain.
    """
    questions: List[InterviewQuestion] = []
    for skill in screen.matched_skills[:n]:
        questions.append(InterviewQuestion(
            question=f"Describe a project where you used {skill}. What challenges did you face and how did you resolve them?",
            intent="technical",
            difficulty="medium",
        ))
    # Add a couple of behavioral prompts
    if len(questions) < n:
        questions.append(InterviewQuestion(question="Tell me about a time you worked in a cross-functional team.", intent="behavioral"))
    return questions
