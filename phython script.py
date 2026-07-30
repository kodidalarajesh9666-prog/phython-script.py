import pandas as pd
import matplotlib.pyplot as plt

# --- STEP 0: Create Sample CSV Data (For Demonstration) ---
# Skip this step if you already have your own sales_data.csv file
sample_data = {
    'Date': ['2026-01-01', '2026-01-01', '2026-01-02', '2026-01-02', '2026-01-03'],
    'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse'],
    'Region': ['North', 'East', 'North', 'West', 'East'],
    'Sales': [1200, 50, 1200, 80, 50]
}
df_mock = pd.DataFrame(sample_data)
df_mock.to_csv('sales_data.csv', index=False)


# --- STEP 1: Load CSV using Pandas ---
# Replace 'sales_data.csv' with your actual file path if needed
df = pd.read_csv('sales_data.csv')

print("--- First 5 Rows of Data ---")
print(df.head())
print("\n" + "="*40 + "\n")


# --- STEP 2: Use groupby() and sum() ---
# Grouping sales data by Product to find total revenue per item
product_sales = df.groupby('Product')['Sales'].sum()

print("--- Total Sales by Product ---")
print(product_sales)
print("\n" + "="*40 + "\n")


# --- STEP 3: Use plot() to generate charts ---
# Creating a bar chart for product sales
plt.figure(figsize=(8, 5))
product_sales.plot(kind='bar', color='skyblue', edgecolor='black')

# Adding visual labels and titles
plt.title('Total Revenue by Product', fontsize=14, fontweight='bold')
plt.xlabel('Product Name', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
plt.tight_layout()
plt.show()