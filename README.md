# 🏭 IOT – Predictive Maintenance System

## 📌 Project Overview
FactoryGuard AI is a machine learning-based predictive maintenance system designed to forecast machine failures within the next 24 hours using telemetry sensor data.

The objective is to minimize unexpected breakdowns and reduce downtime by prioritizing high-recall predictive models.

---

## 🎯 Business Objective
- Predict machine failure within next 24 hours
- Reduce false negatives (missed failures)
- Optimize maintenance scheduling
- Improve operational reliability

---

## 📂 Dataset Description

The dataset consists of telemetry sensor readings including:

- Volt
- Rotate
- Pressure
- Vibration
- MachineID
- Datetime
- Failure indicator (Target variable: `failure_next_24h`)

---

# 📅 Week 1 – Data Engineering & EDA

## 🔹 Tasks Performed
- Data Cleaning
- Handling Missing Values (Interpolation + Forward/Backward Fill)
- Exploratory Data Analysis
- Feature Preparation
- Target Variable Engineering (`failure_next_24h`)
- Dataset Merging ( multiple sources used)

## 🔹 Key Learnings
- Identified class imbalance
- Understood sensor behavior before failure
- Prepared modeling-ready dataset

---

# 📅 Week 2 – Modeling & Hyperparameter Tuning

## 🎯 Goal
Beat baseline model and improve Recall & F1-Score.

---

## 🤖 Models Implemented

### 1️⃣ Random Forest Classifier
- Used class_weight = 'balanced'
- Baseline tree-based model

### 2️⃣ XGBoost Classifier
- High-performance gradient boosting model
- Used scale_pos_weight to handle imbalance

---

## 🔍 Hyperparameter Optimization

- Used RandomizedSearchCV
- Optimized:
  - n_estimators
  - max_depth
  - learning_rate
  - subsample
  - colsample_bytree

---

## 📊 Evaluation Metrics

We prioritized:

- ✅ F1-Score
- ✅ Recall (Minimizing False Negatives)
- ❌ Not Accuracy (due to class imbalance)

---

## 🧠 Why Recall is Important?

In predictive maintenance:
- Missing a failure (False Negative) is costlier than false alarm.
- Therefore, Recall is prioritized over Accuracy.

---

## 🔄 ML Pipeline Flow

1. Data Cleaning
2. Feature Engineering
3. Train-Test Split
4. Handle Class Imbalance
5. Model Training
6. Hyperparameter Tuning
7. Final Evaluation

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Matplotlib / Seaborn

---

## 📈 Future Improvements

- SMOTE for imbalance handling
- Time-series feature engineering
- Rolling window statistics
- SHAP for explainability
- Deployment using Flask / FastAPI

---

Folder Structure

IoT-Predictive-Maintenance-Engine/
│
├── data/
├── notebooks/
│   ├── IoT-Predictive-Maintenance-Engine.ipynb
│ 
├── src/
├── README.md

## ⭐ Key Takeaway

This project demonstrates end-to-end predictive modeling with emphasis on:
- Business-oriented metric selection
- Handling imbalanced classification
- Hyperparameter optimization
- Industry-grade ML pipeline
## 👩‍💻 Author

Sneha  & Team
Machine Learning & Data Science Enthusiast  

---
