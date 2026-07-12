import sys
from pathlib import Path

import streamlit as st

project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

from ui.analysis import execute_analysis
from ui.auth import render_login_page
from ui.components import render_query_form, render_results
from ui.constants import SESSION_AUTH, SESSION_RESULT
from ui.layout import (
    render_analysis_section_header,
    render_landing_hero,
    render_sidebar_nav,
    render_topbar,
)
from ui.styles import inject_custom_css


def _clear_analysis() -> None:
    st.session_state.pop(SESSION_RESULT, None)
    st.rerun()


def main() -> None:
    st.set_page_config(
        page_title="Aviation Near-Miss Intelligence",
        page_icon="✈",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    inject_custom_css()

    if not st.session_state.get(SESSION_AUTH):
        render_login_page()
        return

    render_sidebar_nav(_clear_analysis)
    render_topbar()

    if not st.session_state.get(SESSION_RESULT):
        render_landing_hero()

    render_analysis_section_header()
    analyze_clicked, query = render_query_form()

    if analyze_clicked:
        if not query or not query.strip():
            st.warning("Please describe an aviation scenario before running the analysis.")
        else:
            execute_analysis(query.strip())

    if result := st.session_state.get(SESSION_RESULT):
        st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)
        with st.container(border=True):
            render_results(result)


if __name__ == "__main__":
    main()
