import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

data = pd.read_url('final.csv')

data.shape
X = data.drop(columns=['HeartDisease'], axis=1)
Y = data['HeartDisease']
#print(X,Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=42)

model = LogisticRegression()
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of Testing Data :",accuracy*100)

with open('model_pickle','wb') as f:
    pickle.dump(model, f)
