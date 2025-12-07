# ism2411-data-cleaning-copilot

A small project in Python that showcases basic data cleaning using the pandas library on a messy sales dataset. This project has been developed as an assignment by using GitHub Copilot for code generation and refinement.

Project Objective

Transform the raw sales data (`data/raw/sales_data_raw.csv`) into a structured, clean dataset (`data/processed/sales_data_clean.csv`), ready for analysis.
Required Cleaning Steps
 Standardize column names (lowercase, snake_case)
 Strip whitespace from categorical columns.

 Handle missing values for critical sales metrics: Price, Quantity.
 Remove rows with clearly invalid, negative values.
How to Run
1. Ensure you have Python and pandas installed (`pip install pandas`).
 2. Run the main cleaning script from the root of the project: ```bash python src/data_cleaning.py