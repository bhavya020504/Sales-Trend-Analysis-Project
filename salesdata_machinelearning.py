import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# STEP 1: Load your dataset
df = pd.read_csv(r"C:\Users\vimal\Downloads\sales_data.csv")
  # Replace with your actual file name

# STEP 2: Clean column names (lowercase and replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# STEP 3: Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# STEP 4: Create 'order_month' column for trend analysis
df['order_month'] = df['order_date'].dt.to_period('M')

# STEP 5: Drop rows with missing dates or sales
df.dropna(subset=['order_date', 'total_sales'], inplace=True)

# STEP 6: Convert relevant columns to numeric (if needed)
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['price_per_unit'] = pd.to_numeric(df['price_per_unit'], errors='coerce')
df['total_sales'] = pd.to_numeric(df['total_sales'], errors='coerce')

# STEP 7: Drop rows with any remaining null values in important columns
df.dropna(subset=['quantity', 'price_per_unit', 'total_sales'], inplace=True)

# STEP 8: Encode categorical variables using one-hot encoding
df = pd.get_dummies(df, columns=['product_category', 'region'], drop_first=True)

# STEP 9: Select features (X) and target (y)
feature_cols = [col for col in df.columns if col not in ['order_id', 'order_date', 'order_month', 'total_sales']]
X = df[feature_cols]
y = df['total_sales']

# STEP 10: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# STEP 11: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# STEP 12: Predict on the test set
y_pred = model.predict(X_test)

# STEP 13: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# STEP 14: Print results
print("Mean Squared Error (MSE):", mse)
print("R-squared (R²):", r2)

# OPTIONAL: Print the feature importance (coefficients)
coefficients = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_})
print("\nFeature Importances:")
print(coefficients.sort_values(by='Coefficient', key=abs, ascending=False))
