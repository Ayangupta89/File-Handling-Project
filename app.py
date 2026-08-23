"""
File Manager Pro — Streamlit Edition
-------------------------------------
Run with:  streamlit run streamlit_app.py

Requires:  pip install streamlit
"""

import streamlit as st
from pathlib import Path
from datetime import datetime

# ------------------------------------------------------------------ #
#  Page config
# ------------------------------------------------------------------ #
st.set_page_config(
    page_title="File Manager Pro",
    page_icon="📁",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------ #
#  Styling
# ------------------------------------------------------------------ #
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(160deg, #1e1e2e 0%, #181825 100%);
        color: #cdd6f4;
    }

    section[data-testid="stSidebar"] {
        background-color: #181825;
        border-right: 1px solid #313244;
    }

    h1, h2, h3 { color: #cdd6f4 !important; }

    .app-title {
        font-size: 2.1rem;
        font-weight: 700;
        color: #89b4fa;
        margin-bottom: 0;
    }
    .app-subtitle {
        color: #9399b2;
        font-size: 0.95rem;
        margin-top: 0;
        margin-bottom: 1.5rem;
    }

    .card {
        background-color: #242438;
        border: 1px solid #313244;
        border-radius: 14px;
        padding: 1.6rem 1.6rem 1.2rem 1.6rem;
        margin-bottom: 1.2rem;
    }

    div.stButton > button {
        background-color: #89b4fa;
        color: #1e1e2e;
        font-weight: 700;
        border: none;
        border-radius: 8px;
        padding: 0.55rem 1.4rem;
        transition: background-color 0.15s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: #a6c8ff;
        color: #1e1e2e;
    }

    button[kind="secondary"] { background-color: #33334d !important; }

    .stTextInput > div > div > input,
    .stTextArea textarea {
        background-color: #33334d;
        color: #cdd6f4;
        border: 1px solid #45475a;
        border-radius: 8px;
    }

    div[data-testid="stMetric"] {
        background-color: #242438;
        border: 1px solid #313244;
        border-radius: 10px;
        padding: 0.6rem;
    }

    code, pre, .stCodeBlock, .stMarkdown code {
        font-family: 'JetBrains Mono', monospace !important;
    }

    .log-line { font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; padding: 2px 0; }
    .log-success { color: #a6e3a1; }
    .log-error   { color: #f38ba8; }
    .log-info    { color: #89b4fa; }
    .log-warn    { color: #f9e2af; }

    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------ #
#  Session state
# ------------------------------------------------------------------ #
if "log" not in st.session_state:
    st.session_state.log = []


def log(message, level="info"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.log.insert(0, (timestamp, message, level))
    st.session_state.log = st.session_state.log[:12]


# ------------------------------------------------------------------ #
#  Sidebar navigation
# ------------------------------------------------------------------ #
with st.sidebar:
    st.markdown('<p class="app-title">📁 File Manager</p>', unsafe_allow_html=True)
    st.markdown('<p class="app-subtitle">Pro Edition · built with Streamlit</p>', unsafe_allow_html=True)

    page = st.radio(
        "Operation",
        ["➕ Create", "📖 Read", "✏️ Update", "🗑️ Delete"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    cwd_files = [p.name for p in Path(".").iterdir() if p.is_file()]
    st.metric("Files in current folder", len(cwd_files))
    if cwd_files:
        with st.expander("View files"):
            for f in sorted(cwd_files):
                st.write(f"• {f}")

    st.markdown("---")
    st.caption("Python `pathlib` + Streamlit UI")

# ------------------------------------------------------------------ #
#  Main panels
# ------------------------------------------------------------------ #
st.markdown('<p class="app-title">File Operations</p>', unsafe_allow_html=True)
st.markdown('<p class="app-subtitle">Create, read, update, and delete files from the browser.</p>',
            unsafe_allow_html=True)

if page == "➕ Create":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Create a new file")
    name = st.text_input("File name", key="create_name", placeholder="notes.txt")
    content = st.text_area("File content", key="create_content", height=180,
                            placeholder="Type what you want to save…")
    if st.button("Create File", key="create_btn"):
        if not name.strip():
            log("Please enter a file name.", "error")
        else:
            path = Path(name.strip())
            if path.exists():
                log(f"'{name}' already exists.", "error")
            else:
                try:
                    path.write_text(content)
                    log(f"File '{name}' created successfully.", "success")
                    st.success(f"'{name}' created!")
                except Exception as err:
                    log(f"Error: {err}", "error")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📖 Read":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Read a file")
    col1, col2 = st.columns([4, 1])
    with col1:
        name = st.text_input("File name", key="read_name", placeholder="notes.txt",
                              label_visibility="collapsed")
    with col2:
        load = st.button("Load", key="read_btn", use_container_width=True)

    if load:
        if not name.strip():
            log("Please enter a file name.", "error")
        else:
            path = Path(name.strip())
            if not path.exists():
                log(f"No such file: '{name}'.", "error")
                st.error(f"No such file: '{name}'")
            else:
                try:
                    content = path.read_text()
                    st.session_state["read_result"] = content
                    log(f"Loaded '{name}'.", "success")
                except Exception as err:
                    log(f"Error: {err}", "error")

    if "read_result" in st.session_state:
        st.text_area("Content", st.session_state["read_result"], height=250, disabled=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "✏️ Update":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Update a file")
    name = st.text_input("File name", key="update_name", placeholder="notes.txt")
    mode = st.radio("Operation", ["Rename", "Append", "Overwrite"], horizontal=True, key="update_mode")

    if mode == "Rename":
        new_name = st.text_input("New file name", key="update_newname", placeholder="renamed.txt")
    else:
        text = st.text_area(
            "Content to append" if mode == "Append" else "New content (overwrite)",
            key="update_text", height=150,
        )

    if st.button("Apply", key="update_btn"):
        if not name.strip():
            log("Please enter a file name.", "error")
        else:
            path = Path(name.strip())
            if not path.exists():
                log(f"No such file: '{name}'.", "error")
                st.error(f"No such file: '{name}'")
            else:
                try:
                    if mode == "Rename":
                        if not new_name.strip():
                            log("Please enter a new file name.", "error")
                        else:
                            new_path = Path(new_name.strip())
                            if new_path.exists():
                                log(f"'{new_name}' already exists.", "error")
                            else:
                                path.rename(new_path)
                                log(f"Renamed '{name}' to '{new_name}'.", "success")
                                st.success(f"Renamed to '{new_name}'")
                    elif mode == "Append":
                        with open(path, "a") as fs:
                            fs.write("\n" + text)
                        log(f"Appended content to '{name}'.", "success")
                        st.success("Appended!")
                    elif mode == "Overwrite":
                        path.write_text(text)
                        log(f"Overwrote '{name}'.", "success")
                        st.success("Overwritten!")
                except Exception as err:
                    log(f"Error: {err}", "error")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "🗑️ Delete":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Delete a file")
    st.caption("This action cannot be undone.")
    name = st.text_input("File name", key="delete_name", placeholder="notes.txt")
    confirm = st.checkbox("I understand this cannot be undone", key="delete_confirm")
    if st.button("Delete File", key="delete_btn", disabled=not confirm):
        path = Path(name.strip())
        if not name.strip():
            log("Please enter a file name.", "error")
        elif not path.exists():
            log(f"No such file: '{name}'.", "error")
            st.error(f"No such file: '{name}'")
        else:
            try:
                path.unlink()
                log(f"Deleted '{name}'.", "success")
                st.success(f"'{name}' deleted.")
            except Exception as err:
                log(f"Error: {err}", "error")
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------------------------ #
#  Status log
# ------------------------------------------------------------------ #
if st.session_state.log:
    st.markdown("#### Status log")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    for timestamp, message, level in st.session_state.log:
        st.markdown(
            f'<div class="log-line log-{level}">[{timestamp}] {message}</div>',
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)