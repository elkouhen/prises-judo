from urllib.parse import parse_qs, urlparse


def extract_youtube_id(url: str) -> str:
    parsed_url = urlparse(url)

    if parsed_url.netloc.endswith("youtu.be"):
        return parsed_url.path.lstrip("/").split("/")[0]

    if "/shorts/" in parsed_url.path:
        return parsed_url.path.split("/shorts/", 1)[1].split("/", 1)[0]

    video_ids = parse_qs(parsed_url.query).get("v")
    if video_ids:
        return video_ids[0]

    return url
