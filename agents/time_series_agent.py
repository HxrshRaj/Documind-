def detect_time_series(
    df
):

    for column in df.columns:

        name = column.lower()

        if (
            "date" in name
            or
            "time" in name
            or
            "year" in name
        ):

            return True

    return False