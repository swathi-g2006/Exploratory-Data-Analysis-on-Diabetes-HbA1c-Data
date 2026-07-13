import pandas as pd
import numpy as np

def compute_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Compute descriptive statistics for numeric columns."""
    stats = df.describe().T
    stats['median']   = df.median(numeric_only=True)
    stats['mode']     = df.mode(numeric_only=True).iloc[0]
    stats['skewness'] = df.skew(numeric_only=True)
    stats['kurtosis'] = df.kurt(numeric_only=True)
    if '25%' in stats.columns and '75%' in stats.columns:
        stats['IQR'] = stats['75%'] - stats['25%']
    return stats

def categorical_summary(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Value counts and proportions for a categorical column."""
    counts = df[col].value_counts()
    props  = df[col].value_counts(normalize=True) * 100
    return pd.DataFrame({'Count': counts, 'Percentage (%)': props.round(2)})
