import re
from typing import Any


def filter_post_data(
        post_text: str,
        patterns: list[str],
        restricted_words: list[str]
) -> bool:
    """
    Отбирает только валидные посты - содержат текст, не содержат
    недопустимых строк и содержат слова для поиска

    Args:
        post_text (str): текст поста
        patterns (list[str]): слова для поиска в посте
        restricted_words (list[str]): недопустимые слова в посте

    Returns:
        bool: результат проверки поста на валидность
    """
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
