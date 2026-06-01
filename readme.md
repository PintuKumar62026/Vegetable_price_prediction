# 🥬 Vegetable Price Prediction System

A Machine Learning-powered web application that predicts vegetable prices based on factors such as:

* Vegetable Type
* Season
* Month
* Temperature
* Natural Disasters
* Crop Condition

The project is built using:

* Python
* Flask
* XGBoost
* Pandas
* Scikit-Learn
* Bootstrap 5

---

# 📂 Project Structure

```text
vegetable_price_prediction/
│
├── app.py
├── train.py
├── vegetable_market_500.csv
├── xgb_model.pkl
│
├── templates/
│   └── index.html
│
└── README.md
```

---

# 🚀 How to Run the Project

## Step 1: Open PowerShell

Navigate to the project directory:

```powershell
cd "C:\Users\kumar\Downloads\vegetable price predict\vegetable_price_prediction"
```

---

## Step 2: Verify Project Files

Run:

```powershell
dir
```

You should see:

```text
app.py
train.py
vegetable_market_500.csv
xgb_model.pkl
templates
```

---

## Step 3: Train the Model (Only If Required)

Check if the model already exists:

```powershell
dir xgb_model.pkl
```

If the model file is missing:

```powershell
python train.py
```

Expected output:

```text
MAE: ...
R2 Score: ...
✅ Model saved as xgb_model.pkl
```

---

## Step 4: Run the Flask Application

```powershell
python app.py
```

Expected output:

```text
* Running on http://127.0.0.1:5000
```

---

## Step 5: Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 📦 Install Required Packages

If you encounter errors such as:

```text
ModuleNotFoundError: No module named 'pandas'
```

Install dependencies:

```powershell
pip install pandas numpy flask scikit-learn xgboost
```

Then run:

```powershell
python app.py
```

---

# ⚡ Quick Start

If everything is already installed:

```powershell
cd "C:\Users\kumar\Downloads\vegetable price predict\vegetable_price_prediction"

python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

# 📊 Model Information

Algorithm Used:

* XGBoost Regressor

Features:

* Vegetable
* Season
* Month
* Temperature
* Disaster
* Condition

Target:

* Price_per_kg

Evaluation Metrics:

* MAE (Mean Absolute Error)
* R² Score

---

# 🎯 Features

✅ Vegetable Selection Dropdown

✅ Season Selection

✅ Temperature-Based Prediction

✅ Disaster Impact Analysis

✅ Crop Condition Analysis

✅ Machine Learning Price Prediction

✅ Responsive Bootstrap UI

---

# 🛠 Future Improvements

* Interactive Charts
* Historical Price Trends
* Prediction History
* Admin Dashboard
* Real-Time Market Data Integration
* Advanced Model Comparison

---

# 👨‍💻 Author
Pintu Kumar

Software Developer | Machine Learning Enthusiast
