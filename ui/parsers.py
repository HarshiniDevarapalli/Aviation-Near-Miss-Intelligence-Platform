import re
from datetime import datetime
from typing import Optional

REPORT_SECTIONS = [
    "Executive Summary",
    "Similar Historical Incidents",
    "Common Risk Factors",
    "Risk Assessment",
    "Recommendations",
    "Key Takeaways",
]

PRIORITY_SECTIONS = [
    "Recommendations",
    "Key Takeaways",
]

SECONDARY_SECTIONS = [
    "Similar Historical Incidents",
    "Common Risk Factors",
    "Risk Assessment",
]


def _extract_section(report: str, section_name: str) -> Optional[str]:
    """Extract a named section from the markdown report."""
    pattern = (
        rf"(?:#+\s*)?(?:\d+\.\s*)?{re.escape(section_name)}\s*\n+"
        rf"(.*?)(?=\n(?:#+\s*)?(?:\d+\.\s*)[A-Za-z]|\Z)"
    )
    match = re.search(pattern, report, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def parse_report_sections(report: str) -> dict[str, Optional[str]]:
    """Split a report into its named sections."""
    return {name: _extract_section(report, name) for name in REPORT_SECTIONS}


def extract_executive_summary(report: str) -> Optional[str]:
    return _extract_section(report, "Executive Summary")


def extract_risk_level(report: str) -> Optional[str]:
    search_text = _extract_section(report, "Risk Assessment") or report

    for level in ("HIGH", "MEDIUM", "LOW"):
        if re.search(rf"\b{level}\b", search_text, re.IGNORECASE):
            return level

    return None


def is_gemini_error(report: str) -> bool:
    return report.strip().startswith("Gemini Error:")


def distance_to_similarity_score(distance: float) -> float:
    return round(100.0 / (1.0 + distance), 1)


def format_incident_date(date_str: str) -> str:
    """Format incident dates as 'Month Year' when possible."""
    if not date_str or date_str == "Unknown":
        return "Unknown"

    value = str(date_str).strip()

    for fmt in ("%Y%m", "%Y-%m", "%Y/%m", "%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(value, fmt).strftime("%B %Y")
        except ValueError:
            continue

    return value


def to_title_case(text: str) -> str:
    """Convert text to professional title case while preserving acronyms."""
    if not text:
        return text

    words = []
    for word in text.split():
        if word.isupper():
            words.append(word)
        else:
            words.append(word.capitalize())
    return " ".join(words)


def normalize_section_content(content: str) -> str:
    """Improve readability by reducing excessive ALL CAPS in section bodies."""
    lines = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped and stripped == stripped.upper() and len(stripped) > 3 and stripped.isalpha():
            lines.append(to_title_case(stripped))
        else:
            lines.append(line)
    return "\n".join(lines)
