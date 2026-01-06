
def split_title(df, column="title"):
    df = df.copy()

    split_cols = df[column].str.split(":", n=1, expand=True)
    df["department"] = split_cols[0].str.strip()
    df["reason"] = split_cols[1].str.strip()

    return df

def extract_time_features(df, column="timeStamp"):
    df = df.copy()

    df["hour"] = df[column].dt.hour
    df["day_of_week"] = df[column].dt.dayofweek
    df["day_name"] = df[column].dt.day_name()
    df["month"] = df[column].dt.month
    df["month_name"] = df[column].dt.month_name()

    return df

def filter_ems_calls(df):
    return df[df["department"] == "EMS"].copy()
