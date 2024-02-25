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

# Initialize the key in session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = {1:False,2:False, 3:False}

# Function to update the value in session state
def clicked(button):
    st.session_state.clicked[button] = True


# Conditional based on value in session state, not the output
# if st.session_state.clicked[1]:
#     st.write('The first button was clicked.')
#     st.button('Second Button', on_click=clicked, args=[2])
#     if st.session_state.clicked[2]:
#         st.write('The second button was clicked')

# Button with callback function
button = st.button("Generate Itinerary", on_click=clicked, args=[1])

if button:

    #Select random route index
    route_idx = random.randint(0, len(route_data))

    #Pull out individual stops
    stop_1 = int(route_data.stop_1[route_idx])
    stop_2 = int(route_data.stop_2[route_idx])
    stop_3 = int(route_data.stop_3[route_idx])
    stop_4 = int(route_data.stop_4[route_idx])
    stop_5 = int(route_data.stop_5[route_idx])

    col1, col2 = st.columns([1,1])

    #Brunch
    col1.markdown("1. Brunch:")

    alt_1 = int(dataset.neighbour_1.iloc[stop_1])
    alt_2 = int(dataset.neighbour_2.iloc[stop_1])
    alt_3 = int(dataset.neighbour_3.iloc[stop_1])

    name = str(dataset.name.iloc[stop_1])
    address = str(dataset.address.iloc[stop_1])

    col1.markdown(name)
    col1.markdown(address)

    n = 1

    button_type = "Next"
    button_phold = col2.empty()  # create a placeholder
    do_action = button_phold.button(button_type, key=stop_1, on_click=clicked, args=[2])

    if do_action:
        next_idx = f"alt_{n}"
        name = str(dataset.name.iloc[next_idx])
        address = str(dataset.address.iloc[next_idx])

        col1.write(name)
        col1.write(address)

        button_phold.empty()  #  remove button

    # with col1:
    #     next = st.button('next')
    #     if next:
    #         neighbour = f"alt_{n+1}"
    #         col1.write(str(dataset.name.iloc[neighbour]))
    #         col1.write(str(dataset.address.iloc[neighbour]))
    # with col2:
    #     st.button('previous')

    #Activity
    st.write("2. Activity:")

    alt_1 = int(dataset.neighbour_1.iloc[stop_2])
    alt_2 = int(dataset.neighbour_2.iloc[stop_2])
    alt_3 = int(dataset.neighbour_3.iloc[stop_2])

    st.write(str(dataset.name.iloc[stop_2]))
    st.write(str(dataset.address.iloc[stop_2]))

    #Afternoon Drinks
    st.write("3. Afternoon Drinks:")

    alt_1 = int(dataset.neighbour_1.iloc[stop_3])
    alt_2 = int(dataset.neighbour_2.iloc[stop_3])
    alt_3 = int(dataset.neighbour_3.iloc[stop_3])

    st.write(str(dataset.name.iloc[stop_3]))
    st.write(str(dataset.address.iloc[stop_3]))

    #Dinner
    st.write("4. Dinner:")

    alt_1 = int(dataset.neighbour_1.iloc[stop_4])
    alt_2 = int(dataset.neighbour_2.iloc[stop_4])
    alt_3 = int(dataset.neighbour_3.iloc[stop_4])

    st.write(str(dataset.name.iloc[stop_4]))
    st.write(str(dataset.address.iloc[stop_4]))

    #Evening Out
    st.write("5. Evening Out:")

    alt_1 = int(dataset.neighbour_1.iloc[stop_5])
    alt_2 = int(dataset.neighbour_2.iloc[stop_5])
    alt_3 = int(dataset.neighbour_3.iloc[stop_5])

    st.write(str(dataset.name.iloc[stop_5]))
    st.write(str(dataset.address.iloc[stop_5]))


