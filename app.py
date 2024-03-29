import streamlit as st
import pandas as pd
import numpy as np
import random
import folium
from streamlit_folium import st_folium, folium_static
import streamlit.components.v1 as components  # Import Streamlit

#Adding AdSense code here

st.markdown("""
<head>
    <meta name="google-adsense-account" content="ca-pub-6270659904604748">
</head>
    """, unsafe_allow_html=True)

# components.html("""""<head><meta name="google-adsense-account" content="ca-pub-6270659904604748"></head>""", width=200, height=200)
# HtmlFile = open('./test.html', 'r', encoding='utf-8')
# source_code = HtmlFile.read()
# print(source_code)
# components.html(source_code, height=600)


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

# Initialise Brunch session state
if 'brunch' not in st.session_state:
    st.session_state.brunch = 3


# Function to update the value in session state
def next_brunch(button):
    '''When the Next button is clicked, the text of the next
    alternative stop should be displayed'''
    if button < 3:
        st.session_state.brunch += 1
    else:
        st.session_state.brunch = 0

def previous_brunch(button):
    '''When the Previous button is clicked, the text of the previous
    alternative stop should be displayed'''
    if button <= 3 and button > 0:
        st.session_state.brunch -= 1
    else:
        st.session_state.brunch = 3

# Initialise Activity session state
if 'activity' not in st.session_state:
    st.session_state.activity = 3


# Function to update the value in session state
def next_activity(button):
    '''When the Next button is clicked, the text of the next
    alternative stop should be displayed'''
    if button < 3:
        st.session_state.activity += 1
    else:
        st.session_state.activity = 0

def previous_activity(button):
    '''When the Previous button is clicked, the text of the previous
    alternative stop should be displayed'''
    if button <= 3 and button > 0:
        st.session_state.activity -= 1
    else:
        st.session_state.activity = 3

# Initialise Drinks session state
if 'drinks' not in st.session_state:
    st.session_state.drinks = 3


# Function to update the value in session state
def next_drinks(button):
    '''When the Next button is clicked, the text of the next
    alternative stop should be displayed'''
    if button < 3:
        st.session_state.drinks += 1
    else:
        st.session_state.drinks = 0

def previous_drinks(button):
    '''When the Previous button is clicked, the text of the previous
    alternative stop should be displayed'''
    if button <= 3 and button > 0:
        st.session_state.drinks -= 1
    else:
        st.session_state.drinks = 3

# Initialise Dinner session state
if 'dinner' not in st.session_state:
    st.session_state.dinner = 3

# Function to update the value in session state
def next_dinner(button):
    '''When the Next button is clicked, the text of the next
    alternative stop should be displayed'''
    if button < 3:
        st.session_state.dinner += 1
    else:
        st.session_state.dinner = 0

def previous_dinner(button):
    '''When the Previous button is clicked, the text of the previous
    alternative stop should be displayed'''
    if button <= 3 and button > 0:
        st.session_state.dinner -= 1
    else:
        st.session_state.dinner = 3

# Initialise Evening session state
if 'evening' not in st.session_state:
    st.session_state.evening = 3

# Function to update the value in session state
def next_evening(button):
    '''When the Next button is clicked, the text of the next
    alternative stop should be displayed'''
    if button < 3:
        st.session_state.evening += 1
    else:
        st.session_state.evening = 0

def previous_evening(button):
    '''When the Previous button is clicked, the text of the previous
    alternative stop should be displayed'''
    if button <= 3 and button > 0:
        st.session_state.evening -= 1
    else:
        st.session_state.evening = 3



def select_route():
    st.session_state.route_idx[0] = random.randint(0, len(route_data))
    st.session_state.button[1] = True

col1, col2, col3 = st.columns((1, 3,1))

# Button with callback function
button = col2.button("Generate Itinerary", on_click=select_route)

if st.session_state.button[1] == True:

    # Initialise listes for each entry to draw from
    title_lst = ["1. Brunch", "2. Activity", "3. Afternoon Drinks", "4. Dinner", "5. Evening Out"]
    alt_lst = ["neighbour_1", "neighbour_2", "neighbour_3"]
    stop_lst = ["stop_1", "stop_2", "stop_3", "stop_4", "stop_5"]
    state_lst = [st.session_state.brunch, st.session_state.activity, st.session_state.drinks, st.session_state.dinner, st.session_state.evening]
    next_lst = [next_brunch, next_activity, next_drinks, next_dinner, next_evening]
    prev_lst = [previous_brunch, previous_activity, previous_drinks, previous_dinner, previous_evening]
    
    long_lst = [0,0,0,0,0]
    lat_lst = [0,0,0,0,0]
    name_lst = ["", "", "", "", ""]

    df = pd.DataFrame(columns=["long", "lat", "name", "stop"])
    
    for x, item in enumerate(stop_lst):

        col1, col2, col3 = st.columns((1, 3,1))

        state = state_lst[x]
        next_func = next_lst[x]
        prev_func = prev_lst[x]
        y = x+10

         # Next Button
        next_txt = "⇀"
        next_stop = col3.button(next_txt, on_click=next_func, key=x, args=[state])

        # Previous Button
        prev_txt = "↼"
        prev_stop = col1.button(prev_txt, on_click=prev_func, key=y, args=[state])

        if state == 3:

            #Id stop for Brunch
            stop = int(route_data[item][st.session_state.route_idx])

            col2.write(title_lst[x])  # title
            col2.write(dataset.name.iloc[stop])  # name
            col2.write(dataset.address.iloc[stop])  # address

            long_lst[x] = dataset.long_coordinates.iloc[stop] #longitude
            lat_lst[x] = dataset.lat_coordinates.iloc[stop] #latitude
            name_lst[x] = str(dataset.name.iloc[stop])
        
        else:

            column = str(alt_lst[state])
            stop = int(dataset[column][int(route_data[item][st.session_state.route_idx])])

            col2.write(title_lst[x])  # title
            col2.write(dataset.name.iloc[stop])  # name
            col2.write(dataset.address.iloc[stop])  # address

            long_lst[x] = dataset.long_coordinates.iloc[stop] #longitude
            lat_lst[x] = dataset.lat_coordinates.iloc[stop] #latitude
            name_lst[x] = str(dataset.name.iloc[stop])
        
    df.long = long_lst
    df.lat = lat_lst
    df.name = name_lst
    df.stop = title_lst

    m = folium.Map(location=[df.lat.mean(), df.long.mean()], 
                 zoom_start=11, control_scale=True)

    #Loop through each row in the dataframe
    for i,row in df.iterrows():
        #Setup the content of the popup
        iframe = folium.IFrame(str(row["stop"]) + ": " + str(row["name"]))
        
        #Initialise the popup using the iframe
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        
        #Add each row to the map
        folium.Marker(location=[row['lat'],row['long']],
                    popup = popup, c=row['name']).add_to(m)

    st_data = folium_static(m, width=700)

        


