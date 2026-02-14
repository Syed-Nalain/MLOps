import pandas as pd
import os
from sklearn.model_selection import train_test_split

def preprocess():
    input_path = "data/raw/titanic.csv"
    train_path = "data/processed/train.csv"
    test_path = "data/processed/test.csv"
    
    os.makedirs("data/processed", exist_ok=True)
    
    df = pd.read_csv(input_path)
    
    # Handle missing values
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    df['Fare'].fillna(df['Fare'].median(), inplace=True) # Usually for test set but good practice
    
    # Drop Cabin as it has too many missing values
    df.drop(columns=['Cabin'], inplace=True)
    
    # Encode categorical variables
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    
    # Select features and target
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    target = 'Survived'
    
    # Split into train and test
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    print("Preprocessing complete.")

if __name__ == "__main__":
    preprocess()
