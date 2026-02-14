import pandas as pd
import os

def generate_features():
    train_input = "data/processed/train.csv"
    test_input = "data/processed/test.csv"
    train_output = "features/train_features.csv"
    test_output = "features/test_features.csv"
    
    os.makedirs("features", exist_ok=True)
    
    def add_features(df):
        df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
        df['IsAlone'] = 0
        df.loc[df['FamilySize'] == 1, 'IsAlone'] = 1
        return df
    
    train_df = pd.read_csv(train_input)
    test_df = pd.read_csv(test_input)
    
    train_df = add_features(train_df)
    test_df = add_features(test_df)
    
    train_df.to_csv(train_output, index=False)
    test_df.to_csv(test_output, index=False)
    print("Feature engineering complete.")

if __name__ == "__main__":
    generate_features()
