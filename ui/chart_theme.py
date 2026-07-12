"""Shared Plotly styling for analytics charts."""

CHART_COLORS = ["#2563eb", "#3b82f6", "#6366f1", "#8b5cf6", "#0ea5e9", "#64748b"]

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Plus Jakarta Sans, Inter, sans-serif", color="#334155", size=12),
    margin=dict(l=16, r=16, t=16, b=16),
    height=340,
    xaxis=dict(
        showgrid=True,
        gridcolor="rgba(148,163,184,0.15)",
        linecolor="rgba(148,163,184,0.25)",
        tickfont=dict(size=11, color="#64748b"),
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="rgba(148,163,184,0.15)",
        linecolor="rgba(148,163,184,0.25)",
        tickfont=dict(size=11, color="#64748b"),
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        font=dict(size=11, color="#64748b"),
    ),
    hoverlabel=dict(
        bgcolor="#0f172a",
        font_size=12,
        font_family="Plus Jakarta Sans, Inter, sans-serif",
    ),
)
