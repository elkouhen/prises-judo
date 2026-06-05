from unittest import TestCase, main

from judo_utils import extract_youtube_id


class ExtractYoutubeIdTest(TestCase):
    def test_extracts_watch_id_when_v_is_not_first_query_parameter(self) -> None:
        self.assertEqual(
            extract_youtube_id("https://www.youtube.com/watch?feature=shared&v=abc123"),
            "abc123",
        )

    def test_extracts_supported_youtube_url_forms(self) -> None:
        cases = {
            "https://www.youtube.com/watch?v=watch123&list=playlist": "watch123",
            "https://youtu.be/short123?si=share": "short123",
            "https://www.youtube.com/shorts/shorts123?feature=share": "shorts123",
        }

        for url, expected_id in cases.items():
            with self.subTest(url=url):
                self.assertEqual(extract_youtube_id(url), expected_id)


if __name__ == "__main__":
    main()
