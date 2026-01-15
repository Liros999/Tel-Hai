import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Score': np.random.randint(60, 100, 5)
}

df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)
print("CSV file saved as students.csv")
print(df)


