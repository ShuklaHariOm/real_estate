import numpy as numpy
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import pickle
from wordcloud import WordCloud
import seaborn as sns

st.set_page_config(page_title='pollting_demo')

st.title('Analytics')

new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl','rb'))

group_df = new_df.groupby('sector').mean(numeric_only=True)[['price','price_per_sqft','built_up_area','latitude','longitude']]

# List of questions to display
questions = [
    "What is the price per square foot in Gurugram?",
    "What is the relationship between area and price?",
    "What is the distribution of BHK types?",
    "How do BHK prices compare side by side?",
    "What is the side-by-side price distribution by property type?",
    "What are the features of buying a house in this city?"
]

# Sidebar for question selection
question = st.selectbox("Select a question to visualize:", questions)


def sector_price_geomap():
    st.header('Sector Price per Sqft Geomap')
    fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                    color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                    mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

    st.plotly_chart(fig,use_container_width=True)

def features_wordcloud():
    st.header('Features Wordcloud')

    wordcloud = WordCloud(width = 800, height = 800,
                        background_color ='black',
                        stopwords = set(['s']),  # Any stopwords you'd like to exclude
                        min_font_size = 10).generate(feature_text)

    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad = 0)
    st.pyplot(plt)

def area_vs_price_scatter():
    st.header('area vs price')

    property_type = st.selectbox('property_type', ['house','flat'])

    if property_type == 'house':
        fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

        st.plotly_chart(fig1, use_container_width=True)
    else:
        fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                        title="Area Vs Price")

        st.plotly_chart(fig1, use_container_width=True)

def bhk_pie_chart():
    st.header('BHK Pie Chart')

    sector_options = new_df['sector'].unique().tolist()
    sector_options.insert(0,'overall')

    selected_sector = st.selectbox('Select Sector', sector_options)

    if selected_sector == 'overall':

        fig2 = px.pie(new_df, names='bedRoom')

        st.plotly_chart(fig2, use_container_width=True)
    else:

        fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

        st.plotly_chart(fig2, use_container_width=True)

def bhk_price_boxplot():
    st.header('Side by Side BHK price comparison')

    fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

    st.plotly_chart(fig3, use_container_width=True)

def property_type_distplot():
    st.header('Side by Side Distplot for property type')

    fig3 = plt.figure(figsize=(10, 4))
    sns.histplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
    sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
    plt.legend()
    st.pyplot(fig3)

# Show visualization based on the selected question
if question == questions[0]:
    sector_price_geomap()
elif question == questions[1]:
    area_vs_price_scatter()
elif question == questions[2]:
    bhk_pie_chart()
elif question == questions[3]:
    bhk_price_boxplot()
elif question == questions[4]:
    property_type_distplot()
elif question == questions[5]:
    features_wordcloud()