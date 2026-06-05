from __future__ import annotations

import os

from playwright.sync_api import expect, sync_playwright


APP_URL = os.environ.get("APP_URL", "http://localhost:8501")
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def assert_mobile_layout() -> None:
    with sync_playwright() as playwright:
        launch_options = {"headless": True}
        if os.path.exists(CHROME_PATH):
            launch_options["executable_path"] = CHROME_PATH

        browser = playwright.chromium.launch(**launch_options)

        try:
            for width, height, is_landscape in (
                (390, 844, False),
                (844, 390, True),
                (667, 375, True),
            ):
                page = browser.new_page(
                    viewport={"width": width, "height": height},
                    is_mobile=True,
                )
                page.goto(APP_URL, wait_until="networkidle", timeout=15_000)
                page.wait_for_timeout(1_000)

                video = page.locator(".video-wrapper")
                expect(video).to_be_visible()

                next_button = page.locator(
                    ".st-key-landscape_next_button button"
                ).first
                previous_button = page.locator(
                    ".st-key-landscape_previous_button button"
                ).first

                if is_landscape:
                    expect(next_button).to_be_visible()
                    expect(previous_button).to_be_visible()

                    style = next_button.evaluate(
                        """button => ({
                            opacity: getComputedStyle(button).opacity,
                            background: getComputedStyle(button).backgroundColor,
                        })"""
                    )
                    assert style["opacity"] == "1"
                    assert style["background"] != "rgba(0, 0, 0, 0)"
                else:
                    expect(next_button).to_be_hidden()
                    expect(previous_button).to_be_hidden()

                page.close()
        finally:
            browser.close()


if __name__ == "__main__":
    assert_mobile_layout()
