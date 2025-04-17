import pandas as pd
import random

symptoms = ['fever', 'cough', 'fatigue', 'headache', 'runny_nose', 'sore_throat', 'nausea', 'diarrhea']
diseases = ['flu', 'cold', 'allergy', 'food_poisoning', 'covid']

# Generate 200 random samples
data = []
for _ in range(200):
    entry = {symptom: random.randint(0, 1) for symptom in symptoms}

    # Rule-based assignment for demo purpose
    if entry['fever'] and entry['cough'] and entry['fatigue']:
        disease = 'flu'
    elif entry['sore_throat'] and entry['runny_nose']:
        disease = 'cold'
    elif entry['runny_nose'] and not entry['fever']:
        disease = 'allergy'
    elif entry['nausea'] and entry['diarrhea']:
        disease = 'food_poisoning'
    elif entry['fever'] and entry['cough'] and entry['headache']:
        disease = 'covid'
    else:
        disease = random.choice(diseases)

    entry['disease'] = disease
    data.append(entry)

# Convert to DataFrame
df = pd.DataFrame(data)
#save to CSV
df.to_csv('synptom_dataset.csv', index=False)
print("Random dataset saved to symptom_data.csv")