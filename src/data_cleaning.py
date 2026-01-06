import pandas as pd


def parse_timestamps(df, column="timeStamp"):
    """
    The function `parse_timestamps` converts a column in a DataFrame to datetime format.
    
    :param df: The `df` parameter is typically used to represent a DataFrame in Python, often from a
    library like pandas. It contains structured data in rows and columns, similar to a spreadsheet or
    database table
    :param column: The `column` parameter in the `parse_timestamps` function is used to specify the name
    of the column in the DataFrame `df` that contains the timestamps to be parsed and converted to
    datetime format. By default, the `column` parameter is set to "timeStamp" if no specific column,
    defaults to timeStamp (optional)
    :return: The function `parse_timestamps` takes a DataFrame `df` and converts the values in the
    specified column (default is "timeStamp") to datetime format using `pd.to_datetime` with errors set
    to "coerce". The function then returns the modified DataFrame with the timestamp column converted to
    datetime format.
    """
    df = df.copy()
    df[column] = pd.to_datetime(df[column], errors="coerce")
    return df

def normalize_zip_codes(df, column="zip"):
    """
    The function `normalize_zip_codes` takes a DataFrame and normalizes the zip code values in a
    specified column by converting them to strings, padding with zeros, and handling missing values
    appropriately.
    
    :param df: The `df` parameter in the `normalize_zip_codes` function is a DataFrame that contains zip
    code data. The function normalizes the zip codes in the specified column by converting them to a
    5-digit format with leading zeros if necessary. The function then replaces any "0" values with `pd
    :param column: The `column` parameter in the `normalize_zip_codes` function specifies the name of
    the column in the DataFrame `df` that contains the zip codes. This parameter allows you to specify
    which column should be normalized. If no column name is provided, the default column name is "zip",
    defaults to zip (optional)
    :return: The function `normalize_zip_codes` takes a DataFrame `df` and an optional column name
    parameter (default is "zip"). It normalizes the zip codes in the specified column by converting them
    to integers, filling with leading zeros to make them 5 digits long, and replacing any "0" values
    with `pd.NA`. The function returns the modified DataFrame `df`.
    """
    df = df.copy()

    df[column] = (
        df[column]
        .astype("Int64")
        .astype(str)
        .str.zfill(5)
        .replace("0<NA>", pd.NA)
    )

    return df

