import pandas as pd

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values using median/mode strategy."""
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    before = len(df)
    df = df.drop_duplicates()
    print(f"[INFO] Removed {before - len(df)} duplicate rows.")
    return df

def detect_outliers_iqr(df: pd.DataFrame, column: str) -> pd.Series:
    """Detect outliers using IQR method."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    return df[(df[column] < Q1 - 1.5 * IQR) | (df[column] > Q3 + 1.5 * IQR)]

def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Run full cleaning pipeline."""
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df.columns = [c.lower().replace(' ', '_') for c in df.columns]
    
    # Just in case there are specific column naming mismatches with expected layout
    if 'hba1c_level' not in df.columns and 'hba1c' in df.columns:
         df.rename(columns={'hba1c': 'hba1c_level'}, inplace=True)
         
    return df
