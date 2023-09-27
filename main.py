import json
import pandas as pd
from vk_api import VkApi

from utils import clear_posts_data
from vk_api_parser import get_posts_count, parse_domain_posts


def main():
    with open("config.json", "r", encoding="utf-8") as config_file:
        config_data = json.load(config_file)

        API_VERSION = config_data["api_version"]
        ACCESS_TOKEN = config_data["access_token"]
        DOMAINS = config_data["domains"]

        POST_PER_TIME = config_data["post_per_time"]
        RESTRICTED_WORDS = config_data["post_filter"]["restricted_words"]
        CONTAINS_WORDS = config_data["post_filter"]["contains_words"]
        POST_NUMBER = config_data["post_number"]

        del config_data

    api = VkApi(token=ACCESS_TOKEN, api_version=API_VERSION)
    for domain in DOMAINS:
        max_offset = get_posts_count(api, domain, POST_PER_TIME)

        if not POST_NUMBER:
            POST_NUMBER = max_offset

        all_posts = parse_domain_posts(
            posts_count=POST_NUMBER,
            posts_per_time=POST_PER_TIME,
            max_offset=max_offset,
            api=api,
            patterns=CONTAINS_WORDS,
            restricted_words=RESTRICTED_WORDS,
            domain=domain
        )


        df = pd.DataFrame(
            data=all_posts,
            columns=["money", "year", "month", "text"],
        )
        domain = str(domain)
        initial_len = len(df)
        df, count_of_nan_money, count_of_duplicates, count_of_blowouts = clear_posts_data(df=df, domain=domain)
        final_len = len(df)

        count_of_losses = count_of_nan_money + count_of_duplicates + count_of_blowouts

        print(
            f"Domain = {domain}\n",
            f"Count of all {domain!r} posts: {max_offset}\n",
            f"Count of apartments posts: {initial_len}\n",
            f"Percent of apartments to all posts: {str((initial_len / max_offset) * 100)[:5]}%\n",
            "Count of {type_of_data} and percents to apartments posts count:\n"
            f"Count and percents of empty money: {count_of_nan_money} - {str((count_of_nan_money / (initial_len or 1)) * 100)[:5]}%\n"
            f"Count and percents of duplicates: {count_of_duplicates} - {str((count_of_duplicates / (initial_len or 1)) * 100)[:5]}%\n"
            f"Count and percents of blowouts: {count_of_blowouts} - {str((count_of_blowouts / (initial_len or 1)) * 100)[:5]}%\n"
            f"Count and percents of losses: {count_of_losses} - {str((count_of_losses / (initial_len or 1)) * 100)[:5]}%\n"
            f"Count and percents of cleared data: {final_len} - {str((final_len / (initial_len or 1)) * 100)[:5]}%\n\n"
        )

if __name__ == "__main__":
    main()


