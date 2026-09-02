# enterprise-hr-agents
Stateful multi-agent HR automation platform using LangGraph, Pydantic v2 data contracts, Groq LPU inference, and Human-in-the-Loop (HITL) approval gates.


# 💼 Enterprise HR Multi-Agent Automation Suite

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Orchestration](https://img.shields.io/badge/Orchestrator-LangGraph-orange.svg)](https://github.com/langchain-ai/langgraph)
[![Inference Engine](https://img.shields.io/badge/Inference-Groq_LPU-yellowgreen.svg)](https://groq.com/)
[![Contracts](https://img.shields.io/badge/Data_Contracts-Pydantic_v2-red.svg)](https://docs.pydantic.dev/)
[![UI Framework](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An enterprise-grade, stateful multi-agent human resources automation platform. Built with **LangGraph**, **Pydantic v2 data contracts**, **Groq LPU accelerated inference**, and **Streamlit**, this project demonstrates a modular, stateful approach to HR automation including screening, interview generation, compliance auditing, and human-in-the-loop (HITL) checkpoints.

---

## 🏛️ System Architecture

```text
                               ┌────────────────────────────────┐
                               │       User / HR Recruiter      │
                               │   (PDF Resume & JD Ingestion)  │
                               └───────────────┬────────────────┘
                                               │
                                               ▼
                               ┌────────────────────────────────┐
                               │  LangGraph State Orchestrator  │
                               └───────────────┬────────────────┘
                                               │
               ┌───────────────────────────────┴───────────────────────────�[...]
               ▼                                                               ▼
    ┌──────────────────────┐                                        ┌──────────────────────┐
    │ 1. Resume Screener   │                                        │ 3. Policy & Comp     │
    │    & Skill Matcher   │                                        │    Compliance Auditor│
    └──────────┬───────────┘                                        └──────────┬───────────┘
               │                                                               │
               ▼                                                               │
    ┌──────────────────────┐                                                   │
    │ 2. Interview Auditor │                                                   │
    │    & Question Engine │                                                   │
    └──────────┬───────────┘                                                   │
               │                                                               │
               └───────────────────────┬───────────────────────────────────�[...]
                                       │
                                       ▼
                       ┌────────────────────────────────┐
                       │ 🛑 HUMAN-IN-THE-LOOP (HITL)    │ ──► [Manager Review & Approval]
                       │    Memory Checkpoint Gate      │
                       └───────────────┬────────────────┘
                                       │ (Approved)
                                       ▼
                       ┌────────────────────────────────┐
                       │  4. HR Ops & Communication     │
                       │     (Email / Memo Dispatch)    │
                       └────────────────────────────────┘

```

---

## 📁 Repository structure

For contributors and reviewers, here's the project layout to help understand where code and configuration live:

```text
enterprise-hr-agents/
├── src/
│   ├── __init__.py
│   ├── state.py            # TypedDict state container
│   ├── schemas.py          # Pydantic v2 data contracts
│   │   ├── agents/
│   │   │   ├── __init__.py
│   │   │   ├── screener.py     # Skill extraction & gap analysis
│   │   │   ├── interviewer.py  # Targeted technical & behavioral question engine
│   │   │   ├── compliance.py   # Visa & compensation budget auditor
│   │   │   └── ops.py          # Final executive email & memo drafter
│   └── graph.py            # LangGraph assembly with checkpointer
├── app.py                  # Streamlit dashboard interface
├── requirements.txt        # Pinned project dependencies
├── .gitignore              # Environment & build ignores
└── README.md
```

This tree provides a quick map for developers: core agents live under src/agents, data contracts and state definitions are in src/, the LangGraph orchestration and checkpointer are in src/graph.py, and a minimal Streamlit demo is provided in app.py.

If you'd like, I can also add CONTRIBUTING.md and a short onboarding section with setup and run steps to make it even easier for new contributors.
