import streamlit as st
from src.schemas import Candidate, JobDescription
from src.agents import screen_resume, generate_interview_questions, run_compliance_audit, draft_hr_memo

st.set_page_config(page_title="Enterprise HR Agents", layout="centered")

st.title("Enterprise HR Agents — Demo")

st.sidebar.header("Inputs")
candidate_id = st.sidebar.text_input("Candidate ID", value="cand-001")
name = st.sidebar.text_input("Candidate name")
email = st.sidebar.text_input("Candidate email")
jd_title = st.sidebar.text_input("Job title", value="Software Engineer")
run_button = st.sidebar.button("Run Pipeline")

resume_text = st.text_area("Paste resume text here", height=240)
jd_text = st.text_area("Paste job description here", height=240)

if run_button:
    candidate = Candidate(id=candidate_id, name=name or None, email=email or None, resume_text=resume_text)
    jd = JobDescription(id="jd-001", title=jd_title, description=jd_text, required_skills=["Python", "APIs"])
    screening = screen_resume(candidate, jd)
    st.subheader("Screening")
    st.json(screening.model_dump())

    st.subheader("Interview Questions")
    qs = generate_interview_questions(screening)
    for q in qs:
        st.write(f"- {q.question} ({q.intent})")

    st.subheader("Compliance Audit")
    report = run_compliance_audit(candidate, jd)
    st.json(report.model_dump())

    st.subheader("Draft HR Memo")
    memo = draft_hr_memo(to="Hiring Manager", subject=f"Candidate {candidate.id} Summary", body_context=f"Screening score: {screening.match_score}")
    st.code(memo.body)
