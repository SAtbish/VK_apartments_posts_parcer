import pandas as pd


def drop_blowouts_posts(df: pd.DataFrame, domain: str) -> tuple[pd.DataFrame, int]:
    df.to_csv(f"{domain}/{domain}_with_blowouts.csv", index=False)
    df_counts_fixed = df[df.money < 40000]
    df_counts_fixed = df_counts_fixed[df_counts_fixed.money > 5000]
    return df_counts_fixed, len(df) - len(df_counts_fixed)
