# Exploratory Data Analysis on Diabetes HbA1c Data

This project performs a comprehensive **Exploratory Data Analysis (EDA)** on a Diabetes HbA1c dataset. 
It explores hidden patterns, distributions, and relationships through data cleaning, descriptive statistics, visualization, and correlation analysis.

## Features
- **Data Cleanup**: Handling missing values, duplicates, and outliers.
- **Visualizations**: Histograms, Box Plots, Scatter Plots, Heatmaps.
- **Reporting**: Automated EDA report generation in PDF format.
- **Frontend Dashboard**: Interactive UI built with Streamlit to visualize everything in the browser.

## Getting Started

1. Set up a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis pipeline (generates cleaned data, charts, statistics, and PDF report):
   ```bash
   python main.py
   ```

4. Launch the Streamlit dashboard:
   ```bash
   streamlit run frontend/dashboard/app.py
   ```

5. Explore the interactive Landing page:
   Simply open `frontend/landing/index.html` in your web browser.
