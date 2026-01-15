# Python Container – Manual Install & Run (Codespaces)

## Overview
- ✔ בלי Dockerfile
- ✔ בלי DevContainer
- ✔ הכל ידני
- ✔ שליטה מלאה
- ✔ הכנה מושלמת ל-R בהמשך

## 🧠 מה אנחנו מדגימים?
- מה זה Container
- איך נכנסים אליו
- איך מתקינים Python Packages
- איך מריצים קוד
- למה זה Reproducible

---

## 🧱 STEP 0 – פתיחת Codespaces

1. פתח Repository כלשהו (ריק זה בסדר)
2. Code → Codespaces → Create codespace
3. פתח Terminal
4. בדיקה:
```bash
docker --version
```

---

## 🐳 STEP 1 – יצירת Python Container אינטראקטיבי

```bash
docker run -it --name python-lab python:3.11-slim bash
```

✔ עכשיו אתה בתוך Container  
✔ זו סביבת Linux מבודדת  
✔ Python כבר מותקן

בדיקה:
```bash
python --version
```

---

## 📦 STEP 2 – בדיקת pip והתקנת חבילות

```bash
pip --version
```

התקנת חבילות מדעיות:
```bash
pip install numpy pandas matplotlib scipy
```

בדיקה:
```bash
python -c "import numpy, pandas, matplotlib, scipy; print('OK')"
```

---

## 📁 STEP 3 – יצירת קוד Python בתוך Container

```bash
mkdir /app
cd /app
nano main.py
```

### ✏️ main.py
```python
import numpy as np
import pandas as pd

data = pd.DataFrame({
    "x": np.arange(10),
    "y": np.random.randn(10)
})
print(data)
```

הרצה:
```bash
python main.py
```

---

## 🧪 STEP 4 – ניסוי מדעי קטן

```bash
nano experiment.py
```

```python
import numpy as np

samples = np.random.normal(100, 15, 1000)
print("Mean:", samples.mean())
print("Std:", samples.std())
```

```bash
python experiment.py
```

---

## 🔁 STEP 5 – עצירה והפעלה מחדש

יציאה מה־container:
```bash
exit
```

בדיקה:
```bash
docker ps -a
```

הפעלה מחדש:
```bash
docker start python-lab
docker attach python-lab
```

✔ כל החבילות נשמרו  
✔ הסביבה נשמרה

---

## 🧠 מה חשוב להדגיש לסטודנטים?

- Container ≠ Image
- כל התקנה היא בתוך הסביבה
- אין זיהום מערכת
- זה Reproducible
- Dockerfile הוא רק אוטומציה של מה שעשינו ידנית

---

## 🧪 תרגילי חובה (לפני R)

1. הוסף matplotlib ושרטט גרף
2. שמור CSV
3. קרא CSV
4. צור קובץ JSON
5. התקן חבילה חדשה (seaborn)

---

## 🔜 השלב הבא (רק אחרי שמבינים את זה)

- ➡️ Python + Volumes
- ➡️ Python + API
- ➡️ R Container – בדיוק באותה צורה
- ➡️ Python ↔ R


