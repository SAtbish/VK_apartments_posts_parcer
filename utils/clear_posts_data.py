from pandas import DataFrame
from .drop_na_money_posts import drop_na_money_from_df
from .drop_duplicated_posts import drop_duplicated_posts
from .drop_blowouts_posts import drop_blowouts_posts
from datetime import datetime
import os


def clear_posts_data(df: DataFrame, domain: str) -> tuple[DataFrame, int, int, int]:
    """
    Очищает полученные данные постов от постов: в которых
    не получилось вытянуть цену квартиры, дублирующих друг
    друга и от постов с не соответствующими действительности
    ценами(такое возникает и-за неправильной работы алгоритма
    парсинга цены из текста поста)

    Args:
        df (DataFrame): датафрейм начальных собранных данных
        domain (str): имя группы или страницы источника

    Returns:
        tuple[DataFrame, int, int, int]: очищенный датафрейм данных,
        количество постов с отсутствующей ценой квартиры, количество
        постов-дубликатов, количество записей с выбросом цены.
    """    
    if not os.path.isdir(domain):
        os.mkdir(domain)
    df, count_of_nan_money = drop_na_money_from_df(df, domain)
    df, count_of_duplicates = drop_duplicated_posts(df, domain)
    df, count_of_blowouts = drop_blowouts_posts(df, domain)
    df.to_csv(f"{domain}/{domain}_clear_{datetime.now().strftime('%d%m%Y')}.csv", index=False)
    return df, count_of_nan_money, count_of_duplicates, count_of_blowouts

