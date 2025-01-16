import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a dataset from a CSV file into a pandas DataFrame.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: The loaded dataset as a pandas DataFrame.
    """
    df = pd.read_csv(path, index_col="country")
    print(f"Dataset dimensions: {df.shape}")
    return df
