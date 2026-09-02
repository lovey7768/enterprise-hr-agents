from typing import TypedDict, Optional, List, Dict

class CandidateState(TypedDict, total=False):
    candidate_id: str
    resume_text: str
    jd_text: str
    parsed_resume: Dict[str, object]
    skills: List[str]
    screened: bool
    screening_score: Optional[float]
    screening_notes: Optional[str]
    interview_questions: List[Dict[str, str]]
    interview_notes: List[str]
    compliance_issues: List[str]
    approvals: Dict[str, bool]
    metadata: Dict[str, object]
