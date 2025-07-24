📊 PDF Table Extractor & Visualizer
This project extracts tabular data from a PDF using Camelot, cleans and transforms the data using pandas, and visualizes it using seaborn.

📄 Project Description
Given a PDF file containing structured tables, this script:

Extracts tables from specific pages using the lattice method (suitable for PDFs with visible table borders).

Selects and cleans the required portion of a table (e.g., literacy rates).

Converts the data into a DataFrame and exports it to .csv and .xlsx.

Transforms the data into long format and plots a grouped bar chart to show comparisons over the years.

🛠️ Requirements
Install dependencies via pip:

bash
Copy
Edit
pip install camelot-py[cv]
pip install pandas
pip install seaborn
⚠️ Camelot requires:

Ghostscript

Tkinter (GUI backend)
Make sure these are installed in your environment. See Camelot installation guide.

📁 Input
PDF: india_factsheet_economic_n_hdi.pdf
A factsheet containing Human Development Indicators including Literacy Rates from 2001 and 2011.

🧾 Output
CSV: packt_output.csv

Excel: table_from_pdf.xlsx

Plot: Barplot comparing literacy rates (overall, male, female) between 2001 and 2011

📈 Example Chart
The generated plot shows:

X-axis: Literacy KPI (e.g., Male Literacy Rate)

Y-axis: Percentage (%)

Hue: Year (2001 vs. 2011)

📜 Usage
bash
Copy
Edit
python your_script.py
📂 Files
File	Description
india_factsheet_economic_n_hdi.pdf	Source PDF for extraction
packt_output.csv	Cleaned table saved as CSV
table_from_pdf.xlsx	Cleaned table saved as Excel
your_script.py	Python script performing all steps

✅ Features Covered
📥 PDF scraping using Camelot

🔍 Table extraction and filtering

📤 Export to CSV/Excel

📊 Visualization with Seaborn