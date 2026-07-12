"""Analytics dashboard computed exclusively from retrieved incidents."""

from collections import Counter
from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from ui.chart_theme import CHART_COLORS, PLOTLY_LAYOUT
from ui.helpers import render_card_title
from ui.parsers import distance_to_similarity_score


def _split_factors(factors_str: str) -> list[str]:
    if not factors_str or factors_str == "Unknown":
        return []
    return [part.strip() for part in factors_str.split(";") if part.strip()]


def _extract_year(date_str: str) -> int | None:
    if not date_str or date_str == "Unknown":
        return None

    value = str(date_str).strip()
    for fmt in ("%Y%m", "%Y-%m", "%Y/%m", "%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(value, fmt).year
        except ValueError:
            continue

    if value.isdigit() and len(value) >= 4:
        return int(value[:4])

    return None


def _incident_id(incident: dict) -> str:
    metadata = incident.get("metadata", {})
    return str(incident.get("id", metadata.get("acn", "Unknown")))


def _frequency_tier(count: int, max_count: int) -> str:
    if max_count == 0:
        return "Low"
    ratio = count / max_count
    if ratio >= 0.66:
        return "High"
    if ratio >= 0.33:
        return "Medium"
    return "Low"


def _risk_level_for_tier(tier: str) -> tuple[str, str]:
    mapping = {
        "High": ("🔴 High", "matrix-high"),
        "Medium": ("🟠 Medium", "matrix-medium"),
        "Low": ("🟡 Low", "matrix-low"),
    }
    return mapping.get(tier, ("🟡 Low", "matrix-low"))


def compute_analytics(incidents: list) -> dict:
    primary_problems = []
    all_factors: list[str] = []
    years: list[int] = []
    similarities: list[dict] = []

    for incident in incidents:
        metadata = incident.get("metadata", {})
        problem = metadata.get("primary_problem", "Unknown")
        if problem and problem != "Unknown":
            primary_problems.append(problem)

        all_factors.extend(_split_factors(metadata.get("contributing_factors", "")))

        year = _extract_year(metadata.get("date", ""))
        if year:
            years.append(year)

        similarities.append(
            {
                "incident": f"Incident {_incident_id(incident)}",
                "score": distance_to_similarity_score(incident.get("distance", 0)),
            }
        )

    problem_counts = Counter(primary_problems)
    factor_counts = Counter(all_factors)
    year_counts = Counter(years)

    avg_similarity = (
        round(sum(item["score"] for item in similarities) / len(similarities), 1)
        if similarities
        else 0.0
    )

    top_problem = problem_counts.most_common(1)[0][0] if problem_counts else None
    top_factor = factor_counts.most_common(1)[0][0] if factor_counts else None

    return {
        "count": len(incidents),
        "avg_similarity": avg_similarity,
        "top_problem": top_problem,
        "top_factor": top_factor,
        "problem_counts": problem_counts,
        "factor_counts": factor_counts,
        "year_counts": year_counts,
        "similarities": similarities,
        "all_factors": all_factors,
        "years": years,
    }


def _apply_chart_theme(fig: go.Figure) -> go.Figure:
    fig.update_layout(**PLOTLY_LAYOUT)
    fig.update_traces(marker_line_width=0, hovertemplate="%{label}<br>%{value}<extra></extra>")
    return fig


def render_kpi_cards(stats: dict) -> None:
    cards = [
        ("📋", "Retrieved Incidents", str(stats["count"])),
        ("📊", "Average Similarity", f"{stats['avg_similarity']:.0f}%"),
        ("⚠️", "Most Common Risk", stats["top_problem"] or "N/A"),
        ("🔍", "Top Contributing Factor", stats["top_factor"] or "N/A"),
    ]

    cols = st.columns(4)
    for col, (icon, label, value) in zip(cols, cards):
        with col:
            st.markdown(
                f"""
                <div class="analytics-kpi">
                    <div class="analytics-kpi-icon">{icon}</div>
                    <div class="analytics-kpi-label">{label}</div>
                    <div class="analytics-kpi-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_risk_distribution(stats: dict) -> None:
    render_card_title("Risk Distribution")
    counts = stats["problem_counts"]
    if not counts:
        st.caption("No primary problem data available in retrieved incidents.")
        return

    df = pd.DataFrame(
        [{"Primary Problem": name, "Count": count} for name, count in counts.items()]
    )
    fig = px.pie(
        df,
        names="Primary Problem",
        values="Count",
        hole=0.45,
        color_discrete_sequence=CHART_COLORS,
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(_apply_chart_theme(fig), use_container_width=True)


def render_contributing_factors_chart(stats: dict) -> None:
    render_card_title("Most Frequent Contributing Factors")
    counts = stats["factor_counts"]
    if not counts:
        st.caption("No contributing factor data available in retrieved incidents.")
        return

    df = pd.DataFrame(
        [{"Factor": name, "Count": count} for name, count in counts.most_common()]
    )
    fig = px.bar(
        df,
        x="Count",
        y="Factor",
        orientation="h",
        color_discrete_sequence=[CHART_COLORS[0]],
    )
    fig.update_layout(yaxis=dict(categoryorder="total ascending"))
    st.plotly_chart(_apply_chart_theme(fig), use_container_width=True)


def render_historical_timeline(stats: dict) -> None:
    render_card_title("Historical Incident Timeline")
    counts = stats["year_counts"]
    if not counts:
        st.caption("No date metadata available to build a timeline.")
        return

    df = pd.DataFrame(
        [{"Year": year, "Incidents": count} for year, count in sorted(counts.items())]
    )
    fig = px.line(
        df,
        x="Year",
        y="Incidents",
        markers=True,
        color_discrete_sequence=[CHART_COLORS[0]],
    )
    fig.update_layout(xaxis=dict(dtick=1))
    st.plotly_chart(_apply_chart_theme(fig), use_container_width=True)


def render_similarity_analysis(stats: dict) -> None:
    render_card_title("Similarity Analysis")
    similarities = stats["similarities"]
    if not similarities:
        st.caption("No similarity scores available.")
        return

    df = pd.DataFrame(similarities).sort_values("score", ascending=True)
    fig = px.bar(
        df,
        x="score",
        y="incident",
        orientation="h",
        labels={"score": "Similarity (%)", "incident": ""},
        color_discrete_sequence=[CHART_COLORS[0]],
    )
    fig.update_layout(yaxis=dict(categoryorder="total ascending"))
    st.plotly_chart(_apply_chart_theme(fig), use_container_width=True)


def render_recurring_themes(stats: dict) -> None:
    render_card_title("Recurring Themes")
    factors = stats["factor_counts"].most_common(8)
    if not factors:
        st.caption("No recurring themes identified from retrieved incidents.")
        return

    badges = "".join(
        f'<span class="theme-badge">{name}</span>' for name, _ in factors
    )
    st.markdown(f'<div class="theme-badge-row">{badges}</div>', unsafe_allow_html=True)


def render_risk_matrix(stats: dict) -> None:
    render_card_title("Operational Risk Matrix")
    counts = stats["problem_counts"]
    if not counts:
        st.caption("Insufficient data to build a risk matrix.")
        return

    max_count = max(counts.values())
    rows = []
    for category, count in counts.most_common():
        tier = _frequency_tier(count, max_count)
        risk_label, css_class = _risk_level_for_tier(tier)
        rows.append(
            f'<tr><td>{category}</td><td>{tier}</td>'
            f'<td class="{css_class}">{risk_label}</td></tr>'
        )

    st.markdown(
        f"""
        <table class="risk-matrix">
            <thead>
                <tr>
                    <th>Category</th>
                    <th>Frequency</th>
                    <th>Risk Level</th>
                </tr>
            </thead>
            <tbody>{"".join(rows)}</tbody>
        </table>
        """,
        unsafe_allow_html=True,
    )


def generate_insights(incidents: list, stats: dict) -> list[str]:
    insights: list[str] = []
    total = stats["count"]
    if total == 0:
        return insights

    if stats["top_problem"]:
        insights.append(
            f"{stats['top_problem']}-related hazards dominate the retrieved incidents."
        )

    if stats["top_factor"]:
        incidents_with_factor = sum(
            1
            for incident in incidents
            if stats["top_factor"]
            in _split_factors(incident.get("metadata", {}).get("contributing_factors", ""))
        )
        pct = round((incidents_with_factor / total) * 100)
        insights.append(
            f"{stats['top_factor']} appear in {pct}% of retrieved reports."
        )

    if stats["years"]:
        min_year, max_year = min(stats["years"]), max(stats["years"])
        if min_year == max_year:
            insights.append(f"All retrieved incidents occurred during {min_year}.")
        else:
            insights.append(
                f"Most similar incidents occurred during {min_year}–{max_year}."
            )

    combined_factors = " ".join(stats["all_factors"]).lower()
    theme_keywords = {
        "Night operations": ["night", "dark"],
        "Communication issues": ["communication", "radio", "atc"],
        "Construction activity": ["construction", "work in progress", "wipp"],
        "Airport infrastructure deficiencies": [
            "taxiway",
            "marking",
            "signage",
            "lighting",
            "infrastructure",
        ],
    }

    for theme, keywords in theme_keywords.items():
        if any(keyword in combined_factors for keyword in keywords):
            insights.append(f"{theme.capitalize()} appear frequently across retrieved incidents.")

    if stats["avg_similarity"] >= 75:
        insights.append(
            f"Retrieved incidents show strong semantic alignment "
            f"(average similarity {stats['avg_similarity']:.0f}%)."
        )

    return insights[:6]


def render_quick_insights(incidents: list, stats: dict) -> None:
    render_card_title("Quick Insights")
    insights = generate_insights(incidents, stats)
    if not insights:
        st.caption("Insufficient data to generate insights.")
        return

    items = "".join(f"<li>{insight}</li>" for insight in insights)
    st.markdown(f'<ul class="insights-list">{items}</ul>', unsafe_allow_html=True)


def render_analytics(incidents: list) -> None:
    if not incidents:
        st.info("No historical incidents were retrieved. Analytics requires retrieved evidence.")
        return

    stats = compute_analytics(incidents)

    render_kpi_cards(stats)
    st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)

    col_left, col_right = st.columns(2)
    with col_left:
        with st.container(border=True):
            render_risk_distribution(stats)
    with col_right:
        with st.container(border=True):
            render_contributing_factors_chart(stats)

    st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)

    col_tl, col_sim = st.columns(2)
    with col_tl:
        with st.container(border=True):
            render_historical_timeline(stats)
    with col_sim:
        with st.container(border=True):
            render_similarity_analysis(stats)

    st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)

    with st.container(border=True):
        render_recurring_themes(stats)

    st.markdown("<div class='section-spacer-sm'></div>", unsafe_allow_html=True)

    with st.container(border=True):
        render_risk_matrix(stats)

    st.markdown("<div class='section-spacer-sm'></div>", unsafe_allow_html=True)

    with st.container(border=True):
        render_quick_insights(incidents, stats)
