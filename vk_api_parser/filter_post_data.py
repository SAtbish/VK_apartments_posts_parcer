import re
from typing import Any


def filter_post_data(
        post_data: dict[str | Any],
        patterns: list[str],
        restricted_words: list[str]
) -> bool:
    post_text = post_data["text"]
    return all(
        (
            post_text,
            not any(restricted_word in post_text for restricted_word in restricted_words),
            any(
                [
                    re.findall(pattern, post_text, flags=re.IGNORECASE)
                    for pattern in [rf'{pattern}' for pattern in patterns]
                ]
            )
        )
    )
