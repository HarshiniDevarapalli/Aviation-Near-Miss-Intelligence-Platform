APP_TITLE = "Aviation Near-Miss Intelligence Platform"
APP_SUBTITLE = (
    "AI-powered operational safety analysis using historical aviation incident reports."
)
APP_VERSION = "1.0.0"

QUERY_PLACEHOLDER = "Describe an aviation scenario..."
QUERY_EXAMPLE = "Aircraft taxiing in dense fog with delayed ATC communication."

SESSION_RESULT = "analysis_result"
SESSION_AUTH = "authenticated"
SESSION_USER = "user_email"

PROGRESS_MESSAGES = [
    "Connecting to vector database...",
    "Searching historical incidents...",
    "Ranking retrieved evidence...",
    "Building incident context...",
    "Generating AI safety assessment...",
    "Finalizing report...",
]

# Elapsed seconds before advancing to the next progress step.
PROGRESS_STEP_DELAYS = (3, 7, 12, 18, 25, 32)

EXPORT_FILENAME = "aviation_safety_report.md"

RISK_SUBTITLE = "Operational Risk"
