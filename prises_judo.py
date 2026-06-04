from html import escape
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

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

        .app-header {
            display: flex;
            align-items: center;
            gap: 0.55rem;
            margin: 0 0 0.8rem;
        }

        .title-mark {
            display: grid;
            place-items: center;
            flex: 0 0 auto;
            width: 2.35rem;
            height: 2.35rem;
            border: 1px solid var(--line);
            border-radius: 8px;
            background: var(--panel);
            box-shadow: 0 8px 22px rgba(15, 23, 42, 0.08);
            font-size: 1.15rem;
        }

        .app-title {
            margin: 0 !important;
            color: var(--ink) !important;
            font-size: 1.55rem !important;
            font-weight: 800 !important;
            line-height: 1.05 !important;
            letter-spacing: 0 !important;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            border: 1px solid var(--line);
            border-radius: 8px;
            background: var(--panel);
            box-shadow: 0 12px 32px rgba(15, 23, 42, 0.08);
            margin-top: 0.75rem;
        }

        .tech-title {
            margin: 0;
            color: var(--ink);
            font-size: 1.4rem;
            line-height: 1.1;
            font-weight: 800;
            letter-spacing: 0;
            overflow-wrap: anywhere;
        }

        .tech-link {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            margin-top: 0.3rem;
            color: var(--accent);
            font-size: 0.9rem;
            font-weight: 600;
            text-decoration: none;
            padding: 0.28rem 0.55rem;
            border-radius: 999px;
            background: var(--accent-soft);
            border: 1px solid rgba(31, 75, 110, 0.16);
        }

        .tech-link:hover {
            background: rgba(31, 75, 110, 0.16);
            color: var(--accent);
        }

        .tech-description {
            margin: 0 0 0.75rem;
            color: var(--muted);
            font-size: 0.95rem;
            line-height: 1.55;
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

        .content-layout.is-expanded .tech-description {
            display: none;
        }

        .stSelectbox div[data-baseweb="select"] > div {
            min-height: 2.45rem;
            border-radius: 8px;
            border-color: rgba(17, 24, 39, 0.14);
            background: rgba(255, 255, 255, 0.96);
            box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);
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

        [data-testid="stHorizontalBlock"] {
            align-items: stretch;
            column-gap: 0.35rem;
            display: flex;
            flex-wrap: nowrap !important;
        }

        [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
            min-width: 0 !important;
        }

        .stButton button {
            min-height: 2.35rem;
            width: 100%;
            border-radius: 8px;
            border: 1px solid rgba(31, 75, 110, 0.22);
            background: #ffffff;
            color: var(--ink);
            padding: 0.35rem 0.45rem;
            font-size: 0.86rem;
            font-weight: 700;
            line-height: 1.05;
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.08);
        }

        .stButton button:hover {
            border-color: rgba(31, 75, 110, 0.42);
            background: var(--accent-soft);
            color: var(--ink);
        }

        @media (min-width: 760px) {
            .app-title {
                font-size: 1.8rem !important;
            }

            .title-mark {
                width: 2.65rem;
                height: 2.65rem;
                font-size: 1.35rem;
            }

            .tech-title {
                font-size: 1.7rem;
            }
        }

        @media (orientation: landscape) and (max-height: 560px) and (max-width: 960px) {
            .block-container {
                max-width: 100% !important;
                padding: 0.4rem 0.75rem 0.5rem;
            }

            .app-header {
                gap: 0.4rem;
                margin-bottom: 0.3rem;
            }

            .app-title {
                font-size: 1.2rem !important;
            }

            .title-mark {
                width: 1.9rem;
                height: 1.9rem;
                font-size: 0.95rem;
            }

            [data-testid="stVerticalBlockBorderWrapper"] {
                margin-top: 0.3rem;
            }

            .tech-title {
                font-size: 1.1rem;
            }

            .tech-link {
                font-size: 0.8rem;
                padding: 0.2rem 0.45rem;
                margin-top: 0.2rem;
            }

            .content-layout {
                display: flex;
                gap: 0.75rem;
                align-items: flex-start;
            }

            .tech-description {
                flex: 0 0 32%;
                min-width: 0;
                margin-bottom: 0;
                font-size: 0.88rem;
                line-height: 1.45;
            }

            .video-wrapper {
                flex: 1;
                min-width: 0;
                aspect-ratio: unset;
                height: calc(100dvh - 200px);
            }

            /* Sélecteurs masqués par défaut, visibles si .selectors-visible sur le body */
            [data-testid="stHorizontalBlock"]:has([data-baseweb="select"]) {
                max-height: 200px;
                overflow: hidden;
                opacity: 1;
                transition: max-height 0.25s ease, opacity 0.2s ease, margin 0.25s ease;
            }

            body:not(.selectors-visible) [data-testid="stHorizontalBlock"]:has([data-baseweb="select"]) {
                max-height: 0;
                opacity: 0;
                margin-top: 0 !important;
                margin-bottom: 0 !important;
            }
        }

        #selector-toggle {
            display: none;
            position: fixed;
            top: 0.45rem;
            right: 0.5rem;
            z-index: 9999;
            background: #ffffff;
            border: 1px solid rgba(31, 75, 110, 0.22);
            border-radius: 8px;
            padding: 0.3rem 0.65rem;
            font-size: 0.92rem;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 8px 18px rgba(15, 23, 42, 0.08);
            color: #111827;
            line-height: 1;
        }

        #selector-toggle:hover {
            border-color: rgba(31, 75, 110, 0.42);
            background: rgba(31, 75, 110, 0.10);
        }

        @media (orientation: landscape) and (max-height: 560px) and (max-width: 960px) {
            #selector-toggle {
                display: block;
            }
        }

        @media (max-width: 480px) and (orientation: portrait) {
            .block-container {
                padding: 0.7rem 0.65rem 2rem;
            }

            .app-header {
                gap: 0.5rem;
                margin-bottom: 0.55rem;
            }

            .app-title {
                font-size: 1.42rem !important;
            }

            .title-mark {
                width: 2.2rem;
                height: 2.2rem;
                font-size: 1.05rem;
            }

            .tech-title {
                font-size: 1.2rem;
                line-height: 1.12;
            }

            .tech-description {
                font-size: 0.92rem;
                line-height: 1.5;
            }

            .tech-link {
                font-size: 0.85rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="app-header">
        <div class="title-mark">🥋</div>
        <div>
            <h1 class="app-title">Prises de Judo</h1>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

categories = sorted({technique["category"] for technique in JUDO_TECHNIQUES})


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


def toggle_video_expanded() -> None:
    st.session_state.video_expanded = not st.session_state.get("video_expanded", False)


def prevent_mobile_keyboard_on_selectboxes() -> None:
    components.html(
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
        """,
        height=0,
    )


def add_swipe_navigation_js() -> None:
    components.html(
        """
        <script>
        (function() {
            const doc = window.parent.document;

            function prevBtn() {
                return doc.querySelector('button[title="Technique précédente"]');
            }
            function nextBtn() {
                return doc.querySelector('button[title="Technique suivante"]');
            }

            if (doc._swipeNavBound) return;
            doc._swipeNavBound = true;

            let startX = 0, startY = 0;

            doc.addEventListener('touchstart', function(e) {
                startX = e.touches[0].clientX;
                startY = e.touches[0].clientY;
            }, { passive: true });

            doc.addEventListener('touchend', function(e) {
                const dx = e.changedTouches[0].clientX - startX;
                const dy = e.changedTouches[0].clientY - startY;

                // Ignore short swipes or mostly vertical gestures
                if (Math.abs(dx) < 50 || Math.abs(dy) > Math.abs(dx) * 0.75) return;

                if (dx < 0) { const b = nextBtn(); if (b) b.click(); }
                else        { const b = prevBtn(); if (b) b.click(); }
            }, { passive: true });
        })();
        </script>
        """,
        height=0,
    )


def add_landscape_selectors_toggle_js() -> None:
    components.html(
        """
        <script>
        (function() {
            const doc = window.parent.document;

            if (doc._selectorToggleBound) return;
            doc._selectorToggleBound = true;

            const btn = doc.createElement('button');
            btn.id = 'selector-toggle';
            btn.title = 'Afficher / masquer les filtres';

            function updateLabel() {
                btn.textContent = doc.body.classList.contains('selectors-visible') ? '✕' : '⚙';
            }

            btn.addEventListener('click', function() {
                doc.body.classList.toggle('selectors-visible');
                updateLabel();
            });

            updateLabel();
            doc.body.appendChild(btn);
        })();
        </script>
        """,
        height=0,
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

category_column, technique_column = st.columns(
    [0.36, 0.64],
    gap="small",
)

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
current_index = technique_names.index(st.session_state.selected_name)
previous_index = (current_index - 1) % len(technique_names)
next_index = (current_index + 1) % len(technique_names)

with technique_column:
    selected_name = st.selectbox(
        "Prise",
        technique_names,
        index=current_index,
        format_func=format_technique_name,
        label_visibility="collapsed",
        key="selected_name",
    )

prevent_mobile_keyboard_on_selectboxes()
add_swipe_navigation_js()
add_landscape_selectors_toggle_js()

current_index = technique_names.index(selected_name)
previous_index = (current_index - 1) % len(technique_names)
next_index = (current_index + 1) % len(technique_names)
selected_technique = category_techniques[current_index]
video_id = extract_youtube_id(selected_technique["youtube"])
embed_url = f"https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1"

with st.container(border=True):
    title_column, previous_column, next_column, expand_column = st.columns(
        [0.55, 0.15, 0.15, 0.15], gap="small"
    )

    with title_column:
        st.markdown(
            f'<h2 class="tech-title">{escape(format_technique_name(selected_technique["name"]))}</h2>'
            f'<a class="tech-link" href="{escape(selected_technique["youtube"])}" target="_blank" rel="noopener noreferrer">Ouvrir sur YouTube</a>',
            unsafe_allow_html=True,
        )

    with previous_column:
        st.button(
            "←",
            use_container_width=True,
            on_click=select_technique,
            args=(technique_names[previous_index],),
            help="Technique précédente",
        )

    with next_column:
        st.button(
            "→",
            use_container_width=True,
            on_click=select_technique,
            args=(technique_names[next_index],),
            help="Technique suivante",
        )

    with expand_column:
        is_expanded = st.session_state.get("video_expanded", False)
        st.button(
            "⊟" if is_expanded else "⛶",
            use_container_width=True,
            on_click=toggle_video_expanded,
            help="Réduire la vidéo" if is_expanded else "Agrandir la vidéo",
        )

    content_class = "content-layout is-expanded" if st.session_state.get("video_expanded", False) else "content-layout"
    st.markdown(
        f"""
        <div class="{content_class}">
            <p class="tech-description">{escape(selected_technique["description"])}</p>
            <div class="video-wrapper">
                <iframe class="video-frame" src="{escape(embed_url)}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
