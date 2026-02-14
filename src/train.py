import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestClassifier

def train_model():
    input_path = "features/train_features.csv"
    model_path = "models/model.pkl"
    
    os.makedirs("models", exist_ok=True)
    
    df = pd.read_csv(input_path)
    X = df.drop(columns=['Survived', 'Name', 'Ticket', 'PassengerId'])
    y = df['Survived']
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print("Model training complete.")

if __name__ == "__main__":
    train_model()
