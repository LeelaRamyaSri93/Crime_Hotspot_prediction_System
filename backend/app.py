from flask import Flask, jsonify, request
from flask_cors import CORS
import joblib
import os
import pandas as pd  # add this import at top

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

CRIME_COMMUNITY_CENTROIDS = {
    25: (41.8917, -87.6543),
    61: (41.7698, -87.6136),
    71: (41.7454, -87.7081),
}
# Community Area centroids (sample – extendable)
RISK_COMMUNITY_CENTROIDS = {
    25: {"Latitude": 41.8781, "Longitude": -87.6298, "District": 10},
    61: {"Latitude": 41.7943, "Longitude": -87.6051, "District": 6},
    71: {"Latitude": 41.7658, "Longitude": -87.6459, "District": 7}
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load Poisson model
poisson_model = joblib.load(
    os.path.join(BASE_DIR, "models", "poisson_crime_model.pkl")
)

@app.route("/")
def home():
    return jsonify({"status": "Backend + Poisson model running"})

@app.route("/api/poisson", methods=["POST"])
def poisson_predict():
    data = request.json

    # Create DataFrame with EXACT column names used in training
    X = pd.DataFrame([{
        "Community Area": data["community_area"],
        "hour": data["hour"],
        "day_of_week": data["day_of_week"],
        "month": data["month"],
        "Year": data["year"]
    }])

    prediction = poisson_model.predict(X)[0]

    return jsonify({
        "expected_crimes": round(float(prediction), 2)
    })
crime_type_model = joblib.load(
    os.path.join(BASE_DIR, "models", "crime_type_rf_model.pkl")
)

crime_type_encoder = joblib.load(
    os.path.join(BASE_DIR, "models", "crime_type_label_encoder.pkl")
)
@app.route("/api/crime-type", methods=["POST"])
def crime_type_predict():
    data = request.json

    community_area = int(data["community_area"])
    hour = int(data["hour"])
    day_of_week = int(data["day_of_week"])
    month = int(data["month"])

    # ✅ Get centroid safely
    lat, lon = CRIME_COMMUNITY_CENTROIDS.get(
        community_area, (41.8781, -87.6298)  # Chicago default
    )

    X = pd.DataFrame([{
        "Latitude": lat,
        "Longitude": lon,
        "hour": hour,
        "day_of_week": day_of_week,
        "month": month,
        "Community Area": community_area
    }])

    pred_encoded = crime_type_model.predict(X)[0]
    pred_label = crime_type_encoder.inverse_transform([pred_encoded])[0]

    return jsonify({
        "predicted_crime_type": pred_label
    })


risk_model = joblib.load(
    os.path.join(BASE_DIR, "models", "crime_risk_rf_model.pkl")
)
@app.route("/api/risk", methods=["POST","OPTIONS"])
def risk_level_predict():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200
    data = request.json

    area = data["community_area"]

    if area not in RISK_COMMUNITY_CENTROIDS:
        return jsonify({"error": "Unknown community area"}), 400

    centroid = RISK_COMMUNITY_CENTROIDS[area]

    X = pd.DataFrame([{
        "Latitude": centroid["Latitude"],
        "Longitude": centroid["Longitude"],
        "hour": data["hour"],
        "day_of_week": data["day_of_week"],
        "month": data["month"],
        "Community Area": area,
        "District": centroid["District"]

    }])

    risk_pred = risk_model.predict(X)[0]

    return jsonify({
        "risk_level": risk_pred
    })
KDE_DATA_PATH = os.path.join(BASE_DIR, "data", "kde_hotspot_grid.csv")
KMEANS_DATA_PATH = os.path.join(BASE_DIR, "data", "kmeans_hotspot_zones.csv")
@app.route("/api/hotspots/kde", methods=["GET"])
def get_kde_hotspots():
    df = pd.read_csv(KDE_DATA_PATH)

    return jsonify({
        "type": "kde",
        "count": len(df),
        "data": df.to_dict(orient="records")
    })
@app.route("/api/hotspots/zones", methods=["GET"])
def get_kmeans_zones():
    df = pd.read_csv(KMEANS_DATA_PATH)

    return jsonify({
        "type": "kmeans",
        "count": len(df),
        "data": df.to_dict(orient="records")
    })



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
