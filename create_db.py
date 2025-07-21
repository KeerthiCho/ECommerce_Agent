import pandas as pd
import sqlite3

# Load your CSVs
df_ads = pd.read_csv('ad_sales.csv')
df_total = pd.read_csv('total_sales.csv')
df_eligibility = pd.read_csv('eligibility.csv')

# Connect to SQLite database
conn = sqlite3.connect('ecommerce.db')

# Save each DataFrame to a SQL table
df_ads.to_sql('ad_sales', conn, if_exists='replace', index=False)
df_total.to_sql('total_sales', conn, if_exists='replace', index=False)
df_eligibility.to_sql('eligibility', conn, if_exists='replace', index=False)

conn.close()

print("✅ Database created successfully.")
