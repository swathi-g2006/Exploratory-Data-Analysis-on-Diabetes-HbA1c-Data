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
    [data-testid="stSidebar"] { background: #0f1117; }
    [data-testid="stMainBlockContainer"] {
        max-width: 1400px;
        padding: 2rem 2.5rem 3rem;
    }
    .kpi-card { background: #1e2130; border-radius: 12px;
                padding: 20px; text-align: center; }
    .kpi-value { font-size: 2rem; font-weight: 700; color: #00d4ff; }
    .kpi-label { font-size: 0.9rem; color: #aaa; }

    @media (max-width: 768px) {
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
            border-radius: 0.5rem;
            background: #1e2130;
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
        df_cleaned = clean_pipeline(df)
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
    st.dataframe(df.head(10), width="stretch")

elif page == "📥 Data Explorer":
    st.title("📥 Data Explorer")
    st.write(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    st.markdown("### Cleaned Dataset Preview")
    st.dataframe(df, width="stretch")
    
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
            st.plotly_chart(fig, width="stretch")
        with tab2:
            fig = px.box(df, x=color_col, y=col, color=color_col,
                         template='plotly_dark', 
                         color_discrete_map={'Negative': '#00d4ff', 'Positive': '#ff4b4b'})
            st.plotly_chart(fig, width="stretch")

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
        st.plotly_chart(fig, width="stretch")

elif page == "🥧 Category Breakdown":
    st.title("🥧 Categorical Breakdown")
    cat_cols = df.select_dtypes(exclude='number').columns.tolist()
    if 'diabetes_label' in df.columns:
        cat_cols.append('diabetes_label')
    if cat_cols:
        cat_col = st.selectbox("Select category", cat_cols, index=cat_cols.index('diabetes_label') if 'diabetes_label' in cat_cols else 0)
        fig = px.pie(df, names=cat_col, hole=0.4, template='plotly_dark',
                     color=cat_col, color_discrete_map={'Negative': '#00d4ff', 'Positive': '#ff4b4b'})
        st.plotly_chart(fig, width="stretch")
    else:
        st.write("No categorical variables available.")

elif page == "🔥 Correlation Heatmap":
    st.title("🔥 Correlation Heatmap")
    corr = df.select_dtypes(include='number').corr().round(2)
    fig  = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r',
                     template='plotly_dark', aspect='auto')
    st.plotly_chart(fig, width="stretch")

elif page == "📋 Statistics Table":
    st.title("📋 Descriptive Statistics")
    stats = compute_summary_stats(df)
    st.dataframe(stats.style.background_gradient(cmap='Blues'), width="stretch")
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
