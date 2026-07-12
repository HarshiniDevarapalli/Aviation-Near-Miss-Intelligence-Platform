"""Report export utilities. Extend here for PDF export."""

import streamlit as st

from ui.constants import EXPORT_FILENAME
from ui.helpers import render_card_title


def build_markdown_export(report: str) -> tuple[str, str]:
    """Return export filename and markdown content."""
    return EXPORT_FILENAME, report


def render_export_actions(report: str) -> None:
    """Render download actions for the generated report."""
    filename, content = build_markdown_export(report)

    with st.container(border=True):
        render_card_title("Export Report")
        col_md, col_pdf = st.columns(2)

        with col_md:
            st.download_button(
                label="Download Markdown",
                data=content,
                file_name=filename,
                mime="text/markdown",
                use_container_width=True,
                key="export_markdown",
            )

        with col_pdf:
            st.button(
                label="Download PDF",
                disabled=True,
                use_container_width=True,
                help="PDF export will be available in a future release.",
                key="export_pdf_placeholder",
            )


# Future PDF export entry point:
# def build_pdf_export(report: str) -> bytes:
#     raise NotImplementedError("PDF export is not yet available.")
