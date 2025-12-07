import pandas as pd
import os

# this program cleans a messy sales data file.

# --- file paths ---
# setting up the file locations
RAW_PATH = 'data/raw/sales_data_raw.csv'
CLEANED_PATH = 'data/processed/sales_data_clean.csv'

if __name__ == '__main__':
    print('starting data cleaning...')

    # 1. load data
    # reading the raw csv file into a pandas dataframe
    df = pd.read_csv(RAW_PATH)
    
    # 2. clean column names
    # making column names easy to use (lowercase and underscores)
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_', regex=False)
    # this line removes any leftover non-standard characters like slashes or hyphens
    df.columns = df.columns.str.replace('[^a-z0-9_]', '', regex=True)
    
    # 3. handle text whitespace
    # removing extra spaces from product and category names
    df['prodname'] = df['prodname'].str.strip()
    df['category'] = df['category'].str.strip()

    # 4. convert columns to numeric
    # making sure price and qty are treated as numbers so we can compare them later
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

    # 5. handle missing critical values
    # removing rows that are missing price or quantity (including those that turned into NaN in step 4)
    df.dropna(subset=['price', 'qty'], inplace=True)
    
    # 6. remove invalid rows (negative numbers)
    # keeping only rows where price and quantity are zero or positive
    df = df[(df['price'] >= 0) & (df['qty'] >= 0)]

    # 7. save data
    # creating the processed folder if it doesn't exist
    os.makedirs(os.path.dirname(CLEANED_PATH) or '.', exist_ok=True)
    
    # saving the cleaned table
    df.to_csv(CLEANED_PATH, index=False)
    
    print('\ndata cleaning complete.')
    print('cleaned file saved to:', CLEANED_PATH)
    print('\nfirst 5 rows of cleaned data:')
    print(df.head())