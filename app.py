import streamlit as st
import pandas as pd
import numpy as np
import random

st.title("Manchester Itinerary Generator")

route_data = "./OptimalRoutes.csv"
dataset = "./ItineraryGenerator_Dataset.csv"

@st.cache_data
def load_data(route_data_path, dataset_path):

    route_data = pd.read_csv(route_data_path)
    dataset = pd.read_csv(dataset_path)

    return route_data, dataset

# Create a text element and let the reader know the data is loading
data_load_state = st.text("Loading data...")
# Load 10,000 rows of data into the dataframe
route_data, dataset = load_data(route_data_path=route_data, dataset_path=dataset)
# Notify the reader that the data was successfully loaded
data_load_state.text("Done! Data is loaded in.")

st.write("This is an introduction paragraph to the tool.")
button = st.button("Generate Itinerary")

if button:

    #Select random route index
    route_idx = random.randint(0, len(route_data))

    #Pull out individual stops
    stop_1 = int(route_data.stop_1[route_idx])
    stop_2 = int(route_data.stop_2[route_idx])
    stop_3 = int(route_data.stop_3[route_idx])
    stop_4 = int(route_data.stop_4[route_idx])
    stop_5 = int(route_data.stop_5[route_idx])

    #Brunch
    st.write("1. Brunch:")
    st.write(str(dataset.name.iloc[stop_1]))
    st.write(str(dataset.address.iloc[stop_1]))

    #Activity
    st.write("2. Activity:")
    st.write(str(dataset.name.iloc[stop_2]))
    st.write(str(dataset.address.iloc[stop_2]))

    #Afternoon Drinks
    st.write("3. Afternoon Drinks:")
    st.write(str(dataset.name.iloc[stop_3]))
    st.write(str(dataset.address.iloc[stop_3]))

    #Dinner
    st.write("4. Dinner:")
    st.write(str(dataset.name.iloc[stop_4]))
    st.write(str(dataset.address.iloc[stop_4]))

    #Evening Out
    st.write("5. Evening Out:")
    st.write(str(dataset.name.iloc[stop_5]))
    st.write(str(dataset.address.iloc[stop_5]))


