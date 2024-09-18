import streamlit as st

# Title and Subtitle
st.title("Real Estate Project")
st.subheader("Empowering Your Real Estate Journey")
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)


st.image("https://assets.everspringpartners.com/fe/06/f23661be455e97d009c6ae418995/real-estate-finance.jpg", width=600)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)


st.write("""
    Welcome to the Gurugram Real Estate Project! Discover your dream home in Gurugram with our powerful features.
    Whether you're a first-time buyer or an experienced investor, I have the tools to guide you through the real estate landscape.
""")


st.header("Features")

# Price Predictor
st.subheader("Price Predictor")
st.write("Find out the estimated price of your dream flat in Gurugram!")
st.write('Select the factors that matter most to you: location, size, amenities, and more')
st.write('Receive an instant, data-driven estimate for your desired flat')


# Analytics
st.subheader("Analytics")
st.write("Dive deep into the real estate market in Gurugram. ")
st.write('Get detailed insights, trends, and analysis to make informed decisions about buying or investing in properties.')

st.subheader('Recommend Appartments') 
st.write("Let us help you find the perfect flat! Simply provide your preferred location and area, and it will suggest nearby areas that match your criteria.and you can provide the apprartments too.")




