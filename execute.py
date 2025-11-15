import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Calculate total revenue (typo here!)
total_revenue = df['revenue'].sum()

# Output result
result = {
    'total_revenue': total_revenue,
    'count': len(df)
}

print(json.dumps(result))
