import pandas as pd

from sklearn.preprocessing import LabelEncoder


def preprocess_data(df, target_column):
    """
    Enterprise preprocessing pipeline.

    Handles:
    - Missing values
    - Categorical encoding
    - Target encoding
    """

    df = df.copy()

    # -------------------------
    # Missing Values
    # -------------------------
    for column in df.columns:

        if pd.api.types.is_numeric_dtype(df[column]):

            df[column] = df[column].fillna(
                df[column].median()
            )

        else:

            df[column] = df[column].fillna(
                df[column].mode()[0]
            )

    # -------------------------
    # Encode Feature Columns
    # -------------------------
    for column in df.columns:

        if (
            not pd.api.types.is_numeric_dtype(df[column])
            and column != target_column
        ):

            encoder = LabelEncoder()

            df[column] = encoder.fit_transform(
                df[column].astype(str)
            )

    # -------------------------
    # Encode Target Column
    # -------------------------
    if not pd.api.types.is_numeric_dtype(
        df[target_column]
    ):

        target_encoder = LabelEncoder()

        df[target_column] = target_encoder.fit_transform(
            df[target_column].astype(str)
        )

    return df