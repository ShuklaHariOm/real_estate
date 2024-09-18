import streamlit as st

# Custom CSS for better layout
st.markdown("""
    <style>
    .title-style {
        font-size: 50px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .subtitle-style {
        font-size: 24px;
        color: #6c757d;
        text-align: center;
    }
    .feature-box {
        background-color: #f9f9f9;
        padding: 20px;
        text-decoration: none;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        border: 2px solid #ccc;
        margin: 10px 0;
        text-align: center;
        color: black; /* Change default font color */
        transition: background-color 0.3s, box-shadow 0.3s;
    }
    
    .feature-box a {
        text-decoration: none; /* Ensure no underline for links */
        color: black; /* Ensure link color matches the rest of the text */
    }
    
    .feature-box h2, .feature-box h3, .feature-box h4 {
        color: black !important; /* Change the header color to black */
    }
    .cta-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        border-radius: 5px;
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
        display: block;
        width: 60%;
        margin-left: auto;
        margin-right: auto;
        text-decoration: none;
    }
    .cta-button:hover {
        background-color: #45a049;
    }     
    .feature-box:hover {
        background-color: #f0f0f0;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Subtitle
st.markdown("<h1 class='title-style'>Gurugram House Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle-style'>Empowering Your Real Estate Journey</h3>", unsafe_allow_html=True)
st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

# Add Image
st.image("https://miro.medium.com/v2/resize:fit:626/1*JB1UtsoPA0xQI59JKyY2hA.jpeg", width=800)

st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

# Introduction
st.write("""
    Welcome to the **Gurugram Real Estate Project**! Discover your dream home in Gurugram with our comprehensive suite of tools.
    Whether you're a first-time buyer, an investor, or a real estate enthusiast, we offer valuable insights to help you navigate the real estate landscape.
""")


# Features Section
st.header("Key Features")

# Price Predictor Feature Box
st.markdown("""
    <a href="/Price_Predictor">
    <div class='feature-box'>
        <img src="https://static.vecteezy.com/system/resources/previews/004/806/126/non_2x/house-for-sale-icon-with-a-rupee-vector.jpg" width="100" height="100" style="margin-bottom: 10px;">
        <h3>🔮 Price Predictor</h3>
        <p>Find out the estimated price of your dream flat in Gurugram.</p>
    </div>
    </a>
""", unsafe_allow_html=True)

# Analytics Feature Box
st.markdown("""
    <a href="/Analysis_App">
    <div class='feature-box'>
        <img src="https://cdni.iconscout.com/illustration/premium/thumb/online-data-analysis-illustration-download-in-svg-png-gif-file-formats--analytics-statistics-business-intelligence-pack-illustrations-4646021.png?f=webp" width="100" height="100" style="margin-bottom: 10px;">
        <h3>📊 Real Estate Analytics</h3>
        <p>Get detailed insights and analysis of the Gurugram real estate market.</p>
    </div>
    </a>
""", unsafe_allow_html=True)

# Recommended Apartments Feature Box
st.markdown("""
    <a href="/Recommend_Appartments">
    <div class='feature-box'>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJA1pCV6TEZgY0mF6uLdFDZSBDx5ihUH12gg&s" width="100" height="100" style="margin-bottom: 10px;">
        <h3>🏠 Recommended Apartments</h3>
        <p>Let us help you find the perfect flat based on your preferences.</p>
    </div>
    </a>
""", unsafe_allow_html=True)


# Footer with additional information
st.markdown("""
    <div style='text-align: center; color: #6c757d;'>
        <p>🔑 Unlock the potential of Gurugram's real estate market with our smart tools and insights!</p>
    </div>
""", unsafe_allow_html=True)
