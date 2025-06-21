import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("flight_price_model.pkl")

# Title
st.title("✈️ Flight Price Predictor")
st.markdown("Enter flight details below to predict the ticket price.")

# Input fields
airline = st.selectbox("Airline", [
    "IndiGo", "Air India", "Jet Airways", "SpiceJet", "Vistara",
    "GoAir", "Multiple carriers", "Air Asia", "Trujet"
])

source_city = st.selectbox("Source City", [
    "Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai", "Hyderabad"
])

departure_time = st.selectbox("Departure Time", [
    "Early Morning", "Morning", "Afternoon", "Evening", "Night", "Late Night"
])

arrival_time = st.selectbox("Arrival Time", [
    "Early Morning", "Morning", "Afternoon", "Evening", "Night", "Late Night"
])

destination_city = st.selectbox("Destination City", [
    "Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai", "Hyderabad"
])

stops = st.selectbox("Number of Stops", [0, 1, 2, 3])

flight_class = st.selectbox("Class", ["Economy", "Business"])

duration = st.number_input("Flight Duration (in hours)", min_value=0.0, max_value=50.0, step=0.5)

days_left = st.slider("Days Left Until Flight", min_value=0, max_value=365, value=30)

# Label Encoding Maps (must match training encodings)
airline_map = {
    "IndiGo": 0, "Air India": 1, "Jet Airways": 2, "SpiceJet": 3,
    "Vistara": 4, "GoAir": 5, "Multiple carriers": 6, "Air Asia": 7, "Trujet": 8
}
city_map = {
    "Delhi": 0, "Mumbai": 1, "Bangalore": 2, "Kolkata": 3, "Chennai": 4, "Hyderabad": 5
}
time_map = {
    "Early Morning": 0, "Morning": 1, "Afternoon": 2,
    "Evening": 3, "Night": 4, "Late Night": 5
}
class_map = {"Economy": 0, "Business": 1}

# Encode inputs
input_data = pd.DataFrame([{
    'Unnamed: 0': 0,  # dummy index value
    'airline': airline_map[airline],
    'source_city': city_map[source_city],
    'departure_time': time_map[departure_time],
    'stops': stops,
    'arrival_time': time_map[arrival_time],
    'destination_city': city_map[destination_city],
    'class': class_map[flight_class],
    'duration': duration,
    'days_left': days_left
}], columns=[
    'Unnamed: 0', 'airline', 'source_city', 'departure_time', 'stops',
    'arrival_time', 'destination_city', 'class', 'duration', 'days_left'
])

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Flight Price: ₹{round(prediction, 2)}")
