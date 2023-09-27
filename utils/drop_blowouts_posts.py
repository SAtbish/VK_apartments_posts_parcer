from pandas import DataFrame


def drop_blowouts_posts(df: DataFrame, domain: str) -> tuple[DataFrame, int]:
    """
    Очищает датафрейм от записей с ценами, не соответствующими
    действительности.

    Args:
        df (DataFrame): датафрейм данных постов
        domain (str): имя источника постов

    Returns:
        tuple[DataFrame, int]: датафрейм данных очищенных
        от выбросов цены постов, количество постов с выбросами
    """    
    df.to_csv(f"{domain}/{domain}_with_blowouts.csv", index=False)
    df_counts_fixed = df[df.money < 40000]
    df_counts_fixed = df_counts_fixed[df_counts_fixed.money > 5000]
    return df_counts_fixed, len(df) - len(df_counts_fixed)
