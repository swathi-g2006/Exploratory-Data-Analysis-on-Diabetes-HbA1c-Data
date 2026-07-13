import matplotlib
matplotlib.use("Agg")  # Non-GUI backend — required for server/cloud environments
import matplotlib.pyplot as plt
import seaborn as sns
import os

CHART_DIR = "outputs/charts"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def plot_histogram(df, column, save=True):
    """Plot histogram for a numeric column."""
    if column not in df.columns: return
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, color='steelblue', bins=30)
    plt.title(f'Distribution of {column}', fontsize=14)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    if save:
        path = os.path.join(CHART_DIR, 'histograms')
        ensure_dir(path)
        plt.savefig(os.path.join(path, f'{column}_histogram.png'), dpi=150, bbox_inches='tight')
    plt.close()

def plot_boxplot(df, column, hue=None, save=True):
    """Plot box plot, optionally grouped by a hue column."""
    if column not in df.columns: return
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=hue if hue in df.columns else None, y=column, palette='Set2')
    plt.title(f'Box Plot: {column}', fontsize=14)
    if save:
        path = os.path.join(CHART_DIR, 'boxplots')
        ensure_dir(path)
        plt.savefig(os.path.join(path, f'{column}_boxplot.png'), dpi=150, bbox_inches='tight')
    plt.close()

def plot_scatter(df, x_col, y_col, hue=None, save=True):
    """Plot scatter plot between two numeric columns."""
    if x_col not in df.columns or y_col not in df.columns: return
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue if hue in df.columns else None, alpha=0.7)
    plt.title(f'Scatter: {x_col} vs {y_col}', fontsize=14)
    if save:
        path = os.path.join(CHART_DIR, 'scatterplots')
        ensure_dir(path)
        plt.savefig(os.path.join(path, f'{x_col}_vs_{y_col}.png'), dpi=150, bbox_inches='tight')
    plt.close()

def plot_pie(df, column, save=True):
    """Plot pie chart for a categorical column."""
    if column not in df.columns: return
    counts = df[column].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%',
            startangle=140, colors=sns.color_palette('pastel', len(counts)))
    plt.title(f'Distribution of {column}', fontsize=14)
    if save:
        path = os.path.join(CHART_DIR, 'piecharts')
        ensure_dir(path)
        plt.savefig(os.path.join(path, f'{column}_piechart.png'), dpi=150, bbox_inches='tight')
    plt.close()

def plot_correlation_heatmap(df, save=True):
    """Plot full correlation matrix heatmap."""
    plt.figure(figsize=(12, 10))
    corr = df.select_dtypes(include='number').corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
                linewidths=0.5, square=True)
    plt.title('Correlation Heatmap', fontsize=15)
    if save:
        path = os.path.join(CHART_DIR, 'heatmaps')
        ensure_dir(path)
        plt.savefig(os.path.join(path, 'correlation_heatmap.png'), dpi=150, bbox_inches='tight')
    plt.close()
