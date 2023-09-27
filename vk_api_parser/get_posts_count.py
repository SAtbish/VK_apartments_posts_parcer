from vk_api import VkApiError, VkApi


def get_posts_count(api: VkApi, domain: str, posts_per_time: int) -> int:
    """
    Получает количество постов группы

    Args:
        api (VkApi): апи ВК
        domain (str): имя источника постов
        posts_per_time (int): количество постов, которое
        должно просматриваться за одно обращение к API

    Raises:
        VkApiError: Ошибка, возникающая при обращении к
        API с неправильным access токеном

    Returns:
        int: количество постов группы
    """    
    try:
        return api.method(
            method="wall.get",
            values={"domain": domain, "count": posts_per_time}
        )["count"]
    except VkApiError:
        raise VkApiError(
            "Invalid access token. Get your own token for vk.com on this site: "
            "https://vkhost.github.io/"
        )
