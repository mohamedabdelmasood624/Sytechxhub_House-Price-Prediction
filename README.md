# 🏠 House Price Prediction – Advanced Regression Pipeline

> **Internship-Ready Machine Learning Project**
> Built with a production mindset: clean data, strong baselines, advanced models, and deployment readiness.

---

## 🚀 Project Overview

This project focuses on predicting house prices using advanced regression techniques. Instead of treating this as a simple ML task, the project was designed as a **real-world machine learning pipeline**, similar to what is used in production environments.

**Key goals:**

- Build strong baselines and improve them iteratively
- Apply proper preprocessing and feature engineering
- Compare multiple regression models
- Use ensembling techniques for robustness
- Prepare the solution for deployment

Dataset used: **House Prices – Advanced Regression Techniques (Kaggle)**

---

## 🧠 ML Pipeline

```
EDA → Data Cleaning → Feature Engineering → Preprocessing
→ Model Training → Evaluation → Ensembling → Deployment
```

---

## 🔍 Exploratory Data Analysis (EDA)

EDA was performed to deeply understand the dataset before modeling.

### What was analyzed:

- Distribution of house prices (target variable)
- Missing value patterns
- Correlations between numerical features
- Impact of categorical features on price

### Key insights:

- Target variable is right-skewed → log transformation applied
- Several features contain missing values that require different handling strategies
- Strong non-linear relationships exist → tree-based models are suitable

---

## 🧹 Data Cleaning

Different strategies were applied depending on the feature type:

- Numerical features: median imputation
- Categorical features: most frequent value / "None" category
- Outliers: handled using robust preprocessing techniques

This ensured data consistency without introducing leakage.

---

## 🧠 Feature Engineering

Feature engineering was a core part of improving model performance.

Examples:

- Log transformation for skewed numerical variables
- Creation of interaction features
- Domain-driven feature selection
- Removal of noisy or redundant columns

> Feature engineering significantly improved generalization performance.

---

## ⚙️ Preprocessing

### Scaling

- **RobustScaler** was used instead of StandardScaler to reduce the impact of outliers.

### Encoding

- One-Hot Encoding for nominal categorical features
- Label Encoding for ordinal features

A unified preprocessing pipeline was built to ensure reproducibility.

---

## 🤖 Models Used

### 1️⃣ Linear Models (Baseline)

- Linear Regression
- Ridge Regression
- Lasso Regression

**Why?**

- Establish a strong baseline
- Handle multicollinearity
- Perform implicit feature selection (Lasso)

---

### 2️⃣ Tree-Based Models

- Random Forest
- Gradient Boosting

**Why?**

- Capture non-linear relationships
- Handle feature interactions automatically

---

### 3️⃣ Advanced Boosting Models

- XGBoost
- LightGBM

**Why?**

- High performance on structured/tabular data
- Built-in regularization
- Faster convergence

---

## 🧩 Ensembling & Stacking

Multiple strong models were combined to improve robustness and accuracy.

- Averaging predictions from top-performing models
- Stacking using a meta-learner trained on model outputs

This reduced variance and improved generalization.

---

## 📊 Evaluation Metrics

Models were evaluated using:

- **RMSE (Root Mean Squared Error)**
- Cross-validation for reliable performance estimation

The final ensemble achieved the best validation performance.

---

## 🚀 Deployment Readiness

The project includes deployment-oriented components:

- Model and preprocessing pipeline saved using `joblib`
- Script for loading the model and predicting on new data
- Consistent feature alignment for inference

This makes the solution ready for real-world usage.

---

## 🛠️ How to Run

```bash
# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Jupyter Notebook
jupyter notebook
```

---

## ⭐ Why This Project Stands Out

- Production-style ML pipeline
- Strong baselines + advanced models
- Clear reasoning behind every decision
- Clean, reproducible, and scalable design

> This project reflects how machine learning is applied in real-world scenarios, not just academic exercises.

---

## 📌 Author

**Mohamed Abdelmaqsoud**
Machine Learning Intern / Junior ML Engineer
