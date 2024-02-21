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

def find_neighbour(origin, list):
    orig = gdf.geometry[0]
    destinations = MultiPoint(list)
    n_points = nearest_points(orig, destinations)

    return n_points[1]


if __name__ == "__main__":

    df = pd.read_csv("./ItineraryGenerator_Dataset.csv")
    gdf = convert_geo(df)

    orig = gdf.geometry[0]
    nearest_points = []

    idx = 0

    for x in range(3):

        dest_list = list(gdf.geometry)
        destinations = MultiPoint(dest_list)
        print(type(orig), type(destinations))
        n_points = nearest_points(orig, destinations)
        neighbour = n_points[1]
        print(neighbour)
        nearest_points.append(neighbour)
        dest_list.remove(neighbour)

    print(nearest_points)

    # n = 0

    # for x in range(3):
    #     print(f"Nearest Neighbour {n}: {nearest_points[n]}")