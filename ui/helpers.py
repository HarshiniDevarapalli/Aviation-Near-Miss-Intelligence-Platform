import streamlit as st

from ui.constants import PROGRESS_MESSAGES, RISK_SUBTITLE


def render_section_label(label: str) -> None:
    st.markdown(f'<p class="section-label">{label}</p>', unsafe_allow_html=True)


def render_card_title(title: str) -> None:
    st.markdown(f'<p class="card-title">{title}</p>', unsafe_allow_html=True)


def render_field(label: str, value: str) -> None:
    display = value if value and value != "Unknown" else "_Not available_"
    st.markdown(f"**{label}**")
    st.markdown(display)


def render_metadata_badge(label: str, value: str) -> None:
    display = value if value and value != "Unknown" else "N/A"
    st.markdown(
        f"""
        <div class="meta-item">
            <span class="meta-label">{label}</span>
            <span class="meta-badge">{display}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_risk_card(level: str | None) -> None:
    css_class = {
        "HIGH": "risk-card-high",
        "MEDIUM": "risk-card-medium",
        "LOW": "risk-card-low",
    }.get(level or "", "risk-card-unknown")

    level_text = level if level else "Unassessed"
    st.markdown(
        f"""
        <div class="risk-card {css_class}">
            <div class="risk-card-level">{level_text}</div>
            <div class="risk-card-subtitle">{RISK_SUBTITLE}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_similarity_bar(score: float) -> None:
    st.markdown('<p class="section-label">Similarity</p>', unsafe_allow_html=True)
    st.progress(min(max(score / 100.0, 0.0), 1.0))
    st.markdown(
        f'<p class="similarity-value">{score:.0f}%</p>',
        unsafe_allow_html=True,
    )


def render_progress_steps(placeholder, active_step: int, *, complete: bool = False) -> None:
    lines = ['<div class="progress-panel">']
    for index, message in enumerate(PROGRESS_MESSAGES):
        if complete or index < active_step:
            state, icon = "done", "✓"
        elif index == active_step:
            state, icon = "active", "◉"
        else:
            state, icon = "", "○"
        lines.append(f'<div class="progress-step {state}">{icon} {message}</div>')
    lines.append("</div>")

    placeholder.markdown("".join(lines), unsafe_allow_html=True)
