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
@st.cache_data
def clicked(button):
    st.session_state.clicked[button] = True


@st.cache_data
def select_route():
    route_idx = random.randint(0, len(route_data))
    st.session_state.clicked[1] = True

    return route_idx

# Button with callback function
button = st.button("Generate Itinerary", on_click=select_route)

if st.session_state.clicked[1] == True:

    #Set session state 
    st.write(st.session_state.clicked[1])

    #Select random route index
    st.session_state.route_idx = random.randint(0, len(route_data))

    st.write(route_data.iloc[st.session_state.route_idx])

    #Pull out individual stops
    stop_1 = int(route_data.stop_1[st.session_state.route_idx])
    stop_2 = int(route_data.stop_2[st.session_state.route_idx])
    stop_3 = int(route_data.stop_3[st.session_state.route_idx])
    stop_4 = int(route_data.stop_4[st.session_state.route_idx])
    stop_5 = int(route_data.stop_5[st.session_state.route_idx])

    stop_lst = [stop_1, stop_2, stop_3, stop_4, stop_5]
    title_lst = ["1. Brunch", "2. Activity", "3. Afternoon Drinks", "4. Dinner", "5. Evening Out"]
    alt_lst = ["neighbour_1", "neighbour_2", "neighbour_3"]


     # # Show users table 
    colms = st.columns((1, 3, 1))
    fields = ["Previous", "", "Next"]
    for col, field_name in zip(colms, fields):
        # header
        col.write(field_name)



    for x, stop in enumerate(stop_lst):
        col1, col2, col3 = st.columns((1, 3,1))

        col1.write(st.session_state.clicked[1])

        col2.write(title_lst[x])  # title
        col2.write(stop)
        col2.write(dataset.name.iloc[stop_lst[x]])  # name
        col2.write(dataset.address.iloc[stop_lst[x]])  # address

        next_txt = "Next"
        next_button = col3.empty()  # create a placeholder
        next_stop = next_button.button(next_txt, key=x, on_click=clicked, args=[2])

        # previous_txt = "Previous"
        # next_button = col1.empty()  # create a placeholder
        # next_stop = next_button.button(previous_txt, key=x, on_click=clicked, args=[3])
        col3.write(st.session_state.clicked[2])
        n = 0

        # if st.session_state.clicked[2]:
        if next_stop:

            stop_lst[x] = dataset[alt_lst[n]].iloc[stop_lst[x]]
            st.session_state.clicked[2]= False

            if n < 2:
                n += 1
            
            else:
                n = 1    

    # col1, col2 = st.columns([1,1])

    # #Brunch
    # col1.markdown("1. Brunch:")

    # alt_1 = int(dataset.neighbour_1.iloc[stop_1])
    # alt_2 = int(dataset.neighbour_2.iloc[stop_1])
    # alt_3 = int(dataset.neighbour_3.iloc[stop_1])

    # name = str(dataset.name.iloc[stop_1])
    # address = str(dataset.address.iloc[stop_1])

    # col1.markdown(name)
    # col1.markdown(address)

    # n = 1
        
    # button_type = "Next"
    # button_phold = col2.empty()  # create a placeholder
    # do_action = button_phold.button(button_type, key=stop_1, on_click=clicked, args=[2])

    # if st.session_state.clicked[2]:
    #     next_idx = f"alt_{n}"
    #     name = str(dataset.name.iloc[next_idx])
    #     address = str(dataset.address.iloc[next_idx])

    #     col1.markdown(name)
    #     col1.markdown(address)
        
    #     if n < 3:
    #         n += 1
        
    #     else:
    #         n = 1

    #     button_phold.empty()  #  remove button


    # #Activity
    # col1.write("2. Activity:")

    # alt_1 = int(dataset.neighbour_1.iloc[stop_2])
    # alt_2 = int(dataset.neighbour_2.iloc[stop_2])
    # alt_3 = int(dataset.neighbour_3.iloc[stop_2])

    # col1.write(str(dataset.name.iloc[stop_2]))
    # col1.write(str(dataset.address.iloc[stop_2]))

    # #Afternoon Drinks
    # col1.write("3. Afternoon Drinks:")

    # alt_1 = int(dataset.neighbour_1.iloc[stop_3])
    # alt_2 = int(dataset.neighbour_2.iloc[stop_3])
    # alt_3 = int(dataset.neighbour_3.iloc[stop_3])

    # col1.write(str(dataset.name.iloc[stop_3]))
    # col1.write(str(dataset.address.iloc[stop_3]))

    # #Dinner
    # col1.write("4. Dinner:")

    # alt_1 = int(dataset.neighbour_1.iloc[stop_4])
    # alt_2 = int(dataset.neighbour_2.iloc[stop_4])
    # alt_3 = int(dataset.neighbour_3.iloc[stop_4])

    # col1.write(str(dataset.name.iloc[stop_4]))
    # col1.write(str(dataset.address.iloc[stop_4]))

    # #Evening Out
    # col1.write("5. Evening Out:")

    # alt_1 = int(dataset.neighbour_1.iloc[stop_5])
    # alt_2 = int(dataset.neighbour_2.iloc[stop_5])
    # alt_3 = int(dataset.neighbour_3.iloc[stop_5])

    # col1.write(str(dataset.name.iloc[stop_5]))
    # col1.write(str(dataset.address.iloc[stop_5]))


