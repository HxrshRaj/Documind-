import pandas as pd


def detect_task(
    df,
    target_column
):

    target = df[target_column]

    # -------------------------
    # Time Series Detection
    # -------------------------
    for column in df.columns:

        name = column.lower()

        if (
            "date" in name
            or "time" in name
            or "year" in name
        ):

            return (
                "Time Series",
                "Date/Time column detected."
            )

    # -------------------------
    # Classification
    # -------------------------
    if target.dtype == "object":

        return (
            "Classification",
            "Target column contains categorical values."
        )

    # -------------------------
    # Numerical Target
    # -------------------------
    unique_values = target.nunique()

    if unique_values <= 10:

        return (
            "Classification",
            "Numerical target has a small number of unique classes."
        )

    # -------------------------
    # Regression
    # -------------------------
    return (
        "Regression",
        "Target column contains continuous numerical values."
    )