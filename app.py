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
data_load_state.text("Done! (using st.cache_data)")

st.write("This is an introduction paragraph to the tool.")
button = st.button("Generate Itinerary")

if button:

    #Select random route index
    route_idx = random.randint(0, len(route_data))
    #Get list of stops
    stops_lst = list(route_data["opt_route"].iloc[route_idx])
    st.write(stops_lst)
    st.write(type(stops_lst))
    modified_list = stops_lst.strip('][').split(', ')

    #Pull out individual stops
    stop_0 = int(modified_list[0])
    stop_1 = int(modified_list[1])
    stop_2 = int(modified_list[2])
    stop_3 = int(modified_list[3])
    stop_4 = int(modified_list[4])

    #Brunch
    st.write("1. Brunch:")
    st.write(type(dataset.name.iloc[stop_0]))
    st.write(str(dataset.address.iloc[stop_0]))

    #Activity
    st.write("2. Activity:")
    st.write(str(dataset.name.iloc[stop_1]))
    st.write(str(dataset.address.iloc[stop_1]))

    #Afternoon Drinks
    st.write("3. Afternoon Drinks:")
    st.write(str(dataset.name.iloc[stop_2]))
    st.write(str(dataset.address.iloc[stop_2]))

    #Dinner
    st.write("4. Dinner:")
    st.write(str(dataset.name.iloc[stop_3]))
    st.write(str(dataset.address.iloc[stop_3]))

    #Evening Out
    st.write("5. Evening Out:")
    st.write(str(dataset.name.iloc[stop_4]))
    st.write(str(dataset.address.iloc[stop_4]))


