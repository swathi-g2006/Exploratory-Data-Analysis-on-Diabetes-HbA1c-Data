import pandas as pd
import os

def load_data(filepath: str) -> pd.DataFrame:
    """Load the diabetes HbA1c CSV dataset."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at: {filepath}")
    
    df = pd.read_csv(filepath, encoding='utf-8')
    print(f"[INFO] Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def inspect_data(df: pd.DataFrame) -> None:
    """Print basic info about the dataframe."""
    print(df.info())
    print("-" * 60)
    print(df.head(5))
    print("-" * 60)
    print(df.describe())
