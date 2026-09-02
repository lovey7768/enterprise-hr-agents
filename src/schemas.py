from typing import List, Optional
from pydantic import BaseModel, Field

class JobDescription(BaseModel):
    id: str
    title: str
    description: str
    required_skills: List[str] = Field(default_factory=list)
    optional_skills: List[str] = Field(default_factory=list)
    location: Optional[str] = None
    salary_range: Optional[str] = None

class Candidate(BaseModel):
    id: str
    name: Optional[str] = None
    email: Optional[str] = None
    resume_text: str

class ScreeningResult(BaseModel):
    candidate_id: str
    match_score: float
    matched_skills: List[str]
    missing_skills: List[str]
    notes: Optional[str] = None

class InterviewQuestion(BaseModel):
    question: str
    intent: Optional[str] = None
    difficulty: Optional[str] = "medium"

class ComplianceReport(BaseModel):
    candidate_id: str
    visa_issues: List[str] = []
    compensation_issues: List[str] = []
    notes: Optional[str] = None

class HRMemo(BaseModel):
    to: str
    subject: str
    body: str
