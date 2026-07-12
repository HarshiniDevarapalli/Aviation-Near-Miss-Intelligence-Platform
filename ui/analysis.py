import threading
import time

import streamlit as st

from src.rag_pipeline import RAGPipeline

from ui.constants import PROGRESS_STEP_DELAYS, SESSION_RESULT
from ui.helpers import render_progress_steps


@st.cache_resource(show_spinner="Initializing analysis engine...")
def get_pipeline() -> RAGPipeline:
    return RAGPipeline()


def run_analysis(query: str) -> dict:
    """Run pipeline.run() while displaying progressive status updates."""
    result_holder: dict = {}
    error_holder: dict = {}

    def worker() -> None:
        try:
            result_holder["data"] = get_pipeline().run(query)
        except Exception as exc:
            error_holder["error"] = exc

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()

    progress = st.empty()
    step = 0
    started_at = time.time()

    while thread.is_alive():
        elapsed = time.time() - started_at
        while step < len(PROGRESS_STEP_DELAYS) and elapsed >= PROGRESS_STEP_DELAYS[step]:
            step += 1

        active_step = min(step, len(PROGRESS_STEP_DELAYS))
        render_progress_steps(progress, active_step)
        time.sleep(0.3)

    thread.join()
    render_progress_steps(progress, 0, complete=True)

    if "error" in error_holder:
        raise error_holder["error"]

    return result_holder["data"]


def display_analysis_error(exc: Exception) -> None:
    message = str(exc).lower()

    if isinstance(exc, ConnectionError):
        st.error(
            "Unable to reach the analysis service. "
            "Please check your network connection and try again."
        )
    elif isinstance(exc, TimeoutError):
        st.error(
            "The analysis request timed out. "
            "Please try again with a shorter scenario description."
        )
    elif any(token in message for token in ("api", "key", "gemini")):
        st.error(
            "The AI analysis service is unavailable. "
            "Please verify your API credentials and try again."
        )
    elif any(token in message for token in ("chroma", "database")):
        st.error(
            "The incident database is unavailable. "
            "Please ensure the vector store has been initialized."
        )
    else:
        st.error(
            "An unexpected error occurred during analysis. "
            "Please try again or contact your system administrator."
        )

    with st.expander("Technical details"):
        st.code(str(exc))


def execute_analysis(query: str) -> None:
    try:
        st.session_state[SESSION_RESULT] = run_analysis(query)
    except Exception as exc:
        display_analysis_error(exc)
