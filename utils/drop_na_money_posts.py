import pandas as pd


def drop_na_money_from_df(df: pd.DataFrame, domain: str) -> tuple[pd.DataFrame, int]:
    count_of_nan_money = df.isnull().get("money").sum()
    df.to_csv(f"{domain}/{domain}_with_empty_cost.csv", index=False)
    df = df.dropna()
    return df, count_of_nan_money
