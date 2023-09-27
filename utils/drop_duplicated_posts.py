from pandas import DataFrame


def drop_duplicated_posts(df: DataFrame, domain: str) -> tuple[DataFrame, int]:
    """
    Очищает датафрейм данных постов от
    дублирующихся записей

    Args:
        df (DataFrame): датафрейм данных постов
        domain (str): имя источника постов

    Returns:
        tuple[DataFrame, int]: датафрейм очищенных от
        дубликатов постов и количество таких постов
    """    
    df.to_csv(f"{domain}/{domain}_with_duplicates.csv", index=False)
    df_no_duplicates = df.drop_duplicates()
    return df_no_duplicates, len(df) - len(df_no_duplicates)

