'''This script should be used to train the Deep Reinforcement Learning matrix
and finding the optimised routes for each starting point.'''

import numpy as np
import pandas as pd
import geopandas as gpd
import random


def convert_geo(df):
    '''Convert a dataframe with coordinates into a geodataframe'''
    gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.long_coordinates, df.lat_coordinates), crs="EPSG:4666"
    )
    return gdf

def get_edges_distances(gdf):
    '''Create dataframe with edges and distances'''
    df_edges = pd.DataFrame(columns=["names","edges", "distance", "weighting"])

    edges=[]
    distance=[]
    name = []
    weightings = []

    for i in range(len(gdf)):
        #select point 1
        pnt1 = i
        name1 = gdf.name.loc[i]
        hierarchy_1 = gdf["hierarchy"][i]
        weighting_1 = gdf["weighting"].loc[i]
        #iterate over df and find points above in the hierarchy
        for j in range(len(gdf)):
            #select point 2
            pnt2 = j
            name2 = gdf.name.loc[j]
            hierarchy_2 = gdf["hierarchy"][j]
            weighting_2 = gdf["weighting"].loc[j]

            #Check for hierarchy higher than point 1
            if int(hierarchy_2) == (int(hierarchy_1) + 1):
                #Append edges
                edges.append((pnt1, pnt2))
                name.append((name1, name2))
                weighting = weighting_1 *weighting_2
                weightings.append(weighting)
            else:
                continue
    #Itirate over edges list and add distances between the two points        
    for x in edges:

        index1 = x[0]
        index2 = x[1]
        pnt1 = gdf.geometry[index1]
        pnt2 = gdf.geometry[index2]

        points_df = gpd.GeoDataFrame({'geometry': [pnt1, pnt2]}, crs='EPSG:4666')
        #Changing EPSG makes the code work - the distances don't need to be exact
        points_df = points_df.to_crs('EPSG:5234')
        points_df2 = points_df.shift() #We shift the dataframe by 1 to align pnt1 with pnt2
        dis = points_df.distance(points_df2)
        #Append distance to list
        distance.append(int(dis[1]))
    
    #Normalise distances by dividing by max distance
    
    distance_norm = []

    for x in distance:
        dis_norm = x/max(distance)
        distance_norm.append(dis_norm)


    df_edges["edges"] = edges
    df_edges["distance"] = distance_norm
    df_edges["names"] = name
    df_edges["weighting"] = weightings

    df_edges.to_csv("edges.csv", index=False)

    return df_edges

def init_matrix(df, df_edges, matrix_size):
    '''We create a matrix with the initial rewards. High reward for reaching the goal,
    negative distance between desirable edges as reward and all other points as very low reward'''

    R = np.zeros((matrix_size,matrix_size))
    #40,000 to be assigned to all un-desirable edges
    R = np.full_like(R, 0)

    #Identify list of goal points
    goal = []

    for i in range(len(df.index)):

        if df.hierarchy.loc[i] == 4:
            goal.append(i)
        else:
            continue


    #Assign negative distance to paths and 2000 to goal-reaching point
    for ind in range(len(df_edges.index)):
        dis = df_edges.distance[ind]
        edge = df_edges.edges[ind]
        weight = df_edges.weighting[ind]
        if edge[1] in goal:
            R[edge] = 200
        else:
            R[edge] = (1-dis)*weight

        if edge[0] in goal:
            R[edge[::-1]] = 200
        else:
            # reverse of point
            R[edge[::-1]]= (1-dis)*weight

    #Add goal point round trip
    R[goal,goal]= 200

    return R

def available_actions(state, R):
    '''Returns list of available actions'''
    current_state_row = R[state,]
    av_act = np.where(current_state_row > 0)[0]
    return av_act

def sample_next_action(available_actions_range):
    '''Returns the next action to take from list'''
    next_action = int(np.random.choice(available_actions_range,1))
    return next_action

def update(current_state, action, gamma, Q, R):
    '''updates matrix based on reward for action taken'''
    max_index = np.where(Q[action,] == np.max(Q[action,]))[1]

    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]

    Q[current_state, action] = R[current_state, action] - gamma * max_value

    if (np.max(Q) > 0):
        return(np.sum(Q/np.max(Q)*100))
    else:
        return (0)

def training(Q, gamma, verbose,R):
    '''Trains the matrix to find ideal routes to goal'''
    scores = []
    for i in range(3000):
        current_state = np.random.randint(0, int(Q.shape[0]))
        available_act = available_actions(current_state, R)
        action = sample_next_action(available_act)
        score = update(current_state,action,gamma, Q, R)
        scores.append(score)
    # print(scores)


def opt_route(current_state, trained_Q, df):
    '''Find the optimised route to the goal from starting point'''
    
    current_state_hr = df["hierarchy"][current_state]
    
    steps = [current_state]

    while current_state_hr != 4:

        next_step_index = np.where(trained_Q[current_state,] == np.max(trained_Q[current_state,]))[1]
        
        if next_step_index.shape[0] > 1:
            next_step_index = int(np.random.choice(next_step_index, size = 1))
            next_state_hr = df["hierarchy"][next_step_index]

            if next_state_hr == current_state_hr+1:

                # print(next_step_index, next_state_hr)
                steps.append(next_step_index)
                current_state = next_step_index
                current_state_hr = next_state_hr
            
            else:
                trained_Q[current_state, next_step_index] = 0
                continue
        else:
            next_step_index = int(next_step_index)
            next_state_hr = df["hierarchy"][next_step_index]


            if next_state_hr == current_state_hr+1:
                # print(next_step_index, next_state_hr)
                steps.append(next_step_index)
                current_state = next_step_index
                current_state_hr = next_state_hr
            
            else:
                trained_Q[current_state, next_step_index] = 0
                continue
    
    return steps

def get_route_data(df):
    '''This function trains a reinforcement matrix based on distance between points in ascending hierarchichal order.
    The matrix is used to find the optimal route from a starting point (hierarchy 0) to an end goal (hierarchy 4). Routes
    are compiled in a dataframe and saved as csv file.'''
    
    gdf = convert_geo(df)

    df_edges = get_edges_distances(gdf)

    MATRIX_SIZE = len(df.index)

    R = init_matrix(df=df, df_edges=df_edges, matrix_size= MATRIX_SIZE)

    #Framing Q Matrix
    Q = np.matrix(np.zeros([MATRIX_SIZE, MATRIX_SIZE]))
    Q = np.full_like(Q, 0)

    # learning parameter
    gamma = 0.8

    training(Q=Q, gamma= gamma, verbose=True, R=R)

    df_opt = pd.DataFrame(columns= ["original_index", "name", "stop_1", "stop_2", "stop_3", "stop_4", "stop_5"])

    states = list(df.index[df.hierarchy == 0])
    names = list(df.name[df.hierarchy == 0])

    df_opt["original_index"] = states
    df_opt["name"] = names

    stop_1 = []
    stop_2 = []
    stop_3 = []
    stop_4 = []
    stop_5 = []

    for state in states:
        steps = opt_route(current_state=state, trained_Q=Q, df=df)
        
        stop_1.append(steps[0])
        stop_2.append(steps[1])
        stop_3.append(steps[2])
        stop_4.append(steps[3])
        stop_5.append(steps[4])

    df_opt["stop_1"] = stop_1
    df_opt["stop_2"] = stop_2
    df_opt["stop_3"] = stop_3
    df_opt["stop_4"] = stop_4
    df_opt["stop_5"] = stop_5

    df_opt.to_csv("OptimalRoutes.csv", index=False)

    return df_opt

if __name__ == "__main__":

    df = pd.read_csv("./ItineraryGenerator_Dataset.csv")

    df_opt = get_route_data(df)

    print(df_opt)






