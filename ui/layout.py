import streamlit as st

from ui.constants import APP_SUBTITLE, APP_TITLE, APP_VERSION, SESSION_AUTH, SESSION_USER


def _logo_svg(size: int = 22) -> str:
    return f"""
    <svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none"
         xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M21 16V14L13 9V7C13 5.9 12.1 5 11 5H10C8.9 5 8 5.9 8 7V9L2 12V14L8 12.5V19L6 20.5V22L12 21L18 22V20.5L16 19V12.5L22 14V12L21 16Z"
              fill="white"/>
    </svg>
    """


def render_topbar() -> None:
    user = st.session_state.get(SESSION_USER, "Safety Analyst")
    st.markdown(
        f"""
        <div class="app-topbar">
            <div class="topbar-left">
                <div class="topbar-logo">{_logo_svg()}</div>
                <div>
                    <div class="topbar-title">ANMI Platform</div>
                    <div class="topbar-subtitle">Aviation Safety Intelligence</div>
                </div>
            </div>
            <div class="topbar-right">
                <span class="topbar-pill">Operational</span>
                <span class="topbar-user">{user}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar_nav(on_new_analysis) -> None:
    with st.sidebar:
        st.markdown(
            f"""
            <div class="nav-brand">
                <div class="nav-logo">{_logo_svg(20)}</div>
                <div>
                    <div class="nav-brand-title">ANMI</div>
                    <div class="nav-brand-sub">Safety Intelligence</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)

        if st.button("New Analysis", use_container_width=True, type="primary"):
            on_new_analysis()

        st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)

        user = st.session_state.get(SESSION_USER, "Safety Analyst")
        st.markdown(
            f"""
            <div class="nav-user-card">
                <div class="nav-user-label">Signed in as</div>
                <div class="nav-user-email">{user}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Sign Out", use_container_width=True):
            st.session_state.pop(SESSION_AUTH, None)
            st.session_state.pop(SESSION_USER, None)
            st.rerun()

        st.markdown(
            f'<p class="sidebar-version">Version {APP_VERSION}</p>',
            unsafe_allow_html=True,
        )


def render_landing_hero() -> None:
    st.markdown(
        f"""
        <div class="hero-shell">
            <div class="hero-badge">Enterprise Safety Intelligence</div>
            <h2 class="hero-title">{APP_TITLE}</h2>
            <p class="hero-subtitle">{APP_SUBTITLE}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    features = [
        ("Historical Retrieval", "Semantic search across ASRS near-miss reports to surface relevant precedents."),
        ("AI Safety Assessment", "Gemini-powered operational risk analysis with structured intelligence reports."),
        ("Analytics Dashboard", "Evidence-driven charts, risk matrices, and trend insights from retrieved incidents."),
    ]
    for col, (title, desc) in zip((col1, col2, col3), features):
        with col:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-title">{title}</div>
                    <div class="feature-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_analysis_section_header() -> None:
    st.markdown(
        """
        <div class="section-header">
            <div>
                <h3 class="section-header-title">Safety Analysis</h3>
                <p class="section-header-desc">Describe an operational scenario to generate an intelligence assessment.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
