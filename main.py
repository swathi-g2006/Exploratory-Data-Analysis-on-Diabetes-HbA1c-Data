import os
from scripts.data_loader    import load_data, inspect_data
from scripts.data_cleaner   import clean_pipeline
from scripts.statistics     import compute_summary_stats
from scripts.visualizer     import (plot_histogram, plot_boxplot,
                                    plot_scatter, plot_pie,
                                    plot_correlation_heatmap)
from scripts.correlation    import compute_correlation_matrix, top_correlations
from scripts.report_generator import generate_report

RAW_PATH     = 'data/raw/diabetes_hba1c_raw.csv'
CLEANED_PATH = 'data/processed/diabetes_hba1c_cleaned.csv'

def run_eda():
    print("=" * 60)
    print("  EDA on Diabetes HbA1c Data — Starting Pipeline")
    print("=" * 60)

    # Phase 2: Load
    if not os.path.exists(RAW_PATH):
        print(f"[ERROR] Run aborted. Raw dataset not found at {RAW_PATH}")
        return

    df = load_data(RAW_PATH)
    inspect_data(df)

    # Phase 3: Clean
    print("\n[INFO] Cleaning data...")
    df = clean_pipeline(df)
    
    # Ensure processed directory exists
    os.makedirs(os.path.dirname(CLEANED_PATH), exist_ok=True)
    df.to_csv(CLEANED_PATH, index=False)
    print(f"[INFO] Cleaned data saved to {CLEANED_PATH}")

    # Phase 4: Stats
    print("\n[INFO] Computing descriptive statistics...")
    stats = compute_summary_stats(df)
    print(stats)

    # Phase 5: Visualize
    print("\n[INFO] Generating charts...")
    os.makedirs("outputs/charts", exist_ok=True)
    for col in ['hba1c_level', 'age', 'bmi', 'blood_glucose_level']:
        plot_histogram(df, col)
        plot_boxplot(df, col, hue='diabetes')
    plot_scatter(df, 'hba1c_level', 'blood_glucose_level', hue='diabetes')
    plot_pie(df, 'diabetes')
    plot_pie(df, 'gender')
    plot_correlation_heatmap(df)
    print("[INFO] Charts generated successfully.")

    # Phase 6: Correlation
    print("\n[INFO] Correlation analysis...")
    corr_matrix = compute_correlation_matrix(df)
    top = top_correlations(corr_matrix)
    print(top.head(5))

    # Phase 7: Report
    print("\n[INFO] Generating PDF report...")
    generate_report()

    print("\n✅ EDA pipeline complete!")

if __name__ == '__main__':
    run_eda()
