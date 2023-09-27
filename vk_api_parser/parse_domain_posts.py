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
    """
    Парсит определённое количество постов - posts_count
    необходимого источника

    Args:
        posts_count (int): количество постов, которых
        нужно распарсить
        posts_per_time (int): количество постов, которое
        должно просматриваться за одно обращение к API
        max_offset (int): количество всех постов источника
        api (VkApi): апи ВК
        patterns (list[str]): слова для поиска в посте
        restricted_words (list[str]): недопустимые слова в посте
        domain (str): имя источника постов

    Returns:
        list[list[float, int, int, str]]: список записей вида:
        `цена аренды квартиры`, `год публикации поста`,
        `месяц публикации поста`, `текст поста в одну строку`
    """    
    post_offset = 1
    all_posts = []

    while (post_offset <= posts_count) and (post_offset <= max_offset):
        posts = parse_wall_data(api, post_offset, patterns, restricted_words, domain)
        post_offset += posts_per_time
        all_posts.extend(posts)

    return all_posts
