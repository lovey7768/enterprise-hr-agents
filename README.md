# enterprise-hr-agents
Stateful multi-agent HR automation platform using LangGraph, Pydantic v2 data contracts, Groq LPU inference, and Human-in-the-Loop (HITL) approval gates.


# 💼 Enterprise HR Multi-Agent Automation Suite

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Orchestration](https://img.shields.io/badge/Orchestrator-LangGraph-orange.svg)](https://github.com/langchain-ai/langgraph)
[![Inference Engine](https://img.shields.io/badge/Inference-Groq_LPU-yellowgreen.svg)](https://groq.com/)
[![Contracts](https://img.shields.io/badge/Data_Contracts-Pydantic_v2-red.svg)](https://docs.pydantic.dev/)
[![UI Framework](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An enterprise-grade, stateful multi-agent human resources automation platform. Built with **LangGraph**, **Pydantic v2 data contracts**, **Groq LPU accelerated inference**, and **Streamlit**, this system replaces fragile prompt chains with a stateful Directed Acyclic Graph (DAG) featuring an interactive **Human-in-the-Loop (HITL) authorization checkpoint**.

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
               ┌───────────────────────────────┴───────────────────────────────┐
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
               └───────────────────────┬───────────────────────────────────────┘
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
