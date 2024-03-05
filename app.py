import streamlit as st
import pandas as pd
import numpy as np
import random

st.title("Manchester Itinerary Generator")

route_data = "./OptimalRoutes.csv"
dataset = "./IG_neighbours.csv"

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

# Initialise the key in session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = {1:False,2:False, 3:False}

# Initialise route index in session state
if 'route_idx' not in st.session_state:
    st.session_state.route_idx = [None]

# Function to update the value in session state
@st.cache_data
def clicked(button):
    st.session_state.clicked[button] = True


@st.cache_data
def select_route():
    st.session_state.route_idx[1] = random.randint(0, len(route_data))
    st.session_state.clicked[1] = True
    if st.session_state.clicked[1] == True:
        st.write("session state 1 = True")

# @st.cache_data
# def next_button(stop_idx, n):
#     stop_idx = dataset[alt_lst[n]].iloc[stop_lst[stop_idx]]

# Button with callback function
button = st.button("Generate Itinerary", on_click=select_route)

if st.session_state.clicked[1] == True:

    st.write(st.session_state.clicked[1])

    # Show users table 
    colms = st.columns((1, 3, 1))
    fields = ["Previous", "", "Next"]
    for col, field_name in zip(colms, fields):
        # header
        col.write(field_name)

    n = 0

    col1, col2, col3 = st.columns((1, 3,1))
    next_txt = "Next"
    next_button = col3.empty()  # create a placeholder
    next_stop = next_button.button(next_txt)

    col3.write(st.session_state.clicked[2])

    #Select random route index
    st.write(route_data.iloc[st.session_state.route_idx])

    title_lst = ["1. Brunch", "2. Activity", "3. Afternoon Drinks", "4. Dinner", "5. Evening Out"]
    alt_lst = ["neighbour_1", "neighbour_2", "neighbour_3"]

    #1. Brunch

    if not next_stop:

        #Id stop for Brunch
        stop_1 = int(route_data.stop_1[st.session_state.route_idx])

        col1.write(st.session_state.clicked[1])

        col2.write(title_lst[1])  # title
        col2.write(stop_1)
        col2.write(dataset.name.iloc[stop_1])  # name
        col2.write(dataset.address.iloc[stop_1])  # address
    
    if next_stop:

        column = str(alt_lst[n])
        stop_1 = int(route_data[column][st.session_state.route_idx])

        col1.write(st.session_state.clicked[1])

        col2.write(title_lst[1])  # title
        col2.write(stop_1)
        col2.write(dataset.name.iloc[stop_1])  # name
        col2.write(dataset.address.iloc[stop_1])  # address

        #Change n to go to next alternative stop
        if n < 2:
            n += 1
            
        else:
            n = 1
        

    #     if st.session_state.clicked[2]:

    #         stop_lst[x] = dataset[alt_lst[n]].iloc[stop_lst[x]]
    #         st.session_state.clicked[2]= False

            
    

    # #Pull out individual stops
    # stop_1 = int(route_data.stop_1[st.session_state.route_idx])
    # stop_2 = int(route_data.stop_2[st.session_state.route_idx])
    # stop_3 = int(route_data.stop_3[st.session_state.route_idx])
    # stop_4 = int(route_data.stop_4[st.session_state.route_idx])
    # stop_5 = int(route_data.stop_5[st.session_state.route_idx])


    # for x, stop in enumerate(stop_lst):

        


