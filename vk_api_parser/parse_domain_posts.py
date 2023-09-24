from .parse_wall_data import parse_wall_data
from vk_api import VkApi


def parse_domain_posts(
        posts_count: int,
        posts_per_time: int,
        max_offset: int,
        api: VkApi,
        patterns: list[str],
        restricted_words: list[str],
        domain: str
) -> list[list[float, int, int, str]]:
    post_offset = 1
    all_posts = []

    while (post_offset <= posts_count) and (post_offset <= max_offset):
        posts = parse_wall_data(api, post_offset, patterns, restricted_words, domain)
        post_offset += posts_per_time
        all_posts.extend(posts)

    return all_posts
