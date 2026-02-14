import pandas as pd
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate():
    predictions_path = "results/predictions.csv"
    test_labels_path = "features/test_features.csv"
    metrics_path = "results/metrics.txt"
    
    preds = pd.read_csv(predictions_path)
    truth = pd.read_csv(test_labels_path)
    
    # Ensure IDs match
    merged = pd.merge(preds, truth[['PassengerId', 'Survived']], on='PassengerId', suffixes=('_pred', '_true'))
    
    y_pred = merged['Survived_pred']
    y_true = merged['Survived_true']
    
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    
    with open(metrics_path, "w") as f:
        f.write(f"Accuracy: {accuracy:.4f}\n")
        f.write(f"Precision: {precision:.4f}\n")
        f.write(f"Recall: {recall:.4f}\n")
        f.write(f"F1 Score: {f1:.4f}\n")
        
    print("Evaluation complete. Metrics saved.")

if __name__ == "__main__":
    evaluate()
