import pandas as pd


def parse_timestamps(df, column="timeStamp"):
    df = df.copy()
    df[column] = pd.to_datetime(df[column], errors="coerce")
    return df

def normalize_zip_codes(df, column="zip"):
    df = df.copy()

    df[column] = (
        df[column]
        .astype("Int64")
        .astype(str)
        .str.zfill(5)
        .replace("0<NA>", pd.NA)
    )

    return df

