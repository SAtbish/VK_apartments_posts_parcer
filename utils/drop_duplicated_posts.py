import pandas as pd


def drop_duplicated_posts(df: pd.DataFrame, domain: str) -> tuple[pd.DataFrame, int]:
    df.to_csv(f"{domain}/{domain}_with_duplicates.csv", index=False)
    df_no_duplicates = df.drop_duplicates()
    return df_no_duplicates, len(df) - len(df_no_duplicates)

