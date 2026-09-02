from ..schemas import HRMemo

def draft_hr_memo(to: str, subject: str, body_context: str) -> HRMemo:
    """
    Draft an email/memo to hiring manager or stakeholders.
    Replace with a styled/template generator that uses HITL approvals.
    """
    body = f"""Hello {to},

{body_context}

Best regards,
HR Ops
"""
    return HRMemo(to=to, subject=subject, body=body)
