import pandas as pd


def generate_profile(df):
    """
    Generate dataset profiling information.
    """

    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "numerical_columns": len(
            df.select_dtypes(include=["int64", "float64"]).columns
        ),
        "categorical_columns": len(
            df.select_dtypes(include=["object"]).columns
        ),
        "missing_values": int(df.isnull().sum().sum()),
        "memory_usage_kb": round(
            df.memory_usage(deep=True).sum() / 1024,
            2
        )
    }

    return profile