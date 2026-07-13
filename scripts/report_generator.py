from fpdf import FPDF
import os

class EDAReport(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 14)
        self.cell(0, 10, 'EDA Report - Diabetes HbA1c Data', ln=True, align='C')
        self.ln(5)

    def add_section_title(self, title):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(3)

    def add_paragraph(self, text):
        self.set_font('Helvetica', '', 10)
        self.multi_cell(0, 8, text)
        self.ln(3)

    def add_image(self, img_path, caption=''):
        if os.path.exists(img_path):
            self.image(img_path, w=170)
            self.set_font('Helvetica', 'I', 9)
            self.cell(0, 8, caption, ln=True, align='C')
            self.ln(5)

def generate_report(output_path='outputs/reports/EDA_Final_Report.pdf'):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf = EDAReport()
    pdf.add_page()
    
    pdf.add_section_title('1. Executive Summary')
    pdf.add_paragraph('This report presents an Exploratory Data Analysis (EDA) on the Diabetes HbA1c dataset. It covers data cleaning, descriptive statistics, visual analysis, and correlation discoveries.')
    
    pdf.add_section_title('2. Analysis Pipeline Overview')
    pdf.add_paragraph('The raw dataset was cleaned using median/mode imputation and deduplication. Outliers were detected but retained for accurate clinical distribution mapping.')
    
    pdf.add_section_title('3. Data Visualizations')
    pdf.add_paragraph('Below are generated visualizations derived from the processed data:')
    
    # Try adding a sample heat map if it exists
    heatmap_path = 'outputs/charts/heatmaps/correlation_heatmap.png'
    if os.path.exists(heatmap_path):
        pdf.add_image(heatmap_path, 'Correlation Heatmap')
        
    hist_path = 'outputs/charts/histograms/hba1c_level_histogram.png'
    if os.path.exists(hist_path):
        pdf.add_image(hist_path, 'HbA1c Level Distribution')
        
    pdf.output(output_path)
    print(f"[INFO] PDF Report saved to {output_path}")
