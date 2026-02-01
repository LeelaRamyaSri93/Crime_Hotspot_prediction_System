# 🚨 Crime Hotspot Prediction & Public Safety System

A full-stack **Machine Learning–powered crime analytics system** designed to enhance public safety by identifying crime hotspots, forecasting crime trends, predicting crime types, and assessing area-level risk.

This project uses **real-world crime data**, multiple **ML models**, interactive **map visualizations**, and is **fully deployed on the cloud**.

---

## 🔗 Live Deployments

- **Frontend (Netlify):**  
  👉 https://crimepredictionsystem.netlify.app/

- **Backend API (Render):**  
  👉 https://crime-prediction-system-b0oq.onrender.com

---

## 🎯 Project Objectives

1. Identify **crime hotspot zones** using spatial analysis
2. Forecast **expected number of crimes** for a given time & area
3. Predict the **most likely crime type**
4. Assess **crime risk level** of a region
5. Provide an **interactive, user-friendly web interface**
6. Deploy the complete system on cloud platforms

---

## 🧠 Problem Statements Covered

### 🔹 PS-1: Crime Hotspot Detection
- **Kernel Density Estimation (KDE)** for crime density
- **K-Means clustering** for hotspot zone classification
- Interactive **map-based visualization**

### 🔹 PS-2: Crime Count Forecasting
- **Poisson Regression**
- Predicts expected crime count based on time & area

### 🔹 PS-3: Crime Type Prediction
- **Random Forest Classifier**
- Predicts most probable crime category

### 🔹 PS-4: Crime Risk Level Assessment
- **Random Forest Classifier**
- Classifies regions into **Low / Medium / High risk**

---

## 🛠️ Tech Stack

### 🔹 Machine Learning
- Python
- Scikit-learn
- Pandas, NumPy
- KDE, K-Means, Random Forest, Poisson Regression

### 🔹 Backend
- Flask (REST APIs)
- Flask-CORS
- Joblib (model loading)
- Hosted on **Render**

### 🔹 Frontend
- HTML5
- CSS3
- JavaScript
- Leaflet.js (maps & heatmaps)
- Hosted on **Netlify**

### 🔹 Deployment & Tools
- Git & GitHub
- Render (Backend)
- Netlify (Frontend)

---

## 📂 Project Structure
CRIME/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── models/
│   └── *.pkl
│
├── frontend/
│ ├── index.html
│ ├── dashboard.html
│ ├── hotspots.html
│ ├── prediction.html
│ ├── risk.html
│ └── css/
│   └── style.css
│
├── .gitignore
└── README.md

---


---

## 🔌 Backend API Endpoints

POST /api/poisson
### ▶️ Poisson Crime Forecast
**Input:** Community Area, Hour, Day, Month, Year  
**Output:** Expected crime count

---
POST /api/crime-type
### ▶️ Crime Type Prediction
**Input:** Location & time details  
**Output:** Predicted crime type

---
POST /api/risk
### ▶️ Risk Level Prediction
**Input:** Community area & district  
**Output:** LOW / MEDIUM / HIGH risk

---
GET /api/hotspots/kde
GET /api/hotspots/zones
### ▶️ Hotspot Data
**Output:** Crime density & hotspot zones for visualization

---

## 🗺️ Frontend Pages

- **Home:** System overview & navigation
- **Dashboard:** High-level summary of all models
- **Hotspots:** Crime hotspot map (KDE + K-Means)
- **Predictions:** Crime count & crime type prediction
- **Risk Assessment:** Area-level safety analysis

---

## ⚠️ Model Accuracy (Practical)

- Crime Type Prediction accuracy varies due to **class imbalance**  
- Risk Level model achieves **near-perfect accuracy** due to aggregated features
- Predictions are **probabilistic**, not deterministic
- Similar inputs may yield similar outputs — expected ML behavior

---

## 📜 Disclaimer

This system is built for **academic and educational purposes**.  
Predictions are based on historical data and should not be used as sole decision-making tools for public safety.

---

⭐ *If you find this project useful, feel free to star the repository!* ⭐


