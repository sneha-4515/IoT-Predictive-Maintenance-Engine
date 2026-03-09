import joblib
import shap
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

def main():
    print("Generating dummy sensor data...")
    # 10 sensor features, 1000 samples
    X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
    feature_names = [f"sensor_{i}" for i in range(10)]
    X_df = pd.DataFrame(X, columns=feature_names)

    print("Training RandomForest model...")
    model = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
    model.fit(X_df, y)

    print("Creating SHAP explainer...")
    explainer = shap.TreeExplainer(model)

    print("Serializing model and explainer...")
    joblib.dump(model, 'model.joblib')
    joblib.dump(explainer, 'explainer.joblib')
    
    # Also save the expected feature names to ensure order is correct during prediction
    joblib.dump(feature_names, 'feature_names.joblib')

    print("Done! model.joblib, explainer.joblib, and feature_names.joblib have been created.")

if __name__ == "__main__":
    main()
