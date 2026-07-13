import pandas as pd

def compute_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Compute Pearson correlation matrix."""
    return df.select_dtypes(include='number').corr()

def top_correlations(corr_matrix: pd.DataFrame, threshold=0.5) -> pd.DataFrame:
    """Filter and rank strong correlations."""
    pairs = corr_matrix.unstack().reset_index()
    pairs.columns = ['Feature 1', 'Feature 2', 'Correlation']
    pairs = pairs[pairs['Feature 1'] != pairs['Feature 2']]
    pairs['Abs Corr'] = pairs['Correlation'].abs()
    return pairs[pairs['Abs Corr'] >= threshold].sort_values('Abs Corr', ascending=False)

def hba1c_correlations(df: pd.DataFrame, target_col='hba1c_level') -> pd.Series:
    """Get correlations of all features with the HbA1c target column."""
    if target_col in df.columns:
        return df.select_dtypes(include='number').corr()[target_col].sort_values(ascending=False)
    return pd.Series(dtype=float)
