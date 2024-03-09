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
if 'button' not in st.session_state:
    st.session_state.button = {1:False,2:False, 3:False}

# Initialise route index in session state
if 'route_idx' not in st.session_state:
    st.session_state.route_idx = [0]

# Initialise n for brunch stop
if 'b' not in st.session_state:
    st.session_state.b = 3

# Initialise Brunch session state
if 'brunch' not in st.session_state:
    st.session_state.brunch = [3]

st.write(f"Brunch session state: {st.session_state.b}")

# Function to update the value in session state
def clicked_brunch(button):
    '''When the Next button is clicked, the text of the next
    alternative stop should be displayed'''
    if button <= 3:
        st.session_state.b += 1
        st.session_state.brunch = [st.session_state.b]
    else:
        st.session_state.b = 0
        st.session_state.brunch = [3]

def select_route():
    st.session_state.route_idx[0] = random.randint(0, len(route_data))
    st.session_state.button[1] = True


# Button with callback function
        
st.write(st.session_state.route_idx[0])

button = st.button("Generate Itinerary", on_click=select_route)

if st.session_state.button[1] == True:

    st.write(st.session_state.button[1])

    # Show users table 
    colms = st.columns((1, 3, 1))
    fields = ["Previous", "", "Next"]
    for col, field_name in zip(colms, fields):
        # header
        col.write(field_name)

    col1, col2, col3 = st.columns((1, 3,1))
    next_txt = "Next"
    next_button = col3.empty()  # create a placeholder
    next_stop = next_button.button(next_txt, on_click=clicked_brunch, args=[st.session_state.b])

    title_lst = ["1. Brunch", "2. Activity", "3. Afternoon Drinks", "4. Dinner", "5. Evening Out"]
    alt_lst = ["neighbour_1", "neighbour_2", "neighbour_3"]

    #1. Brunch

    if st.session_state.b == 3:

        #Id stop for Brunch
        stop_1 = int(route_data.stop_1[st.session_state.route_idx])

        col2.write(title_lst[0])  # title
        col2.write(stop_1)
        col2.write(dataset.name.iloc[stop_1])  # name
        col2.write(dataset.address.iloc[stop_1])  # address
    
    # if next_stop:
    else:
        column = str(alt_lst[st.session_state.b])
        stop_1 = int(dataset[column][int(route_data.stop_1[st.session_state.route_idx])])

        col2.write(title_lst[1])  # title
        col2.write(stop_1)
        col2.write(dataset.name.iloc[stop_1])  # name
        col2.write(dataset.address.iloc[stop_1])  # address



            
    

    # #Pull out individual stops
    # stop_1 = int(route_data.stop_1[st.session_state.route_idx])
    # stop_2 = int(route_data.stop_2[st.session_state.route_idx])
    # stop_3 = int(route_data.stop_3[st.session_state.route_idx])
    # stop_4 = int(route_data.stop_4[st.session_state.route_idx])
    # stop_5 = int(route_data.stop_5[st.session_state.route_idx])


        


