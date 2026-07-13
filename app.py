import matplotlib
matplotlib.use("Agg")  # Force non-GUI backend BEFORE any other matplotlib import

import streamlit as st
import pandas as pd
import plotly.express as px
import sys, os

# Import from local modules
import scripts.data_loader as dl
from scripts.data_cleaner import clean_pipeline
from scripts.statistics   import compute_summary_stats

# ── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Diabetes HbA1c EDA Dashboard",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Sidebar Layout & Styling ── */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important; /* Premium Dark Slate */
        border-right: 1px solid #1e293b !important;
    }
    
    /* Ensure high contrast and readable text colors in sidebar */
    [data-testid="stSidebar"] {
        color: #cbd5e1 !important;
    }
    
    /* Style Navigate Label */
    [data-testid="stSidebar"] label[data-testid="stWidgetLabel"],
    [data-testid="stSidebar"] label[data-testid="stWidgetLabel"] p {
        color: #94a3b8 !important; /* Soft gray-blue */
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        margin-bottom: 0.5rem !important;
    }

    /* Style the main title */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #f8fafc !important;
        font-weight: 700 !important;
        font-size: 1.45rem !important;
        padding-top: 1rem !important;
        margin-bottom: 1.25rem !important;
        border-bottom: 1px solid #1e293b !important;
        padding-bottom: 0.75rem !important;
    }

    /* Style radio option wrappers as interactive buttons */
    [data-testid="stSidebar"] div[role="radiogroup"] {
        gap: 0.4rem !important;
    }
    
    [data-testid="stSidebar"] div[role="radiogroup"] label {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
        margin-bottom: 0.25rem !important;
        cursor: pointer !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        display: flex !important;
        align-items: center !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
    }

    /* Hover states for options */
    [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background-color: #334155 !important;
        border-color: #475569 !important;
        transform: translateY(-1px) !important;
    }
    
    /* Option text color inside button */
    [data-testid="stSidebar"] div[role="radiogroup"] label p {
        color: #e2e8f0 !important; /* High contrast text */
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        margin: 0 !important;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label:hover p {
        color: #ffffff !important;
    }

    /* Selected state highlighting (Royal Blue highlight) */
    [data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
        background-color: #2563eb !important; /* Premium Royal Blue */
        border-color: #3b82f6 !important;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.25), 0 2px 4px -2px rgba(37, 99, 235, 0.25) !important;
    }
    
    [data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    [data-testid="stMainBlockContainer"] {
        max-width: 1400px;
        padding: 2rem 2.5rem 3rem;
    }
    .kpi-card { background: #1e2130; border-radius: 12px;
                padding: 20px; text-align: center; }
    .kpi-value { font-size: 2rem; font-weight: 700; color: #00d4ff; }
    .kpi-label { font-size: 0.9rem; color: #aaa; }
    [data-testid="stMetric"] {
        background: #1e2130;
        border: 1px solid #30364a;
        border-radius: 0.75rem;
        padding: 1rem;
    }
    [data-testid="stMetricLabel"],
    [data-testid="stMetricLabel"] * {
        color: #cbd5e1 !important;
    }
    [data-testid="stMetricValue"],
    [data-testid="stMetricValue"] * {
        color: #f8fafc !important;
    }
    [data-testid="stMetricDelta"],
    [data-testid="stMetricDelta"] * {
        color: #67e8f9 !important;
    }

    @media (max-width: 768px) {
        [data-testid="stSidebar"] {
            max-width: 280px !important;
        }
        [data-testid="stSidebar"] div[role="radiogroup"] label {
            padding: 12px 14px !important;
        }
        [data-testid="stSidebar"] h1 {
            font-size: 1.25rem !important;
        }
        [data-testid="stMainBlockContainer"] {
            padding: 1rem 0.75rem 2rem;
        }
        h1 { font-size: 1.65rem !important; }
        h2 { font-size: 1.35rem !important; }
        h3 { font-size: 1.1rem !important; }
        div[data-testid="stHorizontalBlock"] {
            flex-direction: column;
            gap: 0.75rem;
        }
        div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
            width: 100% !important;
            flex: 1 1 100% !important;
        }
        [data-testid="stMetric"] {
            padding: 0.75rem;
            border-radius: 0.65rem;
        }
        [data-testid="stDataFrame"] {
            font-size: 0.8rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar Navigation ────────────────────────────────────────
st.sidebar.title("🩸 HbA1c EDA")
page = st.sidebar.radio("Navigate", [
    "🏠 Home", "📥 Data Explorer", "📊 Distributions",
    "🔵 Scatter Analysis", "🥧 Category Breakdown",
    "🔥 Correlation Heatmap", "📋 Statistics Table", "📄 Download Report"
])

# ── Load & Cache Data ─────────────────────────────────────────
@st.cache_data
def get_data():
    raw_path = os.path.join(os.path.dirname(__file__), 'data', 'raw', 'diabetes_hba1c_raw.csv')
    try:
        df = dl.load_data(raw_path)
        df_cleaned = clean_pipeline(df).copy()
        if 'diabetes' in df_cleaned.columns:
            df_cleaned['diabetes_label'] = df_cleaned['diabetes'].map({0: 'Negative', 1: 'Positive'})
        return df_cleaned
    except Exception as e:
        st.error(f"Error loading dataset: {e}. Please ensure data is present.")
        return pd.DataFrame()

df = get_data()

if df.empty:
    st.stop()

# ── Pages ─────────────────────────────────────────────────────
if page == "🏠 Home":
    st.title("🩸 Diabetes HbA1c — Exploratory Data Analysis")
    st.markdown("### Key Dataset Metrics")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Records",    f"{len(df):,}")
    if 'diabetes' in df.columns:
        c2.metric("Diabetic Patients", f"{int(df['diabetes'].sum()):,}")
    if 'hba1c_level' in df.columns:
        c3.metric("Avg HbA1c (%)",    f"{df['hba1c_level'].mean():.2f}")
    if 'blood_glucose_level' in df.columns:
        c4.metric("Avg Blood Glucose", f"{df['blood_glucose_level'].mean():.0f} mg/dL")
    st.dataframe(df.head(10), use_container_width=True)

elif page == "📥 Data Explorer":
    st.title("📥 Data Explorer")
    st.write(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    st.markdown("### Cleaned Dataset Preview")
    st.dataframe(df, use_container_width=True)
    
elif page == "📊 Distributions":
    st.title("📊 Feature Distributions")
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) > 0:
        col = st.selectbox("Select column", num_cols)
        tab1, tab2 = st.tabs(["Histogram", "Box Plot"])
        color_col = 'diabetes_label' if 'diabetes_label' in df.columns else None
        
        with tab1:
            fig = px.histogram(df, x=col, color=color_col, marginal='box',
                               barmode='overlay', template='plotly_dark',
                               color_discrete_map={'Negative': '#00d4ff', 'Positive': '#ff4b4b'})
            st.plotly_chart(fig, use_container_width=True)
        with tab2:
            fig = px.box(df, x=color_col, y=col, color=color_col,
                         template='plotly_dark', 
                         color_discrete_map={'Negative': '#00d4ff', 'Positive': '#ff4b4b'})
            st.plotly_chart(fig, use_container_width=True)

elif page == "🔵 Scatter Analysis":
    st.title("🔵 Scatter Plot Analysis")
    num_cols = df.select_dtypes(include='number').columns.tolist()
    if len(num_cols) >= 2:
        default_x = num_cols.index('hba1c_level') if 'hba1c_level' in num_cols else 0
        default_y = num_cols.index('blood_glucose_level') if 'blood_glucose_level' in num_cols else 1
        x_col = st.selectbox("X Axis", num_cols, index=default_x)
        y_col = st.selectbox("Y Axis", num_cols, index=default_y)
        color_col = 'diabetes_label' if 'diabetes_label' in df.columns else None
        fig = px.scatter(df, x=x_col, y=y_col, color=color_col,
                         opacity=0.6, template='plotly_dark',
                         color_discrete_map={'Negative': '#00d4ff', 'Positive': '#ff4b4b'})
        st.plotly_chart(fig, use_container_width=True)

elif page == "🥧 Category Breakdown":
    st.title("🥧 Categorical Breakdown")
    cat_cols = df.select_dtypes(exclude='number').columns.tolist()
    if 'diabetes_label' in df.columns:
        cat_cols.append('diabetes_label')
    if cat_cols:
        cat_col = st.selectbox("Select category", cat_cols, index=cat_cols.index('diabetes_label') if 'diabetes_label' in cat_cols else 0)
        fig = px.pie(df, names=cat_col, hole=0.4, template='plotly_dark',
                     color=cat_col, color_discrete_map={'Negative': '#00d4ff', 'Positive': '#ff4b4b'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No categorical variables available.")

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
    csv = stats.to_csv().encode('utf-8')
    st.download_button("⬇️ Download Stats CSV", csv, "statistics.csv", "text/csv")

elif page == "📄 Download Report":
    st.title("📄 Download EDA Report")
    st.markdown("Download the PDF report generated by standard EDA pipeline. Please run `run_pipeline.py` first.")
    report_path = os.path.join(os.path.dirname(__file__), 'outputs', 'reports', 'EDA_Final_Report.pdf')
    if os.path.exists(report_path):
        with open(report_path, 'rb') as f:
            st.download_button("⬇️ Download PDF Report", f, "EDA_Final_Report.pdf", "application/pdf")
    else:
        st.warning("Report not yet generated. Run `python main.py` first in the terminal.")
