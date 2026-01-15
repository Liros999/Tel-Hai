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


