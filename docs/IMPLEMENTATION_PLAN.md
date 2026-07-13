# 📊 Implementation Plan: Exploratory Data Analysis on Diabetes HbA1c Data

**Version:** 2.0  
**Date:** 2026-07-12  
**Authors:** Data Analytics Team  
**Target Audience:** Students, Researchers, Healthcare Analysts  

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Project Structure](#2-project-structure)
3. [Technology Stack](#3-technology-stack)
4. [Phase-by-Phase Implementation Plan](#4-phase-by-phase-implementation-plan)
   - [Phase 1: Environment Setup](#phase-1-environment-setup)
   - [Phase 2: Data Ingestion & Loading](#phase-2-data-ingestion--loading)
   - [Phase 3: Data Cleaning & Preprocessing](#phase-3-data-cleaning--preprocessing)
   - [Phase 4: Descriptive Statistics](#phase-4-descriptive-statistics)
   - [Phase 5: Data Visualization](#phase-5-data-visualization)
   - [Phase 6: Correlation Analysis](#phase-6-correlation-analysis)
   - [Phase 7: Reporting & Export](#phase-7-reporting--export)
   - [Phase 8: Frontend Dashboard](#phase-8-frontend-dashboard)
5. [Module Descriptions](#5-module-descriptions)
6. [Dataset Description](#6-dataset-description)
7. [Deliverables Checklist](#7-deliverables-checklist)
8. [Non-Functional Requirements](#8-non-functional-requirements)
9. [Timeline Estimate](#9-timeline-estimate)
10. [Risks & Mitigations](#10-risks--mitigations)

---

## 1. Project Overview

This project performs a comprehensive **Exploratory Data Analysis (EDA)** on a Diabetes HbA1c dataset. HbA1c (Glycated Hemoglobin) is a critical biomarker used in the diagnosis and management of diabetes. The goal is to uncover hidden patterns, distributions, and relationships within the data using Python-based analytical tools and publish insights through clean visualizations and a structured final report.

### Key Goals

| Goal | Description |
|------|-------------|
| **Data Quality** | Identify and handle missing values, duplicates, and outliers |
| **Descriptive Stats** | Compute mean, median, std, quartiles for all numeric features |
| **Visualization** | Generate histograms, box plots, scatter plots, pie charts, heatmaps |
| **Correlation** | Discover feature-level relationships and multicollinearity |
| **Reporting** | Export a structured, professional final analysis report |

---

## 2. Project Structure

```
Exploratory Data Analysis on Diabetes HbA1c Data/
│
├── 📁 data/
│   ├── raw/
│   │   └── diabetes_hba1c_raw.csv          # Original, untouched dataset
│   └── processed/
│       └── diabetes_hba1c_cleaned.csv      # Post-cleaning dataset
│
├── 📁 notebooks/
│   └── EDA_Diabetes_HbA1c.ipynb            # Main Jupyter Notebook (end-to-end EDA)
│
├── 📁 scripts/
│   ├── data_loader.py                      # Module: Load CSV data
│   ├── data_cleaner.py                     # Module: Clean & preprocess data
│   ├── statistics.py                       # Module: Descriptive statistics
│   ├── visualizer.py                       # Module: All chart generation
│   ├── correlation.py                      # Module: Correlation analysis
│   └── report_generator.py                 # Module: Export final report
│
├── 📁 frontend/                            ← NEW: Web Frontend
│   ├── 📁 dashboard/
│   │   └── app.py                          # Streamlit interactive dashboard
│   └── 📁 landing/
│       ├── index.html                      # HTML landing page
│       ├── style.css                       # CSS styling (dark glassmorphism)
│       └── main.js                         # JavaScript scroll animations
│
├── 📁 outputs/
│   ├── charts/
│   │   ├── histograms/
│   │   │   └── *.png                       # Histogram plots
│   │   ├── boxplots/
│   │   │   └── *.png                       # Box plot charts
│   │   ├── scatterplots/
│   │   │   └── *.png                       # Scatter plot charts
│   │   ├── piecharts/
│   │   │   └── *.png                       # Pie/donut charts
│   │   └── heatmaps/
│   │       └── correlation_heatmap.png     # Correlation matrix heatmap
│   └── reports/
│       └── EDA_Final_Report.pdf            # Auto-generated final report
│
├── 📁 docs/
│   └── IMPLEMENTATION_PLAN.md              # This document
│
├── requirements.txt                        # Python package dependencies
├── README.md                               # Project overview and setup guide
└── main.py                                 # Entry point to run all scripts
```

---

## 3. Technology Stack

| Tool/Library | Version (Recommended) | Purpose |
|---|---|---|
| **Python** | 3.10+ | Core programming language |
| **Pandas** | 2.x | Data loading, cleaning, manipulation |
| **NumPy** | 1.26+ | Numerical operations and array handling |
| **Matplotlib** | 3.8+ | Base plotting and figure customization |
| **Seaborn** | 0.13+ | Statistical visualizations (heatmap, pairplot) |
| **Jupyter Notebook** | 7.x | Interactive analysis and documentation |
| **ReportLab / FPDF2** | Latest | PDF report generation |
| **Scipy** | 1.12+ | Statistical tests (optional enrichment) |
| **Streamlit** | 1.35+ | 🆕 Interactive web dashboard (Python-native) |
| **Plotly** | 5.x | 🆕 Interactive charts inside dashboard |
| **HTML5 / CSS3** | — | 🆕 Landing page structure & styling |
| **JavaScript (Vanilla)** | ES6+ | 🆕 Landing page interactivity |

---

## 4. Phase-by-Phase Implementation Plan

---

### Phase 1: Environment Setup

**Goal:** Prepare a clean, reproducible Python environment.

#### Steps:

1. **Create the project directory structure** as defined in Section 2.
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter fpdf2 scipy openpyxl
   pip freeze > requirements.txt
   ```
4. **Verify installations:**
   ```python
   import pandas, numpy, matplotlib, seaborn
   print("All packages loaded successfully!")
   ```
5. **Create `README.md`** with setup instructions, project objective, and dataset source.

**Deliverable:** Functional environment + `requirements.txt` + `README.md`

---

### Phase 2: Data Ingestion & Loading

**Module:** `scripts/data_loader.py`

**Goal:** Load the raw CSV dataset into a Pandas DataFrame reliably.

#### Steps:

1. **Place raw dataset** in `data/raw/diabetes_hba1c_raw.csv`.
2. **Implement `load_data()` function:**
   - Accept a file path as parameter
   - Read CSV using `pd.read_csv()`
   - Handle encoding issues (`encoding='utf-8'` or `latin-1`)
   - Handle separator variations (`,`, `;`, or `\t`)
3. **Initial inspection:**
   - Print `.shape`, `.dtypes`, `.head(10)`, `.info()`
   - Log number of rows, columns, and data types
4. **Validation checks:**
   - Assert the file exists before loading
   - Log warnings if file is empty or has zero rows

#### Code Skeleton:
```python
# scripts/data_loader.py
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
    print(df.head(10))
    print(df.describe())
```

**Deliverable:** `data_loader.py` + data successfully loaded into notebook.

---

### Phase 3: Data Cleaning & Preprocessing

**Module:** `scripts/data_cleaner.py`

**Goal:** Ensure the dataset is complete, consistent, and analysis-ready.

#### Steps:

1. **Identify missing values:**
   - Use `df.isnull().sum()` per column
   - Visualize missing data with a heatmap
   - Strategy: Fill numeric nulls with **median**, categorical with **mode**

2. **Remove duplicate records:**
   - Use `df.duplicated().sum()` to count
   - Drop using `df.drop_duplicates(inplace=True)`

3. **Fix data types:**
   - Convert age columns to `int`, HbA1c % to `float`
   - Encode categorical columns (e.g., gender: `Male → 1`, `Female → 0`)

4. **Handle outliers:**
   - Use **IQR method** to detect outliers per numeric column
   - Log anomalies (do not blindly remove; document in report)

5. **Rename columns:**
   - Standardize column names: lowercase, underscores (e.g., `HbA1c Level` → `hba1c_level`)

6. **Export cleaned data:**
   - Save to `data/processed/diabetes_hba1c_cleaned.csv`

#### Code Skeleton:
```python
# scripts/data_cleaner.py
import pandas as pd

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values using median/mode strategy."""
    for col in df.select_dtypes(include='number').columns:
        df[col].fillna(df[col].median(), inplace=True)
    for col in df.select_dtypes(include='object').columns:
        df[col].fillna(df[col].mode()[0], inplace=True)
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    before = len(df)
    df.drop_duplicates(inplace=True)
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
    return df
```

**Deliverable:** `data_cleaner.py` + `diabetes_hba1c_cleaned.csv`

---

### Phase 4: Descriptive Statistics

**Module:** `scripts/statistics.py`

**Goal:** Compute and summarize statistical properties of all features.

#### Steps:

1. **Summary statistics for numeric columns:**
   - Mean, median, mode
   - Standard deviation, variance
   - Min, max, range
   - Q1 (25th percentile), Q3 (75th percentile), IQR

2. **Distribution analysis:**
   - Skewness and Kurtosis per column
   - Normality check (optional: Shapiro-Wilk test via `scipy.stats`)

3. **Categorical summary:**
   - Value counts for gender, diabetes status, etc.
   - Proportion/percentage tables

4. **Format output** as a structured Pandas DataFrame and print to console/notebook.

#### Code Skeleton:
```python
# scripts/statistics.py
import pandas as pd
import numpy as np

def compute_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Compute descriptive statistics for numeric columns."""
    stats = df.describe().T
    stats['median']   = df.median(numeric_only=True)
    stats['mode']     = df.mode(numeric_only=True).iloc[0]
    stats['skewness'] = df.skew(numeric_only=True)
    stats['kurtosis'] = df.kurt(numeric_only=True)
    stats['IQR']      = stats['75%'] - stats['25%']
    return stats

def categorical_summary(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Value counts and proportions for a categorical column."""
    counts = df[col].value_counts()
    props  = df[col].value_counts(normalize=True) * 100
    return pd.DataFrame({'Count': counts, 'Percentage (%)': props.round(2)})
```

**Deliverable:** `statistics.py` + stats tables rendered in notebook.

---

### Phase 5: Data Visualization

**Module:** `scripts/visualizer.py`

**Goal:** Generate clear, labeled, and publication-quality charts.

#### Chart Types & Purpose:

| Chart Type | Columns | Purpose |
|---|---|---|
| **Histogram** | HbA1c %, Age, BMI, Blood Glucose | Show distributions |
| **Box Plot** | HbA1c % by Diabetes Status | Identify spread & outliers |
| **Scatter Plot** | HbA1c % vs Blood Glucose | Show linear relationships |
| **Pie / Donut Chart** | Gender, Diabetes Status | Show proportions |
| **Pair Plot** | All numeric columns | Overview of all pairwise relations |
| **Correlation Heatmap** | All numeric columns | Show correlation coefficients |

#### Implementation Rules:
- All charts saved to appropriate `outputs/charts/` subfolder as `.png`
- Use consistent color palette (e.g., Seaborn `coolwarm` or `viridis`)
- Include titles, axis labels, and legends on every chart
- Figure size: minimum `(10, 6)` for readability

#### Code Skeleton:
```python
# scripts/visualizer.py
import matplotlib.pyplot as plt
import seaborn as sns
import os

CHART_DIR = "outputs/charts"

def plot_histogram(df, column, save=True):
    """Plot histogram for a numeric column."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, color='steelblue', bins=30)
    plt.title(f'Distribution of {column}', fontsize=14)
    plt.xlabel(column); plt.ylabel('Frequency')
    if save:
        path = os.path.join(CHART_DIR, 'histograms', f'{column}_histogram.png')
        plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.show()

def plot_boxplot(df, column, hue=None, save=True):
    """Plot box plot, optionally grouped by a hue column."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=hue, y=column, palette='Set2')
    plt.title(f'Box Plot: {column}', fontsize=14)
    if save:
        path = os.path.join(CHART_DIR, 'boxplots', f'{column}_boxplot.png')
        plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.show()

def plot_scatter(df, x_col, y_col, hue=None, save=True):
    """Plot scatter plot between two numeric columns."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, alpha=0.7)
    plt.title(f'Scatter: {x_col} vs {y_col}', fontsize=14)
    if save:
        path = os.path.join(CHART_DIR, 'scatterplots', f'{x_col}_vs_{y_col}.png')
        plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.show()

def plot_pie(df, column, save=True):
    """Plot pie chart for a categorical column."""
    counts = df[column].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%',
            startangle=140, colors=sns.color_palette('pastel'))
    plt.title(f'Distribution of {column}', fontsize=14)
    if save:
        path = os.path.join(CHART_DIR, 'piecharts', f'{column}_piechart.png')
        plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.show()

def plot_correlation_heatmap(df, save=True):
    """Plot full correlation matrix heatmap."""
    plt.figure(figsize=(12, 10))
    corr = df.select_dtypes(include='number').corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
                linewidths=0.5, square=True)
    plt.title('Correlation Heatmap', fontsize=15)
    if save:
        path = os.path.join(CHART_DIR, 'heatmaps', 'correlation_heatmap.png')
        plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.show()
```

**Deliverable:** `visualizer.py` + all chart `.png` files saved in `outputs/charts/`

---

### Phase 6: Correlation Analysis

**Module:** `scripts/correlation.py`

**Goal:** Quantify and interpret the relationships between variables.

#### Steps:

1. **Pearson Correlation:** Between all numeric feature pairs (HbA1c %, glucose, BMI, age)
2. **Top Correlations:** Filter `|r| > 0.5` and display as a ranked table
3. **HbA1c-specific correlations:** Which features are most correlated with HbA1c?
4. **Interpretation notes:** Document what high/low correlations mean clinically
5. **Optional:** Point-Biserial correlation for binary features (e.g., diabetes status)

#### Code Skeleton:
```python
# scripts/correlation.py
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
    return df.select_dtypes(include='number').corr()[target_col].sort_values(ascending=False)
```

**Deliverable:** `correlation.py` + correlation tables + heatmap image.

---

### Phase 7: Reporting & Export

**Module:** `scripts/report_generator.py`

**Goal:** Compile all findings into a structured, exportable PDF report.

#### Report Sections:

```
EDA Final Report — Structure
─────────────────────────────
1. Title Page
   - Project name, date, author(s)
2. Executive Summary
   - Dataset overview, key findings
3. Dataset Description
   - Columns, types, shape, source
4. Data Cleaning Summary
   - Missing values handled, duplicates removed, outliers flagged
5. Descriptive Statistics
   - Tables: mean, median, std, skewness for all numeric columns
6. Visualizations
   - Embedded charts (histograms, box plots, scatter, pie, heatmap)
7. Correlation Analysis
   - Heatmap + top correlated feature pairs
8. Key Insights & Conclusions
   - Clinical interpretation of findings
9. Appendix
   - Raw vs. cleaned data comparison
```

#### Code Skeleton:
```python
# scripts/report_generator.py
from fpdf import FPDF
import os

class EDAReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'EDA Report — Diabetes HbA1c Data', ln=True, align='C')
        self.ln(5)

    def add_section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(3)

    def add_paragraph(self, text):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 8, text)
        self.ln(3)

    def add_image(self, img_path, caption=''):
        if os.path.exists(img_path):
            self.image(img_path, w=180)
            self.set_font('Arial', 'I', 9)
            self.cell(0, 8, caption, ln=True, align='C')
            self.ln(5)

def generate_report(output_path='outputs/reports/EDA_Final_Report.pdf'):
    pdf = EDAReport()
    pdf.add_page()
    pdf.add_section_title('1. Executive Summary')
    pdf.add_paragraph('This report presents an EDA on the Diabetes HbA1c dataset...')
    # Add more sections, tables, and images programmatically
    pdf.output(output_path)
    print(f"[INFO] Report saved to {output_path}")
```

**Deliverable:** `report_generator.py` + `EDA_Final_Report.pdf`

---

### Phase 8: Frontend Dashboard

**Files:** `frontend/dashboard/app.py` + `frontend/landing/index.html`

**Goal:** Expose the entire EDA through a browser-based interactive interface — no coding required for the end user.

---

#### 8A. Streamlit Interactive Dashboard (`frontend/dashboard/app.py`)

Streamlit is the ideal choice here — it is **pure Python**, reuses all existing `scripts/` modules, and renders rich interactive charts in the browser automatically.

##### Dashboard Sidebar Pages:

| Page | Content |
|---|---|
| 🏠 **Home** | Project title, KPI cards (total records, avg HbA1c, diabetic count) |
| 📥 **Data Explorer** | Preview raw and cleaned data, column types, shape info |
| 📊 **Distributions** | Interactive histograms & box plots with a column selector |
| 🔵 **Scatter Analysis** | Axis-selectable scatter plots coloured by diabetes label |
| 🥧 **Category Breakdown** | Pie/donut charts for Gender, Smoking History, Diabetes |
| 🔥 **Correlation Heatmap** | Interactive Plotly heatmap with hover tooltips |
| 📋 **Statistics Table** | Full descriptive stats table with a CSV download button |
| 📄 **Download Report** | One-click PDF report export |

##### Install & Run:
```bash
pip install streamlit plotly
streamlit run frontend/dashboard/app.py
# Opens at http://localhost:8501
```

##### Code Skeleton:
```python
# frontend/dashboard/app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from scripts.data_loader  import load_data
from scripts.data_cleaner import clean_pipeline
from scripts.statistics   import compute_summary_stats

st.set_page_config(
    page_title="Diabetes HbA1c EDA Dashboard",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
  [data-testid="stSidebar"] { background: #0f1117; }
  .kpi-val { font-size: 2rem; font-weight: 700; color: #00d4ff; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🩸 HbA1c EDA")
page = st.sidebar.radio("Navigate", [
    "🏠 Home", "📥 Data Explorer", "📊 Distributions",
    "🔵 Scatter Analysis", "🥧 Category Breakdown",
    "🔥 Correlation Heatmap", "📋 Statistics Table", "📄 Download Report"
])

@st.cache_data
def get_data():
    df = load_data('data/raw/diabetes_hba1c_raw.csv')
    return clean_pipeline(df)

df = get_data()

if page == "🏠 Home":
    st.title("🩸 Diabetes HbA1c — Exploratory Data Analysis")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Records",     f"{len(df):,}")
    c2.metric("Diabetic Patients",  f"{df['diabetes'].sum():,}")
    c3.metric("Avg HbA1c (%)",     f"{df['hba1c_level'].mean():.2f}")
    c4.metric("Avg Blood Glucose",  f"{df['blood_glucose_level'].mean():.0f} mg/dL")
    st.dataframe(df.head(10), use_container_width=True)

elif page == "📊 Distributions":
    st.title("📊 Feature Distributions")
    col = st.selectbox("Select column", df.select_dtypes(include='number').columns)
    tab1, tab2 = st.tabs(["Histogram", "Box Plot"])
    with tab1:
        fig = px.histogram(df, x=col, color='diabetes', marginal='kde',
                           barmode='overlay', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        fig = px.box(df, x='diabetes', y=col, color='diabetes', template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)

elif page == "🔵 Scatter Analysis":
    st.title("🔵 Scatter Plot Analysis")
    num_cols = df.select_dtypes(include='number').columns.tolist()
    x_col = st.selectbox("X Axis", num_cols, index=num_cols.index('hba1c_level'))
    y_col = st.selectbox("Y Axis", num_cols, index=num_cols.index('blood_glucose_level'))
    fig = px.scatter(df, x=x_col, y=y_col, color='diabetes',
                     opacity=0.6, trendline='ols', template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

elif page == "🥧 Category Breakdown":
    st.title("🥧 Categorical Breakdown")
    cat_col = st.selectbox("Select category", ['diabetes', 'gender', 'smoking_history'])
    fig = px.pie(df, names=cat_col, hole=0.4, template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

elif page == "🔥 Correlation Heatmap":
    st.title("🔥 Correlation Heatmap")
    corr = df.select_dtypes(include='number').corr().round(2)
    fig  = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r',
                     template='plotly_dark', aspect='auto')
    st.plotly_chart(fig, use_container_width=True)

elif page == "📋 Statistics Table":
    st.title("📋 Descriptive Statistics")
    stats = compute_summary_stats(df)
    st.dataframe(stats.style.background_gradient(cmap='Blues'), use_container_width=True)
    st.download_button("⬇️ Download Stats CSV", stats.to_csv().encode(),
                       "statistics.csv", "text/csv")

elif page == "📄 Download Report":
    report_path = 'outputs/reports/EDA_Final_Report.pdf'
    if os.path.exists(report_path):
        with open(report_path, 'rb') as f:
            st.download_button("⬇️ Download PDF Report", f,
                               "EDA_Final_Report.pdf", "application/pdf")
    else:
        st.warning("Run `main.py` first to generate the report.")
```

---

#### 8B. HTML/CSS/JS Landing Page (`frontend/landing/`)

A static, visually premium **landing page** for the project. Suitable for GitHub Pages, academic submissions, or demo presentations.

##### Page Sections:

| Section | Description |
|---|---|
| **Navbar** | Brand logo + nav links + "Launch Dashboard" CTA button |
| **Hero** | Title, tagline, animated KPI floating card, dual CTA buttons |
| **Features** | 6 glassmorphism cards (Cleaning, Stats, Viz, Correlation, Dashboard, Report) |
| **Charts Preview** | Screenshot gallery of key chart outputs |
| **Tech Stack** | Tool logos with hover labels |
| **Footer** | Authors, date, GitHub link |

##### Design System:
- **Font:** `Inter` (Google Fonts) — modern, clean
- **Background:** `#0a0e1a` deep navy
- **Primary accent:** `#00d4ff` electric cyan
- **Secondary:** `#7c3aed` violet
- **Card surface:** `#131929`
- **Effects:** Glassmorphism, radial gradient hero, floating animation, scroll fade-in

##### `index.html` Skeleton:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="EDA on Diabetes HbA1c — interactive dashboard and insights." />
  <title>Diabetes HbA1c EDA | Data Analytics Project</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <nav class="navbar">
    <div class="nav-brand">🩸 HbA1c EDA</div>
    <ul class="nav-links">
      <li><a href="#features">Features</a></li>
      <li><a href="http://localhost:8501" class="btn-nav" target="_blank">Launch Dashboard →</a></li>
    </ul>
  </nav>

  <section class="hero">
    <div class="hero-content">
      <span class="badge">Data Analytics · Healthcare</span>
      <h1>Exploring Diabetes<br/><span class="gradient-text">HbA1c Biomarker Data</span></h1>
      <p>A comprehensive EDA revealing patterns and correlations in real-world patient data.</p>
      <div class="hero-actions">
        <a href="http://localhost:8501" class="btn-primary" target="_blank">🚀 Launch Dashboard</a>
        <a href="../../outputs/reports/EDA_Final_Report.pdf" class="btn-outline" download>📄 Download Report</a>
      </div>
    </div>
    <div class="floating-card">
      <div class="kpi"><span class="kpi-val" id="kpi1">0</span><span class="kpi-lbl">Patient Records</span></div>
      <div class="kpi"><span class="kpi-val">6.5%</span><span class="kpi-lbl">Avg HbA1c</span></div>
      <div class="kpi"><span class="kpi-val">8</span><span class="kpi-lbl">Features Analyzed</span></div>
    </div>
  </section>

  <section class="features" id="features">
    <h2>What This Project Covers</h2>
    <div class="features-grid">
      <div class="feature-card"><div class="icon">🧹</div><h3>Data Cleaning</h3><p>Missing values, duplicates, outliers handled via IQR & median imputation.</p></div>
      <div class="feature-card"><div class="icon">📈</div><h3>Statistics</h3><p>Mean, median, skewness, kurtosis, IQR for every numeric feature.</p></div>
      <div class="feature-card"><div class="icon">📊</div><h3>Visualizations</h3><p>Histograms, box plots, scatter plots, pie charts — auto-generated.</p></div>
      <div class="feature-card"><div class="icon">🔥</div><h3>Correlation</h3><p>Pearson heatmap with top correlated feature-pair ranking.</p></div>
      <div class="feature-card"><div class="icon">🤖</div><h3>Dashboard</h3><p>Interactive Streamlit app — filter, explore, and download in your browser.</p></div>
      <div class="feature-card"><div class="icon">📄</div><h3>PDF Report</h3><p>Auto-generated professional report with all charts and insights embedded.</p></div>
    </div>
  </section>

  <footer class="footer">
    <p>Built with 🐍 Python · Pandas · Seaborn · Streamlit · Plotly</p>
    <p>Diabetes HbA1c EDA Project · 2026</p>
  </footer>
  <script src="main.js"></script>
</body>
</html>
```

##### Key `style.css` Rules:
```css
body { font-family: 'Inter', sans-serif; background: #0a0e1a; color: #e2e8f0; }
.navbar { position: sticky; top: 0; backdrop-filter: blur(12px);
          background: rgba(10,14,26,0.85); border-bottom: 1px solid rgba(255,255,255,0.06); }
.gradient-text { background: linear-gradient(90deg,#00d4ff,#7c3aed);
                 -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.floating-card { animation: float 4s ease-in-out infinite;
                 backdrop-filter: blur(16px); border-radius: 20px; }
@keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-12px)} }
.feature-card { background:#131929; border-radius:16px;
                transition: transform .3s, border-color .3s; }
.feature-card:hover { transform:translateY(-6px); border-color:#00d4ff55; }
.fade-in { opacity:0; transform:translateY(30px); transition:0.6s ease; }
.fade-in.visible { opacity:1; transform:translateY(0); }
```

##### Key `main.js` Script:
```javascript
// Scroll fade-in
const observer = new IntersectionObserver(entries =>
  entries.forEach(e => e.isIntersecting && e.target.classList.add('visible')),
  { threshold: 0.15 }
);
document.querySelectorAll('.feature-card, .hero-content')
  .forEach(el => { el.classList.add('fade-in'); observer.observe(el); });

// KPI counter animation
function animateCounter(el, end, suffix='') {
  let val=0, step=Math.ceil(end/60);
  const t=setInterval(()=>{
    val=Math.min(val+step,end); el.textContent=val.toLocaleString()+suffix;
    if(val>=end) clearInterval(t);
  },20);
}
window.addEventListener('load',()=>{
  animateCounter(document.getElementById('kpi1'), 100000, '+');
});
```

**Deliverable:** `frontend/dashboard/app.py` (Streamlit) + `frontend/landing/index.html`, `style.css`, `main.js`

---



| Module | File | Responsibility |
|---|---|---|
| `data_loader` | `scripts/data_loader.py` | Load CSV, inspect raw data |
| `data_cleaner` | `scripts/data_cleaner.py` | Handle nulls, dups, outliers, type casts |
| `statistics` | `scripts/statistics.py` | Compute descriptive stats |
| `visualizer` | `scripts/visualizer.py` | Generate and save all charts |
| `correlation` | `scripts/correlation.py` | Correlation matrix and analysis |
| `report_generator` | `scripts/report_generator.py` | PDF report compilation |
| `main` | `main.py` | Orchestrate all modules end-to-end |
| `dashboard` | `frontend/dashboard/app.py` | Streamlit interactive web dashboard |
| `landing` | `frontend/landing/index.html` | Static HTML/CSS/JS landing page |

### `main.py` — Entry Point

```python
# main.py
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
    df = load_data(RAW_PATH)
    inspect_data(df)

    # Phase 3: Clean
    df = clean_pipeline(df)
    df.to_csv(CLEANED_PATH, index=False)

    # Phase 4: Stats
    stats = compute_summary_stats(df)
    print(stats)

    # Phase 5: Visualize
    for col in ['hba1c_level', 'age', 'bmi', 'blood_glucose_level']:
        plot_histogram(df, col)
        plot_boxplot(df, col, hue='diabetes')
    plot_scatter(df, 'hba1c_level', 'blood_glucose_level', hue='diabetes')
    plot_pie(df, 'diabetes')
    plot_pie(df, 'gender')
    plot_correlation_heatmap(df)

    # Phase 6: Correlation
    corr_matrix = compute_correlation_matrix(df)
    top = top_correlations(corr_matrix)
    print(top)

    # Phase 7: Report
    generate_report()

    print("\n✅ EDA pipeline complete!")

if __name__ == '__main__':
    run_eda()
```

---

## 6. Dataset Description

The expected dataset (`diabetes_hba1c_raw.csv`) should contain the following columns:

| Column Name | Type | Description |
|---|---|---|
| `gender` | Categorical | Male / Female / Other |
| `age` | Numeric (float) | Age of the patient in years |
| `hypertension` | Binary (0/1) | Whether patient has hypertension |
| `heart_disease` | Binary (0/1) | Whether patient has heart disease |
| `smoking_history` | Categorical | Never / Former / Current / No Info |
| `bmi` | Numeric (float) | Body Mass Index |
| `hba1c_level` | Numeric (float) | Glycated hemoglobin level (%) |
| `blood_glucose_level` | Numeric (int) | Blood glucose in mg/dL |
| `diabetes` | Binary (0/1) | Diabetes diagnosis (target variable) |

> **Source:** The Diabetes Prediction Dataset (publicly available on Kaggle).  
> **Rows:** ~100,000 patients (varies by version).

---

## 7. Deliverables Checklist

| # | Deliverable | Status |
|---|---|---|
| 1 | `requirements.txt` | ⬜ Pending |
| 2 | `README.md` | ⬜ Pending |
| 3 | `data/raw/diabetes_hba1c_raw.csv` | ⬜ Pending |
| 4 | `data/processed/diabetes_hba1c_cleaned.csv` | ⬜ Pending |
| 5 | `scripts/data_loader.py` | ⬜ Pending |
| 6 | `scripts/data_cleaner.py` | ⬜ Pending |
| 7 | `scripts/statistics.py` | ⬜ Pending |
| 8 | `scripts/visualizer.py` | ⬜ Pending |
| 9 | `scripts/correlation.py` | ⬜ Pending |
| 10 | `scripts/report_generator.py` | ⬜ Pending |
| 11 | `main.py` | ⬜ Pending |
| 12 | `notebooks/EDA_Diabetes_HbA1c.ipynb` | ⬜ Pending |
| 13 | All chart `.png` files in `outputs/charts/` | ⬜ Pending |
| 14 | `outputs/reports/EDA_Final_Report.pdf` | ⬜ Pending |
| 15 | `docs/IMPLEMENTATION_PLAN.md` | ✅ Done |
| 16 | `frontend/dashboard/app.py` (Streamlit) | ⬜ Pending |
| 17 | `frontend/landing/index.html` | ⬜ Pending |
| 18 | `frontend/landing/style.css` | ⬜ Pending |
| 19 | `frontend/landing/main.js` | ⬜ Pending |

---

## 8. Non-Functional Requirements

| Requirement | Implementation Strategy |
|---|---|
| **Usability** | Clear function docstrings, notebook with markdown explanations |
| **Reproducibility** | Fixed `random_state`, `requirements.txt`, no hardcoded absolute paths |
| **Modularity** | Each concern is isolated in its own `scripts/*.py` module |
| **Efficiency** | Use Pandas vectorized operations; avoid row-wise loops |
| **Portability** | Relative paths only; runs cross-platform (Windows/Linux/Mac) |

---

## 9. Timeline Estimate

| Phase | Task | Estimated Duration |
|---|---|---|
| 1 | Environment Setup | 0.5 day |
| 2 | Data Ingestion & Loading | 0.5 day |
| 3 | Data Cleaning & Preprocessing | 1 day |
| 4 | Descriptive Statistics | 0.5 day |
| 5 | Data Visualization | 1.5 days |
| 6 | Correlation Analysis | 0.5 day |
| 7 | Report Generation | 1 day |
| 8 | **Frontend Dashboard** (Streamlit + HTML/CSS/JS) | **1.5 days** |
| — | Testing, Review & Documentation | 0.5 day |
| **Total** | | **~7.5 days** |

---

## 10. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Dataset has excessive missing values | Medium | High | Apply robust imputation strategies, document choices |
| Chart rendering issues on headless server | Low | Medium | Use `matplotlib.use('Agg')` backend for non-GUI environments |
| Library version conflicts | Low | Medium | Pin exact versions in `requirements.txt` |
| Outliers skew statistical summaries | High | Medium | Report outliers separately; use median over mean |
| PDF report formatting issues | Low | Low | Test with sample data early; use FPDF2 templates |
| Streamlit port conflict (8501 in use) | Low | Low | Use `--server.port 8502` flag when launching |
| Landing page cross-browser issues | Low | Low | Use standard CSS/JS; test on Chrome & Firefox |

---

*End of Implementation Plan*  
*Prepared for: Diabetes HbA1c EDA Project | Version 2.0 | 2026-07-12*
