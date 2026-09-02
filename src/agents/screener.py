from typing import List
from ..schemas import Candidate, JobDescription, ScreeningResult

def screen_resume(candidate: Candidate, jd: JobDescription) -> ScreeningResult:
    """
    Lightweight skill-matching screener.
    Replace with LPU/Groq inference & LangGraph prompt-connected skill extractors.
    """
    resume_text = candidate.resume_text.lower()
    matched = [s for s in jd.required_skills if s.lower() in resume_text]
    missing = [s for s in jd.required_skills if s not in matched]
    match_score = len(matched) / max(1, len(jd.required_skills))
    notes = f"Matched {len(matched)} required skills."
    return ScreeningResult(
        candidate_id=candidate.id,
        match_score=match_score,
        matched_skills=matched,
        missing_skills=missing,
        notes=notes,
    )
