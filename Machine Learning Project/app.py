import streamlit as st
import pandas as pd
import pickle

# Load all trained models
lr_model = pickle.load(open('lr_model.pkl', 'rb'))
ridge_model = pickle.load(open('ridge_model.pkl', 'rb'))
lasso_model = pickle.load(open('lasso_model.pkl', 'rb'))

st.title("House Price Prediction")

# User inputs
area = st.number_input("Area (sq ft)")
bedrooms = st.number_input("Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, step=1)
stories = st.number_input("Stories", min_value=1, step=1)
parking = st.number_input("Parking", min_value=0, step=1)
mainroad = st.selectbox("Main Road?", ["Yes", "No"])
guestroom = st.selectbox("Guest Room?", ["Yes", "No"])
basement = st.selectbox("Basement?", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating?", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning?", ["Yes", "No"])
prefarea = st.selectbox("Preferred Area?", ["Yes", "No"])
furnishingstatus = st.selectbox("Furnishing Status", ["Furnished", "Semi-Furnished", "Unfurnished"])

# Choose model
model_choice = st.selectbox("Choose Model", ["Linear Regression", "Ridge Regression", "Lasso Regression"])

# Convert categorical to numeric
input_data = pd.DataFrame({
    'area':[area],
    'bedrooms':[bedrooms],
    'bathrooms':[bathrooms],
    'stories':[stories],
    'parking':[parking],
    'mainroad_yes':[1 if mainroad=="Yes" else 0],
    'guestroom_yes':[1 if guestroom=="Yes" else 0],
    'basement_yes':[1 if basement=="Yes" else 0],
    'hotwaterheating_yes':[1 if hotwaterheating=="Yes" else 0],
    'airconditioning_yes':[1 if airconditioning=="Yes" else 0],
    'prefarea_yes':[1 if prefarea=="Yes" else 0],
    'furnishingstatus_semi-furnished':[1 if furnishingstatus=="Semi-Furnished" else 0],
    'furnishingstatus_unfurnished':[1 if furnishingstatus=="Unfurnished" else 0]
})

if st.button("Predict Price"):
    if model_choice == "Linear Regression":
        model = lr_model
    elif model_choice == "Ridge Regression":
        model = ridge_model
    else:
        model = lasso_model
        
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ₦{prediction:,.0f}")
