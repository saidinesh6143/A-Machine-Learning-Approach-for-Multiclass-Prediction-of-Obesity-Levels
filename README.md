# 🧠 A Machine Learning Approach for Multiclass Prediction of Obesity Levels

## 📌 Description
This project presents a Machine Learning-based system for predicting multiple levels of obesity using physiological and lifestyle data. Unlike traditional approaches that classify individuals as simply obese or non-obese, this system provides a detailed multiclass classification of obesity levels.

The system takes user inputs such as age, height, weight, BMI, dietary habits, and physical activity levels, and predicts the corresponding obesity category. This helps in early detection and preventive healthcare by enabling individuals to understand their health risks.

The project integrates Machine Learning models into a user-friendly framework, making it accessible for both healthcare professionals and individuals.

---

## 📊 Dataset
The dataset used in this project is sourced from:
- Kaggle Obesity Risk Prediction Dataset

### Dataset Details:
- Total Records: 2,111
- Total Features: 17

### Features Include:
- Age, Gender
- Height, Weight, BMI
- Eating habits and diet patterns
- Physical activity levels
- Water intake
- Smoking and lifestyle behaviors

The dataset undergoes preprocessing steps such as:
- Handling missing values
- Encoding categorical variables
- Normalization of features
- Feature selection using XGBoost importance

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Cleaning and handling missing values
- Feature selection using XGBoost
- Encoding categorical data
- Normalizing numerical features

### 2. Train-Test Split
- Dataset divided into training and testing sets
- Ensures model generalization and avoids overfitting

### 3. Model Training
Three Machine Learning models are used:

- **XGBoost** → High performance and accuracy
- **Logistic Regression** → Simple and interpretable
- **Decision Tree** → Easy to understand and visualize

---

## 🤖 Algorithms Used

### 🔹 XGBoost
- Ensemble learning using gradient boosting
- Handles complex relationships
- Provides feature importance
- Best performing model

### 🔹 Logistic Regression
- Uses sigmoid function for probability prediction
- Interpretable model
- Works well for baseline classification

### 🔹 Decision Tree
- Tree-based classification
- Uses entropy and information gain
- Easy to visualize but slightly less accurate

---

## 📈 Results and Performance

### 🔥 XGBoost Performance:
- Accuracy: **95.27%**
- High precision, recall, and F1-score across all classes

### 📊 Logistic Regression:
- Accuracy: **81.79%**
- Moderate performance

### 🌳 Decision Tree:
- Accuracy: **85%**
- Good interpretability but lower than XGBoost

### ✅ Predicted Classes:
- Underweight
- Normal Weight
- Overweight Level I & II
- Obesity Type I, II, III

The results show that **XGBoost outperforms other models** and provides highly reliable predictions for multiclass obesity classification. :contentReference[oaicite:0]{index=0}

---

## 📦 Required Packages

Install dependencies using:
