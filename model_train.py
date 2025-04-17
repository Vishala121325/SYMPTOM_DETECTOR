import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

#load dataset 
df = pd.read_csv('synptom_dataset.csv')

#Encode target labels
le = LabelEncoder()
df['disease'] = le.fit_transform(df['disease'])

#save labels encoder for decoring predictions label
with open('label_encoder.pkl','wb') as f:
    pickle.dump(le, f)
    
#train-test split
x = df.drop('disease', axis=1)
y= df['disease']
X_train, X_test, y_train, y_test = train_test_split( x, y, test_size=0.2, random_state=42)

#train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

#save model
with open('symptom_model.pkl', 'wb') as f:
    pickle.dump(model, f)
    
print("Logistic Regression model trained and saved.")