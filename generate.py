import pandas as pd
import numpy as np

# Generate sample data
data = {
    'ID': range(1, 101),
    'Value': np.random.normal(100, 15, 100),
    'Category': np.random.choice(['A', 'B', 'C'], 100),
    'Timestamp': pd.date_range('2024-01-01', periods=100, freq='D')
}

df = pd.DataFrame(data)

# Save to CSV in the data folder
output_path = '/data/result.csv'
df.to_csv(output_path, index=False)

print(f"Data generated successfully!")
print(f"Output saved to: {output_path}")
print(f"\nData preview:")
print(df.head())
print(f"\nData shape: {df.shape}")
print(f"\nStatistics:")
print(df.describe())

