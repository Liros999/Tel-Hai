import pandas as pd

df = pd.read_csv('students.csv')
print("Data from CSV:")
print(df)
print("\nStatistics:")
print(df.describe())


