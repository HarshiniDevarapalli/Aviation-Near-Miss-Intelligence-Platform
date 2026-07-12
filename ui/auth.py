import streamlit as st

from ui.constants import APP_SUBTITLE, APP_TITLE, SESSION_AUTH, SESSION_USER


def _logo_svg(size: int = 28) -> str:
    return f"""
    <svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none"
         xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <path d="M21 16V14L13 9V7C13 5.9 12.1 5 11 5H10C8.9 5 8 5.9 8 7V9L2 12V14L8 12.5V19L6 20.5V22L12 21L18 22V20.5L16 19V12.5L22 14V12L21 16Z"
              fill="currentColor"/>
    </svg>
    """


def render_login_page() -> None:
    st.markdown(
        """
        <div class="login-page">
            <div class="login-backdrop"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, center, right = st.columns([1, 1.15, 1])
    with center:
        st.markdown(
            f"""
            <div class="login-card-header">
                <div class="login-logo">{_logo_svg(30)}</div>
                <h1>{APP_TITLE}</h1>
                <p>{APP_SUBTITLE}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("login_form", clear_on_submit=False):
            email = st.text_input("Email", placeholder="analyst@airline.com")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            submitted = st.form_submit_button("Sign In", type="primary", use_container_width=True)

        if submitted:
            st.session_state[SESSION_AUTH] = True
            st.session_state[SESSION_USER] = email.strip() or "Safety Analyst"
            st.rerun()

        st.markdown(
            '<p class="login-footnote">Secure access for authorized aviation safety personnel.</p>',
            unsafe_allow_html=True,
        )
