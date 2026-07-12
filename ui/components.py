import streamlit as st

from src.config import EMBEDDING_MODEL, GEMINI_MODEL

from ui.analytics import render_analytics
from ui.constants import (
    QUERY_EXAMPLE,
    QUERY_PLACEHOLDER,
    SESSION_RESULT,
)
from ui.export import render_export_actions
from ui.helpers import (
    render_card_title,
    render_field,
    render_metadata_badge,
    render_risk_card,
    render_section_label,
    render_similarity_bar,
)
from ui.parsers import (
    PRIORITY_SECTIONS,
    SECONDARY_SECTIONS,
    distance_to_similarity_score,
    extract_risk_level,
    format_incident_date,
    is_gemini_error,
    normalize_section_content,
    parse_report_sections,
    to_title_case,
)


def render_query_form() -> tuple[bool, str]:
    with st.container(border=True):
        query = st.text_area(
            label="Scenario Description",
            placeholder=QUERY_PLACEHOLDER,
            height=120,
            label_visibility="collapsed",
        )
        st.caption(f"Example: {QUERY_EXAMPLE}")
        return st.button(
            "Analyze Incident",
            type="primary",
            use_container_width=True,
        ), query


def _model_display_name(model_id: str) -> str:
    return model_id.split("/")[-1].replace("-", " ").title()


def render_analysis_summary(result: dict) -> None:
    incidents = result.get("retrieved_incidents", [])
    report = result.get("report", "")
    status = "Error" if is_gemini_error(report) else "Complete"
    status_class = "status-error" if status == "Error" else "status-complete"

    with st.container(border=True):
        render_card_title("Analysis Summary")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Historical Incidents Retrieved", len(incidents))
        col2.metric("Embedding Model", _model_display_name(EMBEDDING_MODEL))
        col3.metric("Language Model", _model_display_name(GEMINI_MODEL))
        col4.markdown(
            f"""
            <div class="summary-status">
                <span class="section-label">Analysis Status</span>
                <span class="status-badge {status_class}">{status}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


def _render_section_expander(title: str, content: str | None, *, expanded: bool = False) -> None:
    if not content:
        return

    with st.expander(to_title_case(title), expanded=expanded):
        st.markdown(normalize_section_content(content))


def render_safety_assessment(result: dict) -> None:
    report = result.get("report", "")

    if is_gemini_error(report):
        st.error(
            "The analysis service encountered an error. "
            "Please verify your API configuration and try again."
        )
        st.caption(report)
        return

    sections = parse_report_sections(report)
    risk_level = extract_risk_level(report)

    render_analysis_summary(result)
    st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)

    with st.expander("Executive Summary", expanded=True):
        summary = sections.get("Executive Summary")
        if summary:
            st.markdown(normalize_section_content(summary))
        else:
            st.markdown(
                '<p class="muted-text">Executive summary not available in the generated report.</p>',
                unsafe_allow_html=True,
            )

    st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)

    with st.container(border=True):
        render_section_label("Risk Level")
        render_risk_card(risk_level)

    st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)

    for section_name in PRIORITY_SECTIONS:
        _render_section_expander(section_name, sections.get(section_name))

    for section_name in SECONDARY_SECTIONS:
        _render_section_expander(section_name, sections.get(section_name))

    st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)
    render_card_title("Full Safety Intelligence Report")

    with st.container(border=True):
        st.markdown(normalize_section_content(report))

    st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)
    render_export_actions(report)


def _incident_header(incident: dict) -> str:
    metadata = incident.get("metadata", {})
    incident_id = incident.get("id", metadata.get("acn", "Unknown"))
    primary_problem = metadata.get("primary_problem", "Unknown")
    date = format_incident_date(metadata.get("date", "Unknown"))
    similarity = distance_to_similarity_score(incident.get("distance", 0))
    return (
        f"Incident {incident_id}  ·  {date}  ·  {primary_problem}  ·  "
        f"{similarity:.0f}% Similarity"
    )


def _render_incident_card(incident: dict) -> None:
    metadata = incident.get("metadata", {})
    incident_id = incident.get("id", metadata.get("acn", "Unknown"))
    primary_problem = metadata.get("primary_problem", "Unknown")
    formatted_date = format_incident_date(metadata.get("date", "Unknown"))
    similarity = distance_to_similarity_score(incident.get("distance", 0))

    with st.expander(_incident_header(incident), expanded=False):
        col_left, col_right = st.columns(2)

        with col_left:
            render_metadata_badge("Incident ID", incident_id)
            render_metadata_badge("Primary Problem", primary_problem)

        with col_right:
            render_metadata_badge("Date", formatted_date)
            render_metadata_badge(
                "Result",
                metadata.get("result", "Unknown"),
            )

        st.divider()

        render_field(
            "Contributing Factors",
            metadata.get("contributing_factors", "Unknown"),
        )

        render_similarity_bar(similarity)

        st.divider()

        with st.expander("Narrative"):
            narrative = incident.get("document", "")
            st.markdown(narrative if narrative else "_No narrative available._")


def render_historical_evidence(incidents: list) -> None:
    if not incidents:
        st.info("No historical incidents were retrieved for this analysis.")
        return

    st.caption(
        f"{len(incidents)} historical incident(s) retrieved as supporting evidence."
    )
    st.markdown("<div class='section-spacer-sm'></div>", unsafe_allow_html=True)

    for incident in incidents:
        _render_incident_card(incident)


def render_results(result: dict) -> None:
    tab_assessment, tab_evidence, tab_analytics = st.tabs(
        ["Safety Assessment", "Historical Incident Evidence", "Analytics"]
    )

    with tab_assessment:
        render_safety_assessment(result)

    with tab_evidence:
        render_historical_evidence(result.get("retrieved_incidents", []))

    with tab_analytics:
        render_analytics(result.get("retrieved_incidents", []))
