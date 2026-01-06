
def split_title(df, column="title"):
    """
    The function `split_title` splits a DataFrame column into two separate columns based on a specified
    delimiter.
    
    :param df: The `df` parameter is a DataFrame that contains a column with titles that are formatted
    with a colon (":") separating the department and reason. The function `split_title` takes this
    DataFrame as input and splits the titles into two separate columns, "department" and "reason", based
    on the colon
    :param column: The `column` parameter in the `split_title` function is used to specify the column in
    the DataFrame `df` that contains the titles to be split into department and reason. By default, the
    `column` parameter is set to "title", but you can specify a different column name if the, defaults
    to title (optional)
    :return: The function `split_title` takes a DataFrame `df` and splits the values in the specified
    `column` (default is "title") by ":" into two separate columns "department" and "reason". It then
    returns the modified DataFrame `df` with the new "department" and "reason" columns added.
    """

    df = df.copy()

    split_cols = df[column].str.split(":", n=1, expand=True)
    df["department"] = split_cols[0].str.strip()
    df["reason"] = split_cols[1].str.strip()

    return df

def extract_time_features(df, column="timeStamp"):
    """
    The function `extract_time_features` extracts various time-related features from a datetime column
    in a DataFrame.
    
    :param df: The function `extract_time_features` takes a DataFrame `df` as input and extracts various
    time-related features from a specified column containing timestamps. The default column name for
    timestamps is "timeStamp", but you can specify a different column name if needed
    :param column: The `column` parameter in the `extract_time_features` function is used to specify the
    column in the DataFrame `df` that contains the timestamp data. By default, the column name is set to
    "timeStamp", but you can provide a different column name if your timestamp data is stored in a,
    defaults to timeStamp (optional)
    :return: The function `extract_time_features` takes a DataFrame `df` and extracts various
    time-related features from the specified column (default is "timeStamp"). It adds new columns to the
    DataFrame including "hour", "day_of_week", "day_name", "month", and "month_name" based on the
    timestamp information in the specified column. The function then returns the modified DataFrame with
    the added time features
    """
    df = df.copy()

    df["hour"] = df[column].dt.hour
    df["day_of_week"] = df[column].dt.dayofweek
    df["day_name"] = df[column].dt.day_name()
    df["month"] = df[column].dt.month
    df["month_name"] = df[column].dt.month_name()

    return df

def filter_ems_calls(df):
    """
    The function `filter_ems_calls` filters a DataFrame to only include rows where the "department"
    column is equal to "EMS".
    
    :param df: A pandas DataFrame containing emergency call data, where each row represents a call and
    includes information such as the department handling the call. The function `filter_ems_calls`
    filters this DataFrame to only include rows where the department is "EMS" and returns a copy of the
    filtered DataFrame
    :return: The function `filter_ems_calls` takes a DataFrame `df` as input and returns a new DataFrame
    containing only the rows where the "department" column is equal to "EMS".
    """
    return df[df["department"] == "EMS"].copy()
