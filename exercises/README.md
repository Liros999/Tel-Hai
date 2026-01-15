# תרגילי חובה - Python Container

## תרגיל 1: הוסף matplotlib ושרטט גרף

צור קובץ `plot_example.py`:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sine Wave')
plt.legend()
plt.grid(True)
plt.savefig('sine_wave.png')
print("Graph saved as sine_wave.png")
```

הרצה:
```bash
python plot_example.py
```

---

## תרגיל 2: שמור CSV

צור קובץ `save_csv.py`:

```python
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
```

הרצה:
```bash
python save_csv.py
```

---

## תרגיל 3: קרא CSV

צור קובץ `read_csv.py`:

```python
import pandas as pd

df = pd.read_csv('students.csv')
print("Data from CSV:")
print(df)
print("\nStatistics:")
print(df.describe())
```

הרצה:
```bash
python read_csv.py
```

---

## תרגיל 4: צור קובץ JSON

צור קובץ `create_json.py`:

```python
import json

data = {
    "experiment": {
        "name": "Temperature Measurement",
        "date": "2024-01-15",
        "samples": [20.5, 21.2, 22.1, 20.8, 21.5],
        "unit": "celsius",
        "location": "Lab A"
    },
    "metadata": {
        "researcher": "Student Name",
        "equipment": "Thermometer Model X"
    }
}

with open('experiment_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("JSON file saved as experiment_data.json")
print(json.dumps(data, indent=4, ensure_ascii=False))
```

הרצה:
```bash
python create_json.py
```

---

## תרגיל 5: התקן חבילה חדשה (seaborn)

```bash
pip install seaborn
```

צור קובץ `seaborn_example.py`:

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'category': np.random.choice(['A', 'B', 'C'], 100)
})

plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='x', y='y', hue='category')
plt.title('Seaborn Scatter Plot')
plt.savefig('seaborn_plot.png')
print("Seaborn plot saved as seaborn_plot.png")
```

הרצה:
```bash
python seaborn_example.py
```

---

## בדיקות סופיות

לאחר השלמת כל התרגילים, ודא שיש לך:

- [ ] קובץ גרף (PNG)
- [ ] קובץ CSV
- [ ] קובץ JSON
- [ ] seaborn מותקן ומריץ קוד
- [ ] כל הקבצים נשמרו בתוך ה-container

בדיקה:
```bash
ls -la /app
```


