import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("flight_price_model.pkl")

# Title
st.title("✈️ Flight Price Predictor")

# Subtitle
st.markdown("Enter flight details below to predict the ticket price.")

# Input fields
duration = st.number_input("Flight Duration (in hours)", min_value=0.0, max_value=50.0, step=0.5)
stops = st.selectbox("Number of Stops", [0, 1, 2, 3])
departure_time = st.selectbox("Departure Time", [
    "Morning", "Afternoon", "Evening", "Night", "Early Morning", "Late Night"
])
airline = st.selectbox("Airline", [
    "IndiGo", "Air India", "Jet Airways", "SpiceJet", "Vistara",
    "GoAir", "Multiple carriers", "Air Asia", "Trujet"
])
flight_class = st.selectbox("Class", ["Economy", "Business"])

# Encoding inputs manually (must match training data encoding)
departure_mapping = {
    "Early Morning": 0, "Morning": 1, "Afternoon": 2,
    "Evening": 3, "Night": 4, "Late Night": 5
}

airline_mapping = {
    "IndiGo": 0, "Air India": 1, "Jet Airways": 2, "SpiceJet": 3, "Vistara": 4,
    "GoAir": 5, "Multiple carriers": 6, "Air Asia": 7, "Trujet": 8
}

class_mapping = {"Economy": 0, "Business": 1}

# Convert inputs
departure_encoded = departure_mapping.get(departure_time, 0)
airline_encoded = airline_mapping.get(airline, 0)
class_encoded = class_mapping.get(flight_class, 0)

# Prepare input DataFrame
input_data = pd.DataFrame([{
    'duration': duration,
    'stops': stops,
    'departure_time': departure_encoded,
    'airline': airline_encoded,
    'class': class_encoded
}])

# Predict
if st.button("Predict Price"):
    # prediction = model.predict(input_data)[0]
    prediction = model.feature_names_in_
    # print(model.feature_names_in_)
    # st.success(f"💰 Estimated Flight Price: ₹{round(prediction, 2)}")
    st.success(f"💰 Estimated Flight Price: prediction")
