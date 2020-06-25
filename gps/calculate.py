"""Manipulate gps data."""
import pandas as pd
import numpy as np

from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier

import hdbscan

# read data


def load_data(data_path):
    """Load and preprocess data in numpy array.


    Args:
        data_path (string): location of the data

    Returns:
        np array: X the data of shape num * 2
    """
    # load data
    df = pd.read_csv('data/taxi_data.csv')

    # remove duplicates and null
    df.dropna(inplace=True)
    df.drop_duplicates(subset=['LON', 'LAT'], keep='first', inplace=True)
    X = np.array(df[['LON', 'LAT']], dtype='float64')
    data = X

    return data


def getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2):
    """Measure distance between gps coordinates.

    Args:
        lat1 (float): latitude of point 1
        lon1 (float): longitude of point 1
        lat2 (float): latitude of point2
        lon2 (float): longitude of point2

    Returns:
        d (float): euclidean distance in kilometers
    """
    R = 6371  # Radius of the earth in km
    dLat = np.deg2rad(lat2-lat1)  # deg2rad below
    dLon = np.deg2rad(lon2-lon1)
    a = (np.sin(dLat/2) * np.sin(dLat/2) +
         np.cos(np.deg2rad(lat1)) * np.cos(np.deg2rad(lat2)) * np.sin(dLon/2) * np.sin(dLon/2))
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    d = R * c  # Distance in km
    return d


def find_center_radius(data, cluster_labels):
    """Find the radius and centroid of the clusters.

    Args:
        data (np arr): location data in lng and lat
        cluster_labels (arr): cluster prediction of all data

    Returns:
        centers: the centroids of the cluster
        rads: the radius or approximate size of the cluster
    """
    centers = []
    rads = []
    X = data
    for cluster in np.unique(class_predictions)[1:]:
        #     print(cluster)
        X_sel = X[class_predictions == cluster]
        cluster_centre = np.mean(X[class_predictions == cluster], axis=0)
        centers.append(cluster_centre)
        diff = X_sel - cluster_centre
    #     print(diff)
        diff = np.linalg.norm(diff, axis=1)
        farthest_pt_centre = np.argmax(diff)
        radius_pt = getDistanceFromLatLonInKm(
            X_sel[farthest_pt_centre][1], X_sel[farthest_pt_centre][0],
            cluster_centre[1], cluster_centre[0])*1000
        rads.append(radius_pt)
    return centers, rads


# perform clustering
X = load_data('fire')
model = DBSCAN(eps=0.01, min_samples=5).fit(X)
class_predictions = model.labels_

centers, rads = find_center_radius(X, class_predictions)

print(len(centers))