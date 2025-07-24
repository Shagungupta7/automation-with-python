# 📊 PDF Table Extractor & Visualizer

This project extracts tabular data from a PDF using Camelot, cleans and transforms the data using `pandas`, and visualizes it using `seaborn`.

---

## 📄 Project Description

Given a PDF file containing structured tables, this script:

1. Extracts tables from specific pages using the **lattice** method (suitable for PDFs with visible table borders).  
2. Selects and cleans the required portion of a table (e.g., literacy rates).  
3. Converts the data into a `DataFrame` and exports it to `.csv` and `.xlsx`.  
4. Transforms the data into long format and plots a grouped bar chart to show comparisons over the years.

---

## 🛠️ Requirements

Install dependencies via pip:

```bash
pip install "camelot-py[cv]"
pip install pandas seaborn
