import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Price Predictor")

# Load Data
with open('df.pkl','rb') as file:
    df = pickle.load(file)

with open('xgboost_pipeline.pkl','rb') as file1:
    pipeline = pickle.load(file1)

# Page Title
st.title("House Price Predictor in Gurugram")
st.write("""
This tool helps you estimate the price of a property in Gurugram based on your inputs. 
Simply fill out the details below and get an instant prediction.
""")

# --------------------------------------
# User Inputs (Organized into sections)
# --------------------------------------
st.header('Enter Property Details')

# Collapsible sections for a cleaner UI
with st.expander("Basic Information", expanded=True):
    property_type = st.selectbox('Property Type',['flat','house'], help="Choose between a flat or house.")
    sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()), help="Select the sector where the property is located.")
    built_up_area = st.number_input('Built Up Area (in sqft)', min_value=0.0, help="Enter the total built-up area in square feet.")

with st.expander("Rooms & Amenities", expanded=False):
    bedrooms = st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist()), help="Select the number of bedrooms.")
    bathroom = st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist()), help="Select the number of bathrooms.")
    balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()), help="Select the number of balconies.")
    servant_room = st.selectbox('Servant Room', [0.0, 1.0], help="Indicate if the property has a servant room.")
    store_room = st.selectbox('Store Room', [0.0, 1.0], help="Indicate if the property has a store room.")

with st.expander("Additional Features", expanded=False):
    property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()), help="Specify the age or possession status of the property.")
    furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()), help="Is the property furnished, semi-furnished, or unfurnished?")
    luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()), help="Select the luxury category of the property.")
    floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()), help="Specify whether it's on a low or high floor.")

# --------------------------------------
# Prediction Logic
# --------------------------------------
if st.button('Predict Price'):

    # Collect data in a DataFrame
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    # Predict price
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # Display the predicted price range
    st.markdown(f"""
        ### Predicted Price Range:
        **₹ {round(low, 2)} Cr to ₹ {round(high, 2)} Cr**
    """, unsafe_allow_html=True)

# Optional Tips for Better Accuracy
st.info("Tip: For more accurate results, ensure the built-up area and property age are correctly filled.")
