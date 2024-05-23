# Itinerary-Generator

The idea for this project was to create a web app that could generate an itinerary for a day out in Manchester. It's a great place to visit and live, but it's a lot of work to find the best places and activities on your own.

*Tech Stack:*

- Python
- Jupyter Notebook
- Reinforcement learning algorithm
- GeoPandas
- JavaScript
- CSS
- HTML
- Firebase
- Google Analytics
- Google Console

## Dataset

The dataset has been manually curated to ensure any recommendations are up-to-date and high quality. This required extensive local knowledge and knowing where to look for suggestions. The dataset itself contains the place names, addresses, coordinates, hierarchy (where in the itinerary it should sit), as well as links to the relevant websites.

## Reinforcement Learning Algorithm

A reinforcement learning algorithm was needed to figure out the optimal routes to recommend, depending on where you start. This is optimised based on finding the recommendation in the next level of the hierarchy with the closest physical distance to the current stop. There is also a weighting worked into the algorithm, that allows for specific recommendations to be favoured over others. The exploration of the algorithm is detailed in the `Itinerary_generator.ipynb` notebook and implemented in the `generator_training.py` script.

The hierarchy for the itinerary is as follows: Brunch, Activity, Afternoon Drinks, Dinner, Evening Out;

## Nearest Neighbours

To provide users with alternative suggestions, if they are not particularly taken with any of the recommendations in the generated itinerary, the three closest recommendations in the same level of the hierarchy were identified also. The `n_neighbour.py` script selects the points in the same level of hierarchy as the original recommendation and identifies the three closest neighbours by physical distance.

## App

The `app.py` script wraps the optimal routes and nearest recommendations into a usable streamlit app. In fact there are two versions of the streamlit app, one is optimised for desktop and one for mobile. The final step is to use React to deploy the web app. This means using javascript and html to create the front-end, style the page using css and deploying it via firebase.

*Access the final website here:* https://manchester-makeyourday.co.uk/
