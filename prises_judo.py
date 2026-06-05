from html import escape
import json
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Prises de judo",
    page_icon="🥋",
    layout="wide",
)

DATA_PATH = Path(__file__).with_name("techniques.json")
JUDO_TECHNIQUES = json.loads(DATA_PATH.read_text(encoding="utf-8"))

def extract_youtube_id(url: str) -> str:
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0].split("&")[0]
    if "/shorts/" in url:
        return url.split("/shorts/")[1].split("?")[0].split("&")[0]
    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    return url


st.markdown(
    """
    <style>
        :root {
            --ink: #111827;
            --muted: #4b5563;
            --line: rgba(17, 24, 39, 0.12);
            --panel: rgba(255, 255, 255, 0.92);
            --surface: #f4f6f8;
            --accent: #1f4b6e;
            --accent-soft: rgba(31, 75, 110, 0.10);
        }

        .stApp {
            background:
                linear-gradient(180deg, rgba(255, 255, 255, 0.72), rgba(255, 255, 255, 0.72)),
                linear-gradient(180deg, #f7f8fa 0%, #eef2f6 100%);
            color: var(--ink);
        }

        .block-container {
            max-width: 820px;
            padding: 0.85rem 1rem 2.25rem;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"] {
            display: none;
        }

        .tech-panel {
            border: 1px solid var(--line);
            border-radius: 8px;
            background: var(--panel);
            box-shadow: 0 12px 32px rgba(15, 23, 42, 0.08);
            margin-top: 0.75rem;
            padding: 1rem;
        }

        .video-wrapper {
            position: relative;
            width: 100%;
            aspect-ratio: 16 / 9;
            overflow: hidden;
            background: #0f172a;
            border-radius: 8px;
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.14);
        }

        .video-frame {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            border: 0;
        }

        .app-title {
            display: none;
            align-items: center;
            gap: 0.5rem;
            margin: 0 0 0.4rem;
            color: var(--ink);
            font-size: 1.4rem;
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: 0;
        }

        .app-title-mark {
            display: inline-grid;
            place-items: center;
            flex: 0 0 auto;
            width: 2.7rem;
            height: 2.7rem;
            border: 1px solid var(--line);
            border-radius: 999px;
            background: var(--panel);
            box-shadow: 0 6px 16px rgba(15, 23, 42, 0.08);
            line-height: 1;
        }

        .app-title-mark svg {
            width: 1.84rem;
            height: 1.84rem;
            display: block;
        }

        @media (orientation: portrait) {
            .app-title {
                display: inline-flex;
            }
        }

        .tech-description {
            display: none;
            margin: 0 0 0.75rem;
            color: var(--muted);
            font-size: 0.95rem;
            line-height: 1.55;
        }

        @media (orientation: portrait) {
            .tech-description {
                display: block;
            }
        }

        .stSelectbox div[data-baseweb="select"] > div {
            min-height: 2.45rem;
            border-radius: 8px;
            border-color: rgba(17, 24, 39, 0.14);
            background: rgba(255, 255, 255, 0.96);
            box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);
        }

        .stSelectbox div[data-baseweb="select"] [role="combobox"],
        .stSelectbox div[data-baseweb="select"] span {
            white-space: nowrap !important;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .stSelectbox div[data-baseweb="select"] span,
        .stSelectbox div[data-baseweb="select"] input,
        .stSelectbox div[data-baseweb="select"] div,
        .stSelectbox div[data-baseweb="select"] svg {
            color: var(--ink) !important;
            fill: var(--ink) !important;
        }

        .stSelectbox div[data-baseweb="select"] input::placeholder {
            color: rgba(17, 24, 39, 0.56) !important;
        }

        .stSelectbox [data-baseweb="select"] [aria-selected="true"],
        .stSelectbox [data-baseweb="select"] [data-baseweb="tag"] {
            color: var(--ink) !important;
        }

        .stSelectbox div[data-baseweb="select"] {
            min-height: 2.45rem;
        }

        .stSelectbox input {
            caret-color: transparent;
        }

        .stSelectbox {
            margin-bottom: 0;
        }

        .stButton {
            display: none !important;
        }

        .stVerticalBlock {
            padding: 0 !important;
        }

        [data-testid="stElementContainer"]:has(iframe[height="0"]) {
            display: none;
        }

        @media (orientation: landscape) {
            .block-container {
                max-width: 100% !important;
                padding: 0 !important;
            }

            [data-testid="stElementContainer"]:has(.app-title),
            [data-testid="stHorizontalBlock"]:has(.stSelectbox) {
                display: none !important;
            }

            .tech-panel {
                margin: 0;
                padding: 0;
                border: none;
                border-radius: 0;
                background: transparent;
                box-shadow: none;
            }

            .tech-panel .tech-description {
                display: none;
            }

            .video-wrapper {
                position: fixed !important;
                inset: 0 !important;
                aspect-ratio: auto !important;
                width: 100vw !important;
                height: 100vh !important;
                height: 100dvh !important;
                max-width: 100vw !important;
                margin: 0 !important;
                border-radius: 0 !important;
                box-shadow: none !important;
                z-index: 9000 !important;
                background: #000 !important;
            }

            .st-key-landscape_previous_button,
            .st-key-landscape_next_button {
                display: block !important;
                position: fixed;
                right: 1.5rem;
                z-index: 9999;
            }

            .st-key-landscape_previous_button {
                top: calc(50% - 4.25rem);
            }

            .st-key-landscape_next_button {
                top: calc(50% + 0.75rem);
            }

            .st-key-landscape_previous_button .stButton,
            .st-key-landscape_next_button .stButton {
                display: block !important;
            }

            .st-key-landscape_previous_button button,
            .st-key-landscape_next_button button {
                width: 3.5rem;
                height: 3.5rem;
                min-width: 3.5rem;
                padding: 0;
                background: rgba(255, 255, 255, 0.94) !important;
                backdrop-filter: blur(4px);
                border: 0;
                border-radius: 999px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
                font-size: 1.6rem;
                line-height: 1;
                color: var(--ink) !important;
                opacity: 1 !important;
                transform: none !important;
                -webkit-tap-highlight-color: transparent;
            }

            .st-key-landscape_previous_button button:hover,
            .st-key-landscape_next_button button:hover,
            .st-key-landscape_previous_button button:focus,
            .st-key-landscape_next_button button:focus,
            .st-key-landscape_previous_button button:focus-visible,
            .st-key-landscape_next_button button:focus-visible,
            .st-key-landscape_previous_button button:active,
            .st-key-landscape_next_button button:active,
            .st-key-landscape_previous_button button:disabled,
            .st-key-landscape_next_button button:disabled {
                background: rgba(255, 255, 255, 0.98) !important;
                color: var(--ink) !important;
                opacity: 1 !important;
                border: 0 !important;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
                transform: none !important;
            }
        }

        @media (max-width: 480px) and (orientation: portrait) {
            .block-container {
                padding: 0.7rem 0.65rem 2rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

categories = list(dict.fromkeys(technique["category"] for technique in JUDO_TECHNIQUES))


def get_category_techniques(category: str) -> list[dict[str, str]]:
    return sorted(
        [
            technique
            for technique in JUDO_TECHNIQUES
            if technique["category"] == category
        ],
        key=lambda technique: format_technique_name(technique["name"]),
    )


def format_technique_name(name: str) -> str:
    return name.replace("-", " ")


def reset_selected_name() -> None:
    category_techniques = get_category_techniques(st.session_state.selected_category)
    st.session_state.selected_name = category_techniques[0]["name"]


def select_technique(name: str) -> None:
    st.session_state.selected_name = name


def prevent_mobile_keyboard_on_selectboxes() -> None:
    st.html(
        """
        <script>
            function lockSelectInputs() {
                const inputs = window.parent.document.querySelectorAll(
                    '[data-baseweb="select"] input'
                );

                inputs.forEach((input) => {
                    input.setAttribute('readonly', 'readonly');
                    input.setAttribute('inputmode', 'none');
                    input.setAttribute('autocomplete', 'off');
                });
            }

            lockSelectInputs();
            window.parent.setTimeout(lockSelectInputs, 250);
            window.parent.setTimeout(lockSelectInputs, 750);

            const observer = new MutationObserver(lockSelectInputs);
            observer.observe(window.parent.document.body, {
                childList: true,
                subtree: true
            });
        </script>
        """
    )


if "selected_category" not in st.session_state:
    st.session_state.selected_category = categories[0]

category_techniques = get_category_techniques(st.session_state.selected_category)
technique_names = [technique["name"] for technique in category_techniques]

if (
    "selected_name" not in st.session_state
    or st.session_state.selected_name not in technique_names
):
    st.session_state.selected_name = technique_names[0]

current_index = technique_names.index(st.session_state.selected_name)
previous_index = (current_index - 1) % len(technique_names)
next_index = (current_index + 1) % len(technique_names)

prevent_mobile_keyboard_on_selectboxes()

st.markdown(
    """
    <h1 class="app-title">
        <span class="app-title-mark" aria-hidden="true">
            <svg viewBox="0 0 24 24" role="img" aria-hidden="true">
                <polygon
                    points="12,2.2 16.9,4.2 21.8,9.1 21.8,14.9 16.9,19.8 12,21.8 7.1,19.8 2.2,14.9 2.2,9.1 7.1,4.2"
                    fill="#ffffff"
                    stroke="currentColor"
                    stroke-width="1.2"
                />
                <circle cx="12" cy="12" r="3.9" fill="#d01818" />
            </svg>
        </span>
        <span>Prises de Judo</span>
    </h1>
    """,
    unsafe_allow_html=True,
)

category_column, technique_column = st.columns([0.36, 0.64], gap="small")

with category_column:
    selected_category = st.selectbox(
        "Catégorie",
        categories,
        index=categories.index(st.session_state.selected_category),
        label_visibility="collapsed",
        key="selected_category",
        on_change=reset_selected_name,
    )

category_techniques = get_category_techniques(selected_category)
technique_names = [technique["name"] for technique in category_techniques]

with technique_column:
    selected_name = st.selectbox(
        "Prise",
        technique_names,
        index=technique_names.index(st.session_state.selected_name),
        format_func=format_technique_name,
        label_visibility="collapsed",
        key="selected_name",
    )

selected_technique = category_techniques[technique_names.index(selected_name)]

video_id = extract_youtube_id(selected_technique["youtube"])
embed_url = f"https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1"

st.markdown(
    f"""
    <div class="tech-panel">
        <p class="tech-description">{escape(selected_technique["description"])}</p>
        <div class="video-wrapper">
            <iframe id="video-{video_id}" key="{video_id}" class="video-frame" src="{escape(embed_url)}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.button(
    "←",
    on_click=select_technique,
    args=(technique_names[previous_index],),
    help="Technique précédente",
    key="landscape_previous_button",
)
st.button(
    "→",
    on_click=select_technique,
    args=(technique_names[next_index],),
    help="Technique suivante",
    key="landscape_next_button",
)
