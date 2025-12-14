import re
from dataclasses import dataclass
from typing import List

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE_RE = re.compile(r"\b(\+?\d{1,3}[\s-]?)?(\(?\d{2,4}\)?[\s-]?)?\d{3,4}[\s-]?\d{3,4}\b")
IPV4_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
LINKEDIN_RE = re.compile(r"https?://(www\.)?linkedin\.com/[^ \n]+", re.IGNORECASE)

SENSITIVE_KEYWORDS = [
    "passport", "driver license", "medicare", "bank account", "credit card",
    "tax file number", "tfn", "dob", "date of birth"
]

@dataclass
class PiiFinding:
    kind: str
    sample: str

def detect_pii(text: str) -> List[PiiFinding]:
    findings: List[PiiFinding] = []

    for m in EMAIL_RE.finditer(text):
        findings.append(PiiFinding("email", m.group(0)))

    for m in PHONE_RE.finditer(text):
        s = m.group(0).strip()
        digits = re.sub(r"\D", "", s)
        if len(digits) >= 9:
            findings.append(PiiFinding("phone", s))

    for m in IPV4_RE.finditer(text):
        findings.append(PiiFinding("ip_address", m.group(0)))

    for m in LINKEDIN_RE.finditer(text):
        findings.append(PiiFinding("profile_link", m.group(0)))

    lowered = text.lower()
    for kw in SENSITIVE_KEYWORDS:
        if kw in lowered:
            findings.append(PiiFinding("sensitive_keyword", kw))

    # Deduplicate
    seen = set()
    uniq = []
    for f in findings:
        k = (f.kind, f.sample)
        if k not in seen:
            uniq.append(f)
            seen.add(k)
    return uniq

def redact_pii(text: str) -> str:
    text = EMAIL_RE.sub("[REDACTED_EMAIL]", text)

    def _phone_sub(m: re.Match) -> str:
        s = m.group(0).strip()
        digits = re.sub(r"\D", "", s)
        if len(digits) >= 9:
            return "[REDACTED_PHONE]"
        return s

    text = PHONE_RE.sub(_phone_sub, text)
    text = LINKEDIN_RE.sub("[REDACTED_PROFILE_LINK]", text)
    return text
