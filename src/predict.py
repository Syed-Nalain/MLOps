import pandas as pd
import pickle
import os

def predict():
    model_path = "models/model.pkl"
    input_path = "features/test_features.csv"
    output_path = "results/predictions.csv"
    
    os.makedirs("results", exist_ok=True)
    
    with open(model_path, "rb") as f:
        model = pickle.load(f)
        
    df = pd.read_csv(input_path)
    X = df.drop(columns=['Survived', 'Name', 'Ticket', 'PassengerId'])
    
    predictions = model.predict(X)
    
    pd.DataFrame({'PassengerId': df['PassengerId'], 'Survived': predictions}).to_csv(output_path, index=False)
    print("Predictions saved.")

if __name__ == "__main__":
    predict()
