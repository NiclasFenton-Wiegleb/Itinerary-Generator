import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points

def convert_geo(df):
    '''Convert a dataframe with coordinates into a geodataframe'''
    gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.long_coordinates, df.lat_coordinates), crs="EPSG:4666"
    )
    return gdf

def find_neighbour(gdf, n, origin_idx):
    '''Find the closest n number of neighbours to the given origin'''
    
    #Set origin point
    orig = gdf.geometry[origin_idx]

    neighbours = []

    #Create list of all points in df excluding origin
    #Neighbours need to have the same hierarchy lvl
    orig_hr = gdf.hierarchy[origin_idx]

    hr_list = list(gdf.index[gdf.hierarchy == orig_hr])

    dest_list = list(gdf.geometry[x] for x in hr_list if x != origin_idx)

    while len(neighbours) < n:

        destinations = MultiPoint(dest_list)
        n_points = nearest_points(orig, destinations)
        neighbour = n_points[1]

        if neighbour in neighbours:
            dest_list.remove(neighbour)
            continue
        else:
            neighbours.append(neighbour)
            dest_list.remove(neighbour)
    
    return neighbours

def get_idx(neighbours_lst, orig):
    '''Retrieves the index for the neighbouring points provided in list'''
    n_list = []

    #Iterate through Points object in neighbours
    #Select first element and exclude origin
    for x in neighbours_lst:
        val = np.array(orig)
        idx_series = gdf.index[gdf.geometry == x]
        idx = np.setdiff1d(idx_series,val)
        n_list.append(idx[0])
    
    return n_list



if __name__ == "__main__":

    #Import data
    df = pd.read_csv("./ItineraryGenerator_Dataset.csv")
    gdf = convert_geo(df)

    orig_lst = list(df.index)
    n = 3

    #Creat empty lists for each neighbour
    n_1 = []
    n_2 = []
    n_3 = []

    for idx in orig_lst:

        #Find nearest neighbours
        neighbours = find_neighbour(gdf, n=n, origin_idx=idx)
        n_list = get_idx(neighbours, idx)
        
        n_1.append(n_list[0])
        n_2.append(n_list[1])
        n_3.append(n_list[2])
    
    df["neighbour_1"] = n_1
    df["neighbour_2"] = n_2
    df["neighbour_3"] = n_3

    df.to_csv("IG_neighbours.csv")