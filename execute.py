import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Calculate total revenew (typo here!)
total_revenew = df['revenue'].sum()

# Output result
result = {
    'total_revenue': total_revenew,
    'count': len(df)
}

print(json.dumps(result))
