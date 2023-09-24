import datetime

from vk_api import VkApi
from filter_post_data import filter_post_data
from utils import find_apartment_cost


def parse_wall_data(
        api: VkApi,
        post_offset: int,
        patterns: list[str],
        restricted_words: list[str],
        domain: str
) -> list[list[float, int, int, str]]:
    data = api.method(
        method="wall.get",
        values={"domain": domain, "offset": post_offset, "count": 1000}
    )["items"]
    posts = []
    for post in data:
        if filter_post_data(post, patterns=patterns, restricted_words=restricted_words):
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
