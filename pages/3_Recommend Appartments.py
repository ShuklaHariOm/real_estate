import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Recommend Apartments")

# Load the data and similarity matrices
location_df = pickle.load(open('datasets/location_distance.pkl','rb'))
cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl','rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl','rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl','rb'))


def recommend_properties_with_scores(property_name, top_n=5):
    # Calculate combined similarity matrix
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties based on similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a DataFrame with the results
    recommendations_df = pd.DataFrame({
        'Apartment': top_properties,
        'Similarity Score': top_scores
    })

    return recommendations_df


# Add clear page title and description
st.title("Apartment Recommendation System")
st.write("""
This page helps you find the best apartments in two ways:
1. **Search by Location and Radius**: Find apartments within a specified distance from your preferred location.
2. **Recommend Similar Apartments**: Get a list of apartments similar to the one you choose, based on factors like size, location, and amenities.
""")

# -------------------------------
# Section 1: Search by Location and Radius
# -------------------------------
st.subheader('Search Apartments by Location and Radius')
st.write('Choose a location and specify a distance in kilometers to find apartments within that radius.')

selected_location = st.selectbox('Select Location', sorted(location_df.columns.to_list()), help="Choose the location you are interested in.")
radius = st.number_input('Enter Radius (in kilometers)', min_value=3.0, value=5.0, help="Specify the search radius in kilometers.")

if st.button('Search Apartments'):
    result_ser = location_df[location_df[selected_location] < radius*1000][selected_location].sort_values()

    st.write(f"**Apartments within {radius} km of {selected_location}:**")
    for key, value in result_ser.items():
        st.write(f"{key} - {round(value/1000, 2)} km")

# -------------------------------
# Section 2: Recommend Similar Apartments
# -------------------------------
st.subheader('Find Similar Apartments')
st.write("Select an apartment, and we'll recommend similar ones based on size, proximity to amenities, and other factors.")

selected_apartment = st.selectbox('Select an Apartment', sorted(location_df.index.to_list()), help="Choose an apartment to find similar ones.")
num_recommendations = st.slider('Number of recommendations', min_value=1, max_value=10, value=5, help="Choose how many similar apartments you want to see.")

if st.button('Recommend Similar Apartments'):
    recommendation_df = recommend_properties_with_scores(selected_apartment, top_n=num_recommendations)
    
    st.write(f"**Apartments similar to {selected_apartment}:**")
    st.dataframe(recommendation_df)

# -------------------------------
# Additional Tips or Instructions (Optional)
# -------------------------------
st.info("""
Tip: Use the search function to explore apartments near specific locations, and then try finding similar apartments to discover even more options!
""")
