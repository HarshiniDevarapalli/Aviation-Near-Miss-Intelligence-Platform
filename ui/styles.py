import streamlit as st


def inject_custom_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

        :root {
            --bg-app: #f4f6fb;
            --bg-surface: #ffffff;
            --bg-muted: #eef2f8;
            --border: #e2e8f0;
            --border-strong: #cbd5e1;
            --text-primary: #0f172a;
            --text-secondary: #64748b;
            --text-muted: #94a3b8;
            --accent: #2563eb;
            --accent-dark: #1d4ed8;
            --accent-soft: #eff6ff;
            --success: #059669;
            --warning: #d97706;
            --danger: #dc2626;
            --shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.05);
            --shadow-md: 0 8px 24px rgba(15, 23, 42, 0.08);
            --shadow-lg: 0 20px 48px rgba(15, 23, 42, 0.12);
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
            --radius-xl: 20px;
        }

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            color: var(--text-primary);
            line-height: 1.6;
        }

        #MainMenu, footer, header[data-testid="stHeader"] {
            visibility: hidden;
        }

        .stApp {
            background:
                radial-gradient(circle at 0% 0%, rgba(37, 99, 235, 0.06), transparent 28%),
                radial-gradient(circle at 100% 0%, rgba(99, 102, 241, 0.05), transparent 24%),
                var(--bg-app);
        }

        .block-container {
            padding-top: 1rem;
            padding-bottom: 3rem;
            max-width: 1240px;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0b1220 0%, #111827 100%);
            border-right: 1px solid rgba(255,255,255,0.06);
        }

        section[data-testid="stSidebar"] .block-container {
            padding-top: 1.5rem;
        }

        section[data-testid="stSidebar"] .stButton > button {
            border-radius: var(--radius-sm);
            font-weight: 600;
            transition: all 0.18s ease;
        }

        section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            border: none;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
        }

        section[data-testid="stSidebar"] .stButton > button:not([kind="primary"]) {
            background: rgba(255,255,255,0.04);
            color: #cbd5e1;
            border: 1px solid rgba(255,255,255,0.08);
        }

        /* Login */
        .login-page {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
        }

        .login-backdrop {
            position: absolute;
            inset: 0;
            background:
                radial-gradient(circle at 20% 20%, rgba(37, 99, 235, 0.18), transparent 35%),
                radial-gradient(circle at 80% 0%, rgba(99, 102, 241, 0.14), transparent 30%),
                linear-gradient(180deg, #eef2ff 0%, #f8fafc 100%);
        }

        .login-card-header {
            text-align: center;
            margin-bottom: 1rem;
        }

        .login-card-header h1 {
            font-size: clamp(1.35rem, 2.5vw, 1.75rem);
            font-weight: 700;
            letter-spacing: -0.03em;
            margin: 0.75rem 0 0.45rem;
            color: var(--text-primary);
        }

        .login-card-header p {
            color: var(--text-secondary);
            font-size: 0.88rem;
            margin: 0;
            line-height: 1.55;
        }

        .login-logo {
            width: 56px;
            height: 56px;
            margin: 2rem auto 0;
            border-radius: 14px;
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-md);
        }

        .login-footnote {
            text-align: center;
            color: var(--text-muted);
            font-size: 0.76rem;
            margin-top: 1rem;
        }

        div[data-testid="stForm"] {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 1.35rem;
            box-shadow: var(--shadow-md);
        }

        /* Report typography */
        div[data-testid="stExpanderDetails"] div[data-testid="stMarkdownContainer"] p,
        div[data-testid="stExpanderDetails"] div[data-testid="stMarkdownContainer"] li,
        div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stMarkdownContainer"] p,
        div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stMarkdownContainer"] li {
            color: #334155;
            font-size: 0.93rem;
            line-height: 1.75;
        }

        div[data-testid="stExpanderDetails"] div[data-testid="stMarkdownContainer"] h1,
        div[data-testid="stExpanderDetails"] div[data-testid="stMarkdownContainer"] h2,
        div[data-testid="stExpanderDetails"] div[data-testid="stMarkdownContainer"] h3,
        div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stMarkdownContainer"] h1,
        div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stMarkdownContainer"] h2,
        div[data-testid="stVerticalBlockBorderWrapper"] div[data-testid="stMarkdownContainer"] h3 {
            color: var(--text-primary);
            letter-spacing: -0.02em;
            margin-top: 1.1rem;
        }

        /* Navigation */
        .nav-brand {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.25rem 0 0.5rem;
        }

        .nav-logo {
            width: 38px;
            height: 38px;
            border-radius: 10px;
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
        }

        .nav-brand-title {
            color: #f8fafc;
            font-weight: 700;
            font-size: 0.95rem;
            letter-spacing: 0.04em;
        }

        .nav-brand-sub {
            color: #94a3b8;
            font-size: 0.72rem;
        }

        .nav-divider {
            height: 1px;
            background: rgba(255,255,255,0.08);
            margin: 1rem 0;
        }

        .nav-user-card {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: var(--radius-sm);
            padding: 0.75rem;
            margin-bottom: 0.75rem;
        }

        .nav-user-label {
            color: #94a3b8;
            font-size: 0.68rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 0.2rem;
        }

        .nav-user-email {
            color: #e2e8f0;
            font-size: 0.82rem;
            font-weight: 500;
            word-break: break-word;
        }

        .sidebar-version {
            color: #64748b;
            font-size: 0.68rem;
            text-align: center;
            padding-top: 1rem;
            margin: 0.5rem 0 0;
        }

        /* Topbar */
        .app-topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 0.9rem 1.25rem;
            margin-bottom: 1.25rem;
            box-shadow: var(--shadow-sm);
        }

        .topbar-left {
            display: flex;
            align-items: center;
            gap: 0.85rem;
        }

        .topbar-logo {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
        }

        .topbar-title {
            font-weight: 700;
            font-size: 0.95rem;
            color: var(--text-primary);
        }

        .topbar-subtitle {
            font-size: 0.75rem;
            color: var(--text-secondary);
        }

        .topbar-right {
            display: flex;
            align-items: center;
            gap: 0.65rem;
        }

        .topbar-pill {
            background: #ecfdf5;
            color: #047857;
            border: 1px solid #a7f3d0;
            border-radius: 999px;
            padding: 0.25rem 0.65rem;
            font-size: 0.72rem;
            font-weight: 600;
        }

        .topbar-user {
            background: var(--bg-muted);
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: 0.3rem 0.75rem;
            font-size: 0.78rem;
            color: var(--text-secondary);
            font-weight: 500;
        }

        /* Hero & features */
        .hero-shell {
            background: linear-gradient(135deg, #0b1220 0%, #1e293b 55%, #1e3a8a 100%);
            border-radius: var(--radius-xl);
            padding: 2rem 2.25rem;
            margin-bottom: 1.25rem;
            box-shadow: var(--shadow-lg);
            position: relative;
            overflow: hidden;
        }

        .hero-shell::after {
            content: "";
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at 85% 15%, rgba(59,130,246,0.35), transparent 40%);
            pointer-events: none;
        }

        .hero-badge {
            display: inline-block;
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.15);
            color: #dbeafe;
            border-radius: 999px;
            padding: 0.3rem 0.75rem;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.04em;
            margin-bottom: 0.85rem;
            position: relative;
            z-index: 1;
        }

        .hero-title {
            color: #f8fafc;
            font-size: clamp(1.5rem, 3vw, 2.1rem);
            font-weight: 700;
            letter-spacing: -0.03em;
            margin: 0 0 0.5rem;
            position: relative;
            z-index: 1;
        }

        .hero-subtitle {
            color: #cbd5e1;
            font-size: 0.95rem;
            max-width: 720px;
            margin: 0;
            position: relative;
            z-index: 1;
        }

        .feature-card {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1.1rem 1.15rem;
            height: 100%;
            box-shadow: var(--shadow-sm);
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }

        .feature-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }

        .feature-title {
            font-weight: 600;
            font-size: 0.92rem;
            color: var(--text-primary);
            margin-bottom: 0.45rem;
        }

        .feature-desc {
            color: var(--text-secondary);
            font-size: 0.82rem;
            line-height: 1.55;
        }

        .section-header {
            margin: 1.5rem 0 0.85rem;
        }

        .section-header-title {
            margin: 0;
            font-size: 1.15rem;
            font-weight: 700;
            letter-spacing: -0.02em;
        }

        .section-header-desc {
            margin: 0.25rem 0 0;
            color: var(--text-secondary);
            font-size: 0.86rem;
        }

        /* Cards & typography */
        .section-label {
            color: var(--text-secondary);
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            margin: 0 0 0.45rem;
        }

        .card-title {
            color: var(--text-primary);
            font-size: 1rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            margin: 0 0 0.75rem;
        }

        .muted-text {
            color: var(--text-secondary);
            font-size: 0.9rem;
        }

        .section-spacer { height: 1.1rem; }
        .section-spacer-sm { height: 0.65rem; }

        /* Risk cards */
        .risk-card {
            border-radius: var(--radius-md);
            padding: 1.6rem 1.5rem;
            text-align: center;
            border: 1px solid;
            box-shadow: var(--shadow-sm);
        }

        .risk-card-level {
            font-size: 2rem;
            font-weight: 700;
            letter-spacing: 0.03em;
            line-height: 1.1;
            margin-bottom: 0.35rem;
        }

        .risk-card-subtitle {
            font-size: 0.88rem;
            font-weight: 500;
            opacity: 0.9;
        }

        .risk-card-high {
            background: linear-gradient(180deg, #fef2f2, #fee2e2);
            color: #b91c1c;
            border-color: #fecaca;
        }

        .risk-card-medium {
            background: linear-gradient(180deg, #fffbeb, #fef3c7);
            color: #b45309;
            border-color: #fde68a;
        }

        .risk-card-low {
            background: linear-gradient(180deg, #ecfdf5, #d1fae5);
            color: #047857;
            border-color: #a7f3d0;
        }

        .risk-card-unknown {
            background: var(--bg-muted);
            color: #475569;
            border-color: var(--border);
        }

        /* Status & meta */
        .summary-status { display: flex; flex-direction: column; gap: 0.35rem; }

        .status-badge {
            display: inline-block;
            width: fit-content;
            padding: 0.3rem 0.75rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 600;
            border: 1px solid;
        }

        .status-complete {
            background: #ecfdf5;
            color: #047857;
            border-color: #a7f3d0;
        }

        .status-error {
            background: #fef2f2;
            color: #b91c1c;
            border-color: #fecaca;
        }

        .meta-item { margin-bottom: 0.75rem; }

        .meta-label {
            display: block;
            color: var(--text-secondary);
            font-size: 0.68rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.25rem;
        }

        .meta-badge {
            display: inline-block;
            background: var(--bg-muted);
            color: var(--text-primary);
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: 0.28rem 0.7rem;
            font-size: 0.82rem;
            font-weight: 500;
        }

        .similarity-value {
            color: var(--accent);
            font-size: 0.92rem;
            font-weight: 700;
            margin: 0.35rem 0 0;
        }

        /* Streamlit components */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--bg-surface);
            border-color: var(--border);
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
            padding: 0.5rem 0.75rem 0.75rem;
        }

        div[data-testid="stExpander"] {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            margin-bottom: 0.6rem;
            box-shadow: var(--shadow-sm);
            transition: box-shadow 0.18s ease;
        }

        div[data-testid="stExpander"]:hover {
            box-shadow: var(--shadow-md);
        }

        div[data-testid="stExpander"] summary {
            font-weight: 600;
            font-size: 0.9rem;
            color: var(--text-primary);
        }

        div[data-testid="stMetric"] {
            background: var(--bg-muted);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 0.8rem 0.95rem;
        }

        div[data-testid="stMetricLabel"] {
            font-size: 0.72rem;
            color: var(--text-secondary);
            font-weight: 600;
        }

        div[data-testid="stMetricValue"] {
            font-size: 1.15rem;
            color: var(--text-primary);
            font-weight: 700;
        }

        .stTextArea textarea {
            border-radius: var(--radius-sm);
            border-color: var(--border);
            font-size: 0.92rem;
        }

        .stTextArea textarea:focus {
            border-color: var(--accent);
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
        }

        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            color: white;
            border: none;
            border-radius: var(--radius-sm);
            font-weight: 600;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.28);
            transition: all 0.18s ease;
        }

        .stButton > button[kind="primary"]:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 18px rgba(37, 99, 235, 0.34);
        }

        .stButton > button:not([kind="primary"]) {
            border-radius: var(--radius-sm);
            border-color: var(--border);
            font-weight: 600;
        }

        /* Premium tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.35rem;
            background: var(--bg-muted);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 0.35rem;
            margin-bottom: 0.5rem;
        }

        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border-radius: var(--radius-sm);
            padding: 0.55rem 1.1rem;
            font-weight: 600;
            font-size: 0.84rem;
            color: var(--text-secondary);
            transition: all 0.18s ease;
        }

        .stTabs [aria-selected="true"] {
            background: var(--bg-surface);
            color: var(--accent);
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--border);
        }

        .stTabs [data-baseweb="tab-panel"] {
            padding-top: 0.75rem;
        }

        /* Progress */
        .progress-panel {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1rem 1.15rem;
            box-shadow: var(--shadow-sm);
            margin: 0.75rem 0 1rem;
        }

        .progress-step {
            display: flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.32rem 0;
            color: var(--text-secondary);
            font-size: 0.84rem;
        }

        .progress-step.active {
            color: var(--accent);
            font-weight: 600;
        }

        .progress-step.done {
            color: var(--success);
        }

        div[data-testid="stProgressBar"] > div > div {
            background: linear-gradient(90deg, #2563eb, #3b82f6);
            border-radius: 999px;
        }

        /* Analytics */
        .analytics-kpi {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1rem 1.05rem;
            box-shadow: var(--shadow-sm);
            min-height: 112px;
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }

        .analytics-kpi:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }

        .analytics-kpi-icon { font-size: 1rem; margin-bottom: 0.35rem; }
        .analytics-kpi-label {
            color: var(--text-secondary);
            font-size: 0.7rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.35rem;
        }
        .analytics-kpi-value {
            color: var(--text-primary);
            font-size: 1.2rem;
            font-weight: 700;
            line-height: 1.25;
        }

        .theme-badge-row { display: flex; flex-wrap: wrap; gap: 0.45rem; }

        .theme-badge {
            display: inline-block;
            background: var(--accent-soft);
            color: var(--accent-dark);
            border: 1px solid #bfdbfe;
            border-radius: 999px;
            padding: 0.32rem 0.8rem;
            font-size: 0.8rem;
            font-weight: 600;
        }

        .risk-matrix {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
        }

        .risk-matrix th {
            text-align: left;
            color: var(--text-secondary);
            font-size: 0.68rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 0.7rem 0.75rem;
            border-bottom: 1px solid var(--border);
            background: var(--bg-muted);
        }

        .risk-matrix td {
            padding: 0.8rem 0.75rem;
            border-bottom: 1px solid #f1f5f9;
            color: var(--text-primary);
        }

        .matrix-high { color: #dc2626; font-weight: 700; }
        .matrix-medium { color: #d97706; font-weight: 700; }
        .matrix-low { color: #ca8a04; font-weight: 700; }

        .insights-list {
            margin: 0;
            padding-left: 1.15rem;
            color: #334155;
        }

        .insights-list li {
            margin-bottom: 0.55rem;
            line-height: 1.6;
        }

        .results-shell {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 1rem 1.15rem 1.25rem;
            box-shadow: var(--shadow-sm);
        }

        @media (max-width: 768px) {
            .block-container { padding-left: 0.85rem; padding-right: 0.85rem; }
            .hero-shell { padding: 1.35rem 1.25rem; }
            .app-topbar { flex-direction: column; align-items: flex-start; gap: 0.65rem; }
            .topbar-right { width: 100%; justify-content: flex-start; flex-wrap: wrap; }
            .risk-card-level { font-size: 1.55rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
