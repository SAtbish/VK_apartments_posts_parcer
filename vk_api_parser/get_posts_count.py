from vk_api import VkApiError, VkApi


def get_max_offset(api: VkApi, domain: str, posts_per_time: int) -> int:
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
