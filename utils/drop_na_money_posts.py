from pandas import DataFrame



def drop_na_money_from_df(df: DataFrame, domain: str) -> tuple[DataFrame, int]:
    """
    Очищает датафрейм данных постов от
    записей, содержащие пустое значение в поле `money`

    Args:
        df (DataFrame): датафрейм данных постов
        domain (str): имя источника постов

    Returns:
        tuple[DataFrame, int]: очищенный от записей с пустым
        полем `money` постов и количество таких постов
    """    
    count_of_nan_money = df.isnull().get("money").sum()
    df.to_csv(f"{domain}/{domain}_with_empty_cost.csv", index=False)
    df = df.dropna()
    return df, count_of_nan_money
