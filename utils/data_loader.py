import pandas as pd


def load_data(uploaded_file):
    """
    Loads a CSV file and returns a pandas DataFrame.
    """

    try:
        df = pd.read_csv(uploaded_file)
        return df

    except Exception as e:
        raise Exception(f"Error loading file: {e}")