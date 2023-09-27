import datetime

from vk_api import VkApi
from .filter_post_data import filter_post_data
from utils import find_apartment_cost


def parse_wall_data(
        api: VkApi,
        post_offset: int,
        patterns: list[str],
        restricted_words: list[str],
        domain: str
) -> list[list[float, int, int, str]]:
    """
    Парсит посты, которые получилось вытащить за одно
    обращение к API

    Args:
        api (VkApi): апи ВК
        post_offset (int): _description_
        patterns (list[str]): слова для поиска в посте
        restricted_words (list[str]): недопустимые слова в посте
        domain (str): имя источника постов

    Returns:
        list[list[float, int, int, str]]: список записей вида:
        `цена аренды квартиры`, `год публикации поста`,
        `месяц публикации поста`, `текст поста в одну строку`
    """    
    data = api.method(
        method="wall.get",
        values={"domain": domain, "offset": post_offset, "count": 1000}
    )["items"]
    posts = []
    for post in data:
        if filter_post_data(post["text"], patterns=patterns, restricted_words=restricted_words):
            dt = datetime.datetime.fromtimestamp(post["date"])
            posts.append(
                [
                    find_apartment_cost(post["text"]),
                    dt.year,
                    dt.month,
                    post["text"].replace("\n", " ")
                ]
            )
            continue
    return posts
