from html import escape

import streamlit as st

st.set_page_config(
    page_title="Prises de judo",
    page_icon="🥋",
    layout="wide",
)

JUDO_TECHNIQUES = [
    {
        "category": "Koshi waza",
        "name": "Uki-goshi",
        "youtube": "https://www.youtube.com/watch?v=bPKwtB4lyOQ",
        "description": "Projection de hanche légère qui fait pivoter l'adversaire autour de la hanche.",
    },
    {
        "category": "Koshi waza",
        "name": "Koshi-guruma",
        "youtube": "https://www.youtube.com/watch?v=SU7Id6uVJ44",
        "description": "Variation de hanche avec prise du cou pour faire basculer l'adversaire en cercle.",
    },
    {
        "category": "Koshi waza",
        "name": "Ushiro-goshi",
        "youtube": "https://www.youtube.com/watch?v=ORIYstuxYT8",
        "description": "Projection arrière de hanche utilisée pour contrer et soulever l'adversaire.",
    },
    {
        "category": "Koshi waza",
        "name": "Hane-goshi",
        "youtube": "https://www.youtube.com/watch?v=M9_7De6A1kk",
        "description": "Projection de hanche avec coup de jambe ascendant pour déséquilibrer et lancer.",
    },
    {
        "category": "Koshi waza",
        "name": "O-goshi",
        "youtube": "https://www.youtube.com/watch?v=yhu1mfy2vJ4",
        "description": "Projection classique de hanche où l'on soulève l'adversaire sur la hanche.",
    },
    {
        "category": "Koshi waza",
        "name": "Sode-tsurikomi-goshi",
        "youtube": "https://www.youtube.com/watch?v=QsmAxpmYLOI",
        "description": "Projection de hanche contrôlée par la manche et l'épaule pour lever et tourner.",
    },
    {
        "category": "Koshi waza",
        "name": "Utsuri-goshi",
        "youtube": "https://www.youtube.com/watch?v=4pQd_bEnlf0",
        "description": "Projection de hanche où l'on déplace l'adversaire d'une hanche à l'autre.",
    },
    {
        "category": "Koshi waza",
        "name": "Tsurikomi-goshi",
        "youtube": "https://www.youtube.com/watch?v=McfzA0yRVt4",
        "description": "Projection de hanche par levage et traction de la manche pour amener l'adversaire au sol.",
    },
    {
        "category": "Koshi waza",
        "name": "Kubi-nage",
        "youtube": "https://www.youtube.com/watch?v=F-4fyNwx52w",
        "description": "Projection de hanche utilisant la tête ou le cou pour diriger l'adversaire.",
    },
    {
        "category": "Koshi waza",
        "name": "Harai-goshi",
        "youtube": "https://www.youtube.com/watch?v=qTo8HlAAkOo",
        "description": "Projection de hanche avec balayage de jambe pour balayer l'adversaire sur le côté.",
    },
    {
        "category": "Te waza",
        "name": "Uki-otoshi",
        "youtube": "https://www.youtube.com/watch?v=6H5tmncOY4Q",
        "description": "Projection de main qui fait tomber l'adversaire en utilisant son élan vers l'avant.",
    },
    {
        "category": "Te waza",
        "name": "Seoi-otoshi",
        "youtube": "https://www.youtube.com/watch?v=vu1TMVNnq34",
        "description": "Projection d'épaule où l'on fait glisser l'adversaire par-dessus l'épaule.",
    },
    {
        "category": "Te waza",
        "name": "Ippon-seoi-nage",
        "youtube": "https://www.youtube.com/watch?v=FQnOlCxo4oI",
        "description": "Projection d'épaule à un bras, rapide et très technique.",
    },
    {
        "category": "Te waza",
        "name": "Tai-otoshi",
        "youtube": "https://www.youtube.com/watch?v=4x6S3Q-Ktv8",
        "description": "Projection au corps coupé avec blocage de jambe pour faire tomber l'adversaire.",
    },
    {
        "category": "Te waza",
        "name": "Kata-guruma",
        "youtube": "https://www.youtube.com/watch?v=cnHRhSy8yi4",
        "description": "Projection en portant l'adversaire sur l'épaule avant de le déposer au sol.",
    },
    {
        "category": "Te waza",
        "name": "Te-guruma",
        "youtube": "https://www.youtube.com/watch?v=P-4HUgB_rK4",
        "description": "Projection en saisissant la jambe pour lever et tourner l'adversaire.",
    },
    {
        "category": "Te waza",
        "name": "Morote-gari",
        "youtube": "https://www.youtube.com/watch?v=BHLQS4K85bs",
        "description": "Double attaque de jambes en saisissant les deux jambes de l'adversaire.",
    },
    {
        "category": "Te waza",
        "name": "Morote-seoi-nage",
        "youtube": "https://www.youtube.com/watch?v=zIq0xI0ogxk",
        "description": "Projection d'épaule renforcée par une prise des deux mains.",
    },
    {
        "category": "Te waza",
        "name": "Kibisu-gaeshi",
        "youtube": "https://www.youtube.com/watch?v=tJylJYfBliA",
        "description": "Renversement rapide en attrapant le talon de l'adversaire.",
    },
    {
        "category": "Te waza",
        "name": "Kuchiki-taoshi",
        "youtube": "https://www.youtube.com/watch?v=ZNL47q1aJNY",
        "description": "Projection de saisie de jambe pour faire tomber l'adversaire sur le côté.",
    },
    {
        "category": "Te waza",
        "name": "Eri-seoi-nage",
        "youtube": "https://www.youtube.com/watch?v=vOpRNSg1O14",
        "description": "Projection d'épaule où l'on utilise le col de la veste pour diriger l'adversaire.",
    },
    {
        "category": "Ashi waza",
        "name": "O-soto-gari",
        "youtube": "https://www.youtube.com/watch?v=c-A_nP7mKAc",
        "description": "Balayage extérieur de la jambe pour faire tomber l'adversaire vers l'arrière.",
    },
    {
        "category": "Ashi waza",
        "name": "Ko-soto-gari",
        "youtube": "https://www.youtube.com/watch?v=jeQ541ScLB4",
        "description": "Petit balayage extérieur pour déséquilibrer l'adversaire vers l'arrière.",
    },
    {
        "category": "Ashi waza",
        "name": "Ko-uchi-gari",
        "youtube": "https://www.youtube.com/watch?v=3Jb3tZvr9Ng",
        "description": "Balayage intérieur sur la jambe pour faire chuter l'adversaire.",
    },
    {
        "category": "Ashi waza",
        "name": "Sasae-tsurikomi-ashi",
        "youtube": "https://www.youtube.com/watch?v=699i--pvYmE",
        "description": "Blocage de la cheville pour empêcher la jambe de l'adversaire et le faire tomber.",
    },
    {
        "category": "Ashi waza",
        "name": "O-uchi-gari",
        "youtube": "https://www.youtube.com/watch?v=0itJFhV9pDQ",
        "description": "Balayage intérieur de la jambe pour tirer l'adversaire vers l'arrière.",
    },
    {
        "category": "Ashi waza",
        "name": "Uchi-mata",
        "youtube": "https://www.youtube.com/watch?v=iUpSu5J-bgw",
        "description": "Projection de cuisse qui élève l'adversaire et le fait basculer sur le côté.",
    },
    {
        "category": "Ashi waza",
        "name": "Ko-soto-gake",
        "youtube": "https://www.youtube.com/watch?v=8b6kY4s4zH4",
        "description": "Crochetage de la jambe extérieure pour déstabiliser et renverser l'adversaire.",
    },
    {
        "category": "Ashi waza",
        "name": "Osoto-otoshi",
        "youtube": "https://www.youtube.com/watch?v=2DsVvDw7b8g",
        "description": "Projection de l'extérieur du pied en utilisant le déséquilibre vers l'arrière.",
    },
    {
        "category": "Ashi waza",
        "name": "Okuri-ashi-barai",
        "youtube": "https://www.youtube.com/watch?v=nw1ZdRjrdRI",
        "description": "Balayage des deux jambes adverses en déplaçant le pied du même côté.",
    },
    {
        "category": "Ashi waza",
        "name": "Hiza-guruma",
        "youtube": "https://www.youtube.com/watch?v=JPJx9-oAVns",
        "description": "Blocage du genou pour faire basculer l'adversaire par rotation.",
    },
    {
        "category": "Ashi waza",
        "name": "De-ashi-harai",
        "youtube": "https://www.youtube.com/watch?v=4BUUvqxi_Kk",
        "description": "Balayage du pied avancé au moment du déplacement de l'adversaire.",
    },
    {
        "category": "Ashi waza",
        "name": "Ashi-guruma",
        "youtube": "https://www.youtube.com/watch?v=ROeayhvom9U",
        "description": "Projection qui utilise la jambe comme pivot pour tourner l'adversaire.",
    },
    {
        "category": "Ashi waza",
        "name": "Harai-tsurikomi-ashi",
        "youtube": "https://www.youtube.com/watch?v=gGPXvWL8VbE",
        "description": "Balayage combiné avec levage de la manche pour déséquilibrer et jeter.",
    },
    {
        "category": "Sutemi waza",
        "name": "Tani otoshi",
        "youtube": "https://www.youtube.com/watch?v=3b9Me3Fohpk",
        "description": "Projection où l'on se laisse tomber en arrière pour tirer l'adversaire au sol.",
    },
    {
        "category": "Sutemi waza",
        "name": "Yoko-guruma",
        "youtube": "https://www.youtube.com/watch?v=MehP6I5cY2c",
        "description": "Projection latérale où l'on bascule l'adversaire en se couchant sur le côté.",
    },
    {
        "category": "Sutemi waza",
        "name": "Tomoe-nage",
        "youtube": "https://www.youtube.com/watch?v=880WbHvHv6A",
        "description": "Projection en cercle effectuée en tombant sur le dos et en poussant avec le pied.",
    },
    {
        "category": "Sutemi waza",
        "name": "Sumi-gaeshi",
        "youtube": "https://www.youtube.com/watch?v=5VhduA5xkbA",
        "description": "Projection en se laissant tomber en arrière pour faire pivoter l'adversaire.",
    },
    {
        "category": "Sutemi waza",
        "name": "Soto-maki-komi",
        "youtube": "https://www.youtube.com/watch?v=bWG9O1BVKtQ",
        "description": "Projection circulaire en tournant l'adversaire autour de son propre corps.",
    },
    {
        "category": "Sutemi waza",
        "name": "Ura-nage",
        "youtube": "https://www.youtube.com/watch?v=Fgi9b8DJ5sQ",
        "description": "Projection arrière en soulevant l'adversaire avec le dos et en le posant au sol.",
    },
    {
        "category": "Osaekomi",
        "name": "Hon-gesa-gatame",
        "youtube": "https://www.youtube.com/watch?v=NDaQuJOFBYk",
        "description": "Immobilisation de base en position latérale avec contrôle du buste.",
    },
    {
        "category": "Osaekomi",
        "name": "Yoko-shiho-gatame",
        "youtube": "https://www.youtube.com/watch?v=TT7XJVSEQxA",
        "description": "Immobilisation latérale couvrante qui contrôle la tête et les épaules.",
    },
    {
        "category": "Osaekomi",
        "name": "Kuzure-gesa-gatame",
        "youtube": "https://www.youtube.com/watch?v=Q2fb9jaoUFQ",
        "description": "Variation du gésa-gatame avec une prise plus lâche sur la tête.",
    },
    {
        "category": "Osaekomi",
        "name": "Kami-shiho-gatame",
        "youtube": "https://www.youtube.com/watch?v=HFuMjOv0WN8",
        "description": "Immobilisation en haut du corps avec contrôle des épaules adverses.",
    },
    {
        "category": "Osaekomi",
        "name": "Tate-shiho-gatame",
        "youtube": "https://www.youtube.com/watch?v=55-rFmBx53g",
        "description": "Immobilisation montant, assis sur le buste de l'adversaire.",
    },
    {
        "category": "Osaekomi",
        "name": "Kata-gatame",
        "youtube": "https://www.youtube.com/watch?v=zQR3IOXxO_Q",
        "description": "Immobilisation en utilisant le bras et l'épaule pour comprimer le cou.",
    },
    {
        "category": "Osaekomi",
        "name": "Kuzure-kami-shiho-gatame",
        "youtube": "https://www.youtube.com/watch?v=YUrogQWdwiY",
        "description": "Variation du kami-shiho-gatame avec une prise modifiée pour stabiliser.",
    },
    {
        "category": "Osaekomi",
        "name": "Ushiro-gesa-gatame",
        "youtube": "https://www.youtube.com/watch?v=SBapox2M2dE",
        "description": "Immobilisation arrière du gésa-gatame avec un contrôle depuis l'arrière.",
    },
    {
        "category": "Osaekomi",
        "name": "Makura-gesa-gatame",
        "youtube": "https://www.youtube.com/shorts/IqTFKnS9yH8",
        "description": "Immobilisation avec la tête de l'adversaire encadrée entre les jambes.",
    },
    {
        "category": "Shime waza",
        "name": "Gyaku-juji-jime",
        "youtube": "https://www.youtube.com/watch?v=t3tQriIPdlI",
        "description": "Étranglement croisé utilisant les deux avant-bras sur le col.",
    },
    {
        "category": "Shime waza",
        "name": "Sankaku-jime",
        "youtube": "https://www.youtube.com/watch?v=lq1CUBRAm7s",
        "description": "Étranglement en triangle créé avec les jambes autour du cou et du bras.",
    },
    {
        "category": "Shime waza",
        "name": "Nami-juji-jime",
        "youtube": "https://www.youtube.com/watch?v=k2cHry9HByQ",
        "description": "Étranglement croisé classique en utilisant le revers de la veste.",
    },
    {
        "category": "Shime waza",
        "name": "Kata-ha-jime",
        "youtube": "https://www.youtube.com/watch?v=yaTGgRjnwB8",
        "description": "Étranglement d'un seul côté avec une prise du revers et du cou.",
    },
    {
        "category": "Shime waza",
        "name": "Kata-juji-jime",
        "youtube": "https://www.youtube.com/watch?v=3VZVUAmiMD8",
        "description": "Étranglement croisé serré utilisant une main sur le revers et l'autre sur la nuque.",
    },
    {
        "category": "Shime waza",
        "name": "Kata-te-jime",
        "youtube": "https://www.youtube.com/watch?v=cHeIs-fSqwE",
        "description": "Étranglement à une main appliqué depuis la position de contrôle frontal.",
    },
    {
        "category": "Shime waza",
        "name": "Hadaka-jime",
        "youtube": "https://www.youtube.com/watch?v=9f0n8jez7iA",
        "description": "Étranglement sans prise du col, appliqué avec les bras autour du cou.",
    },
    {
        "category": "Shime waza",
        "name": "Okuri-eri-jime",
        "youtube": "https://www.youtube.com/watch?v=EiqyoVcIAi8",
        "description": "Étranglement avec une main qui tire le revers et l'autre qui contrôle le cou.",
    },
    {
        "category": "Kansetsu waza",
        "name": "Ude garami",
        "youtube": "https://www.youtube.com/watch?v=AIlTvZb4RlE",
        "description": "Clef de bras en torsion pour contrôler le coude et l'épaule.",
    },
    {
        "category": "Kansetsu waza",
        "name": "Ude-hishigi-hara-gatame",
        "youtube": "https://www.youtube.com/watch?v=ZzEycg8R_9M",
        "description": "Clef de bras au sol avec pression sur l'avant-bras et le biceps.",
    },
    {
        "category": "Kansetsu waza",
        "name": "Ude-hishigi-juji-gatame",
        "youtube": "https://www.youtube.com/watch?v=OWgSOlCuMXw",
        "description": "Clef de bras en croix classique appliquée sur l'articulation du coude.",
    },
    {
        "category": "Kansetsu waza",
        "name": "Ude-hishigi-ude-gatame",
        "youtube": "https://www.youtube.com/watch?v=SBf0aTma1VI",
        "description": "Immobilisation de bras droite avec pression sur l'articulation du coude.",
    },
    {
        "category": "Kansetsu waza",
        "name": "Ude-hishigi-hiza-gatame",
        "youtube": "https://www.youtube.com/watch?v=H2HtAJdiJcE",
        "description": "Clef de bras utilisant le genou comme point de levier.",
    },
    {
        "category": "Kansetsu waza",
        "name": "Ude-hishigi-waki-gatame",
        "youtube": "https://www.youtube.com/watch?v=8F5p1zuJRG0",
        "description": "Clef de bras appliquée au niveau de l'aisselle pour contrôler le coude.",
    },
    {
        "category": "Kansetsu waza",
        "name": "Hiza-gatame",
        "youtube": "https://www.youtube.com/watch?v=H7VXS0cvGKU",
        "description": "Clef de jambe ou de genou utilisée pour immobiliser et contrôler le bas du corps.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Jodan-naname-shuto",
        "youtube": "https://www.youtube.com/watch?v=rrIaF9mXpiQ",
        "description": "Coupe diagonale de la main haute inspirée des techniques de ju-jitsu.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Mae-dori",
        "youtube": "https://www.youtube.com/watch?v=b7vg80ByuNk",
        "description": "Saisie avant du revers ou du col pour contrôler l'adversaire.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Mae-kubi-dori",
        "youtube": "https://www.youtube.com/watch?v=LYRGJI0Oi9M",
        "description": "Saisie du cou à l'avant pour manipuler la posture de l'adversaire.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Chudan-gyaku-tsuki",
        "youtube": "https://www.youtube.com/watch?v=T1lFQA92jYo",
        "description": "Frappe médiane inversée inspirée des techniques de ju-jitsu.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Eri-dori",
        "youtube": "https://www.youtube.com/watch?v=obPFgYk1HZA",
        "description": "Saisie du revers pour préparer une projection ou une immobilisation.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Yoko-dori",
        "youtube": "https://www.youtube.com/watch?v=-lCkfc-mSEk",
        "description": "Saisie latérale pour contrôler le corps de l'adversaire.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Yoko-kubi-dori",
        "youtube": "https://www.youtube.com/watch?v=djZcAPJRslY",
        "description": "Saisie latérale du cou pour diriger l'adversaire sur le côté.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Chudan-mawashi-geri",
        "youtube": "https://www.youtube.com/watch?v=aCVXZZYAWlw",
        "description": "Coup de pied circulaire au corps inspiré des techniques de self-défense.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Yoko-sode-dori",
        "youtube": "https://www.youtube.com/watch?v=JvoC4Cmawrw",
        "description": "Saisie du revers sur le côté pour contrôler l'équilibre de l'adversaire.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Chudan-mae-geri-kekomi",
        "youtube": "https://www.youtube.com/watch?v=Z1hf3CPlwRk",
        "description": "Coup de pied frontal direct au corps pour ouvrir la garde.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Jodan-oi-tsuki",
        "youtube": "https://www.youtube.com/watch?v=8YyVT1aKzvI",
        "description": "Direct montant du bras pour toucher la zone haute du torse ou du visage.",
    },
    {
        "category": "Judo jujitsu",
        "name": "Katate-dori",
        "youtube": "https://www.youtube.com/watch?v=auzBXYyp1C4",
        "description": "Saisie d'une main pour diriger et préparer une transition ou une projection.",
    },
]

CATEGORY_DETAILS = {
    "Ashi waza": {"label": "Jambes", "accent": "#2563eb"},
    "Judo jujitsu": {"label": "Self-défense", "accent": "#dc2626"},
    "Kansetsu waza": {"label": "Clés", "accent": "#7c3aed"},
    "Koshi waza": {"label": "Hanches", "accent": "#059669"},
    "Osaekomi": {"label": "Sol", "accent": "#ca8a04"},
    "Shime waza": {"label": "Étranglements", "accent": "#0891b2"},
    "Sutemi waza": {"label": "Sacrifices", "accent": "#ea580c"},
    "Te waza": {"label": "Mains", "accent": "#4f46e5"},
}


def extract_youtube_id(url: str) -> str:
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0].split("&")[0]
    if "/shorts/" in url:
        return url.split("/shorts/")[1].split("?")[0].split("&")[0]
    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    return url


def technique_matches_query(technique: dict[str, str], query: str) -> bool:
    normalized_query = query.strip().lower()
    if not normalized_query:
        return True

    searchable_text = " ".join(
        [
            technique["name"],
            technique["category"],
            technique["description"],
        ]
    ).lower()
    return normalized_query in searchable_text


st.markdown(
    """
    <style>
        :root {
            --ink: #101828;
            --muted: #667085;
            --line: rgba(16, 24, 40, 0.10);
            --panel: rgba(255, 255, 255, 0.92);
            --soft: #f5f7fb;
            --brand: #dc2626;
            --brand-dark: #991b1b;
            --blue: #2563eb;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(220, 38, 38, 0.13), transparent 28rem),
                linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
            color: var(--ink);
        }

        .block-container {
            max-width: 1120px;
            padding: 1rem 1rem 3rem;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"] {
            display: none;
        }

        .hero {
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.72);
            border-radius: 8px;
            padding: 1.1rem;
            background:
                linear-gradient(135deg, rgba(153, 27, 27, 0.95), rgba(16, 24, 40, 0.95)),
                repeating-linear-gradient(45deg, rgba(255,255,255,0.10) 0 1px, transparent 1px 16px);
            box-shadow: 0 18px 50px rgba(16, 24, 40, 0.16);
            color: #ffffff;
        }

        .hero::after {
            content: "";
            position: absolute;
            inset: auto -3rem -5rem auto;
            width: 13rem;
            height: 13rem;
            border: 1.4rem solid rgba(255, 255, 255, 0.10);
            border-radius: 999px;
        }

        .hero-kicker {
            position: relative;
            z-index: 1;
            width: fit-content;
            border: 1px solid rgba(255, 255, 255, 0.28);
            border-radius: 999px;
            padding: 0.35rem 0.65rem;
            background: rgba(255, 255, 255, 0.12);
            font-size: 0.76rem;
            font-weight: 800;
            letter-spacing: 0;
            text-transform: uppercase;
        }

        .app-title {
            position: relative;
            z-index: 1;
            margin: 0.8rem 0 0.35rem;
            font-size: 2.15rem;
            line-height: 1;
            font-weight: 900;
            letter-spacing: 0;
        }

        .app-lead {
            position: relative;
            z-index: 1;
            max-width: 42rem;
            margin: 0;
            color: rgba(255, 255, 255, 0.84);
            font-size: 0.98rem;
            line-height: 1.55;
        }

        .stat-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.55rem;
            margin: 0.8rem 0 0;
        }

        .stat {
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 0.75rem;
            background: var(--panel);
            box-shadow: 0 10px 30px rgba(16, 24, 40, 0.07);
        }

        .stat-value {
            color: var(--ink);
            font-size: 1.15rem;
            font-weight: 900;
            line-height: 1;
        }

        .stat-label {
            margin-top: 0.35rem;
            color: var(--muted);
            font-size: 0.78rem;
            font-weight: 650;
        }

        .section-label {
            margin: 1.1rem 0 0.45rem;
            color: var(--ink);
            font-size: 0.92rem;
            font-weight: 850;
        }

        .detail-card,
        .result-card {
            border: 1px solid var(--line);
            border-radius: 8px;
            background: var(--panel);
            box-shadow: 0 16px 44px rgba(16, 24, 40, 0.09);
        }

        .detail-card {
            overflow: hidden;
            margin-top: 0.9rem;
        }

        .detail-body {
            padding: 1rem;
        }

        .category-chip {
            display: inline-flex;
            align-items: center;
            min-height: 2rem;
            border-radius: 999px;
            padding: 0.3rem 0.7rem;
            background: color-mix(in srgb, var(--chip-color) 13%, white);
            color: var(--chip-color);
            font-size: 0.78rem;
            font-weight: 850;
        }

        .tech-title {
            margin: 0.7rem 0 0.45rem;
            color: var(--ink);
            font-size: 1.75rem;
            line-height: 1.08;
            font-weight: 950;
        }

        .tech-description {
            margin: 0;
            color: #344054;
            font-size: 1rem;
            line-height: 1.65;
        }

        .video-wrapper {
            position: relative;
            width: 100%;
            aspect-ratio: 16 / 9;
            overflow: hidden;
            background: #000000;
        }

        .video-frame {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            border: 0;
        }

        .video-link {
            display: inline-flex;
            margin-top: 0.9rem;
            color: var(--blue);
            font-size: 0.9rem;
            font-weight: 750;
            text-decoration: none;
        }

        .result-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 0.65rem;
            margin-top: 0.55rem;
        }

        .result-card {
            padding: 0.85rem;
        }

        .result-name {
            color: var(--ink);
            font-size: 0.98rem;
            font-weight: 900;
            line-height: 1.25;
        }

        .result-description {
            margin-top: 0.4rem;
            color: var(--muted);
            font-size: 0.84rem;
            line-height: 1.45;
        }

        .stTextInput input,
        .stSelectbox div[data-baseweb="select"] > div {
            min-height: 3rem;
            border-radius: 8px;
            border-color: rgba(16, 24, 40, 0.16);
            background: rgba(255, 255, 255, 0.96);
        }

        div[role="radiogroup"] {
            display: flex;
            gap: 0.45rem;
            overflow-x: auto;
            padding-bottom: 0.15rem;
        }

        div[role="radiogroup"] label {
            min-height: 2.65rem;
            border: 1px solid rgba(16, 24, 40, 0.13);
            border-radius: 999px;
            padding: 0.3rem 0.7rem;
            background: rgba(255, 255, 255, 0.86);
            white-space: nowrap;
        }

        div[role="radiogroup"] label:has(input:checked) {
            border-color: rgba(220, 38, 38, 0.35);
            background: rgba(220, 38, 38, 0.09);
            color: var(--brand-dark);
            font-weight: 800;
        }

        @media (min-width: 760px) {
            .block-container {
                padding-top: 2rem;
            }

            .hero {
                padding: 1.6rem;
            }

            .app-title {
                font-size: 3rem;
            }

            .detail-card {
                margin-top: 1.2rem;
            }
        }

        @media (max-width: 560px) {
            .block-container {
                padding-inline: 0.7rem;
            }

            .hero {
                padding: 1rem;
            }

            .app-title {
                font-size: 1.85rem;
            }

            .stat-row {
                grid-template-columns: 1fr;
            }

            .result-grid {
                grid-template-columns: 1fr;
            }

            .tech-title {
                font-size: 1.45rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

categories = sorted({technique["category"] for technique in JUDO_TECHNIQUES})
category_options = ["Toutes"] + categories

st.markdown(
    f"""
    <section class="hero">
        <div class="hero-kicker">Catalogue vidéo</div>
        <h1 class="app-title">Prises de judo</h1>
        <p class="app-lead">Trouvez une technique, filtrez par famille, puis lancez la vidéo sans quitter l'application. L'écran est pensé pour une consultation rapide sur mobile.</p>
    </section>
    <div class="stat-row">
        <div class="stat">
            <div class="stat-value">{len(JUDO_TECHNIQUES)}</div>
            <div class="stat-label">techniques</div>
        </div>
        <div class="stat">
            <div class="stat-value">{len(categories)}</div>
            <div class="stat-label">familles</div>
        </div>
        <div class="stat">
            <div class="stat-value">vidéo</div>
            <div class="stat-label">démo intégrée</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">Recherche</div>', unsafe_allow_html=True)
query = st.text_input(
    "Rechercher une prise",
    placeholder="Ex. o-soto, hanche, étranglement...",
    label_visibility="collapsed",
)

st.markdown('<div class="section-label">Famille technique</div>', unsafe_allow_html=True)
selected_category = st.radio(
    "Famille technique",
    category_options,
    horizontal=True,
    label_visibility="collapsed",
)

filtered_techniques = [
    technique
    for technique in JUDO_TECHNIQUES
    if (selected_category == "Toutes" or technique["category"] == selected_category)
    and technique_matches_query(technique, query)
]

if not filtered_techniques:
    st.warning("Aucune prise ne correspond à votre recherche. Essayez un autre mot-clé ou une autre famille.")
    st.stop()

filtered_techniques = sorted(
    filtered_techniques,
    key=lambda technique: (technique["category"], technique["name"]),
)

st.markdown(
    f'<div class="section-label">{len(filtered_techniques)} résultat(s)</div>',
    unsafe_allow_html=True,
)

selected_name = st.selectbox(
    "Technique",
    [technique["name"] for technique in filtered_techniques],
    label_visibility="collapsed",
)

preview_cards = []
for technique in filtered_techniques[:6]:
    details = CATEGORY_DETAILS.get(
        technique["category"],
        {"label": technique["category"], "accent": "#475467"},
    )
    preview_cards.append(
        f"""
        <article class="result-card">
            <span class="category-chip" style="--chip-color: {details['accent']}">{escape(details['label'])}</span>
            <div class="result-name">{escape(technique['name'])}</div>
            <div class="result-description">{escape(technique['description'])}</div>
        </article>
        """
    )

st.markdown(
    f'<div class="result-grid">{"".join(preview_cards)}</div>',
    unsafe_allow_html=True,
)

selected_technique = next(
    technique for technique in filtered_techniques if technique["name"] == selected_name
)
selected_details = CATEGORY_DETAILS.get(
    selected_technique["category"],
    {"label": selected_technique["category"], "accent": "#475467"},
)
video_id = extract_youtube_id(selected_technique["youtube"])
embed_url = f"https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1"

st.markdown(
    f"""
    <article class="detail-card">
        <div class="video-wrapper">
            <iframe class="video-frame" src="{escape(embed_url)}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <div class="detail-body">
            <span class="category-chip" style="--chip-color: {selected_details['accent']}">{escape(selected_details['label'])}</span>
            <h2 class="tech-title">{escape(selected_technique['name'])}</h2>
            <p class="tech-description">{escape(selected_technique['description'])}</p>
            <a class="video-link" href="{escape(selected_technique['youtube'])}" target="_blank">Ouvrir sur YouTube</a>
        </div>
    </article>
    """,
    unsafe_allow_html=True,
)
