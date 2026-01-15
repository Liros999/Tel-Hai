# הערות למרצה - Python Container Assignment

## מטרות הלמידה

1. הבנת מושג Container כסביבה מבודדת
2. עבודה ידנית עם Docker ללא אוטומציה
3. הבנת ההבדל בין Container ל-Image
4. הבנת Reproducibility בסביבות מדעיות

## נקודות חשובות להדגשה

### Container vs Image
- **Image**: תבנית סטטית (read-only)
- **Container**: מופע רץ של Image (read-write)
- כל שינוי ב-Container לא משפיע על ה-Image המקורי

### Reproducibility
- כל התקנה היא בתוך הסביבה המבודדת
- אין זיהום של מערכת המארח
- ניתן לשחזר את הסביבה בדיוק

### שליטה מלאה
- עבודה ידנית מלמדת מה קורה מאחורי הקלעים
- הבנת Dockerfile תהיה קלה יותר אחרי עבודה ידנית

## נקודות קושי צפויות

1. **יציאה מ-Container**: סטודנטים עלולים להתבלבל בין `exit` ל-`Ctrl+D`
2. **נתיבים**: חשוב להדגיש שכל הקבצים נוצרים בתוך ה-Container
3. **התקנות**: pip install צריך להתבצע בתוך ה-Container

## פתרון בעיות נפוצות

### Container לא מתחיל
```bash
docker ps -a  # בדיקת containers קיימים
docker rm python-lab  # מחיקת container ישן
docker run -it --name python-lab python:3.11-slim bash  # יצירה מחדש
```

### חבילות לא נשמרות
- ודא שהסטודנט לא יצא מה-Container לפני שמירה
- הסבר על ההבדל בין Container running ל-stopped

### בעיות הרשאות
- במידה ויש בעיות, ניתן להשתמש ב-`chmod` בתוך ה-Container

## הערכה

### קריטריונים להערכה:
1. יצירת Container בהצלחה
2. התקנת חבילות נדרשות
3. ביצוע כל 5 התרגילים
4. הבנת ההבדל בין Container ל-Image
5. יכולת להפעיל מחדש Container ולמצוא קבצים

### שאלות לבדיקה:
- מה ההבדל בין `docker run` ל-`docker start`?
- איפה נשמרים הקבצים שיצרת?
- מה קורה לחבילות כשאתה יוצא מה-Container?

## המשך הלמידה

לאחר השלמת התרגיל:
1. Python + Volumes (שמירת קבצים מחוץ ל-Container)
2. Python + API (חיבור לשירותים חיצוניים)
3. R Container (אותה מתודולוגיה)
4. Python ↔ R (תקשורת בין containers)

## משאבים נוספים

- [Docker Documentation](https://docs.docker.com/)
- [Python Docker Images](https://hub.docker.com/_/python)
- [Docker Commands Cheat Sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)


