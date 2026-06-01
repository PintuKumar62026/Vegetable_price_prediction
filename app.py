import pandas as pd
import pickle
from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Load Model
# -----------------------------
try:
    with open("xgb_model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    print("Model Load Error:", e)
    model = None

# -----------------------------
# Load Dataset Used For Training
# -----------------------------
try:
    df = pd.read_csv("vegetable_market_500.csv")
except Exception as e:
    print("Dataset Load Error:", e)
    df = pd.DataFrame()

# -----------------------------
# Create Label Encoders
# -----------------------------
label_encoders = {}

categorical_columns = [
    "Vegetable",
    "Season",
    "Condition"
]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le

# -----------------------------
# Flask App
# -----------------------------
app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        selected_vegetable="",
        selected_season="Winter",
        selected_month="",
        selected_temp="",
        selected_disaster="0",
        selected_condition="Poor"
    )


@app.route("/predict", methods=["POST"])
def predict():

    try:

        if model is None:
            return render_template(
                "index.html",
                prediction_text="Model not loaded."
            )

        # -----------------------------
        # Get Form Data
        # -----------------------------
        vegetable = request.form["Vegetable"]
        season = request.form["Season"]
        month = int(request.form["Month"])
        temp = float(request.form["Temp"])
        disaster = int(request.form["Disaster"])
        condition = request.form["Condition"]

        # -----------------------------
        # Encode Categorical Values
        # -----------------------------
        vegetable_encoded = label_encoders["Vegetable"].transform([vegetable])[0]

        season_encoded = label_encoders["Season"].transform([season])[0]

        condition_encoded = label_encoders["Condition"].transform([condition])[0]

        # -----------------------------
        # Create Input DataFrame
        # -----------------------------
        input_df = pd.DataFrame({
            "Vegetable": [vegetable_encoded],
            "Season": [season_encoded],
            "Month": [month],
            "Temp": [temp],
            "Disaster": [disaster],
            "Condition": [condition_encoded]
        })

        # -----------------------------
        # Predict
        # -----------------------------
        prediction = model.predict(input_df)[0]

        return render_template(
            "index.html",
            prediction_text=f"Predicted Price: ₹{prediction:.2f} per kg",

            selected_vegetable=vegetable,
            selected_season=season,
            selected_month=month,
            selected_temp=temp,
            selected_disaster=str(disaster),
            selected_condition=condition
        )

    except Exception as e:

        return render_template(
            "index.html",

            prediction_text=f"Error: {str(e)}",

            selected_vegetable=request.form.get("Vegetable", ""),
            selected_season=request.form.get("Season", "Winter"),
            selected_month=request.form.get("Month", ""),
            selected_temp=request.form.get("Temp", ""),
            selected_disaster=request.form.get("Disaster", "0"),
            selected_condition=request.form.get("Condition", "Poor")
        )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )