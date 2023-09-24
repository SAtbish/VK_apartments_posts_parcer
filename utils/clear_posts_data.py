import pandas as pd
from .drop_na_money_posts import drop_na_money_from_df
from .drop_duplicated_posts import drop_duplicated_posts
from .drop_blowouts_posts import drop_blowouts_posts
import os


def clear_posts_data(df: pd.DataFrame, domain: str) -> tuple[pd.DataFrame, int, int, int]:
    if not os.path.isdir(domain):
        os.mkdir(domain)
    df, count_of_nan_money = drop_na_money_from_df(df, domain)
    df, count_of_duplicates = drop_duplicated_posts(df, domain)
    df, count_of_blowouts = drop_blowouts_posts(df, domain)
    df.to_csv(f"{domain}/{domain}_clear.csv", index=False)
    return df, count_of_nan_money, count_of_duplicates, count_of_blowouts

