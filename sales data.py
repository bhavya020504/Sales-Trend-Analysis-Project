import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv(r"C:\Users\vimal\Downloads\sales_data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Drop rows with missing dates (if any)
df = df.dropna(subset=['order_date'])

# Extract month
df['order_month'] = df['order_date'].dt.to_period('M')

# Group by month and sum total sales
monthly_sales = df.groupby('order_month')['total_sales'].sum().reset_index()

# Convert period to string for plotting
monthly_sales['order_month'] = monthly_sales['order_month'].astype(str)

# Plot the monthly sales trend
plt.figure(figsize=(10, 5))
sns.lineplot(x='order_month', y='total_sales', data=monthly_sales, marker='o')
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
