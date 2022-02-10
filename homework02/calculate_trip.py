#!/usr/bin/env python3

import json
import math

START_LATITUDE = 16.0
START_LONGITUDE = 82.0
MARS_RADIUS = 3389.5  # In km
MAX_SPEED = 10  # In km/h
METEOR_SAMPLING_TIME = {"stony": 1, "iron": 2, "stony-iron": 3}  # In hours 


def calc_distance_gc(lat1: float, long1: float, lat2: float, long2: float) -> float:
    """
    When given the latitudes and longitudes of two points on a spherical body,
    this function calculates the great-circle distance between those points.
 
    Args:
        lat1 (float): The latitude of the first point.
        long1 (float): The longitude of the first point.
        lat2 (float): The latitude of the second point.
        long2 (float): The longitude of the second point.

    Returns:
        distance (float): Returns the great-circle distance between the points.    
    """
    lat1, long1, lat2, long2 = map( math.radians, [lat1, long1, lat2, long2] )
    d_sigma = math.acos(math.sin(lat1)*math.sin(lat2) + \
                    math.cos(lat1)*math.cos(lat2)* \
                    math.cos(abs(long1-long2)))
    return MARS_RADIUS * d_sigma


def trip_calc(site_list):
    """
    Given a list of meteorite sites, where each entry is a dictionary with
    longitude, latitude, and composition information on the meteorite, this
    function calculates how long the trip to sample them in input order
    would take and prints updates as it computes.
 
    Args:
        site_list (list of dicts): A list of meteorite sites where each entry
                                   is a dictionary with "latitude", "longitude",
                                   and "composition" keys.
    """
    leg = 0
    total_time = 0
    total_distance = 0

    for i in range(len(site_list)):
        leg += 1
        if(i == 0):
            lat1 = START_LATITUDE
            long1 = START_LONGITUDE
        else:
            lat1 = site_list[i-1]["latitude"]
            long1 = site_list[i-1]["longitude"]

        leg_time = calc_distance_gc(lat1, long1, site_list[i]["latitude"],\
                   site_list[i]["longitude"]) / MAX_SPEED        
        sample_time = METEOR_SAMPLING_TIME[ site_list[i]["composition"] ]
        total_time += (leg_time + sample_time)
        total_distance += (leg_time * MAX_SPEED)

        print("leg = ", leg, ", ", "time to travel = ", leg_time, " hr", ", ",\
              "time to sample = ", sample_time, " hr", sep = "")
    print("===================================================================")
    print("number of legs = ", leg, ", ", "total time elapsed = ", total_time\
          , " hr", ", ", "\n", "total distance traveled: ", total_distance,\
          " km", sep = "")


def main():
    with open('meteorites.json', 'r') as f:
        site_data = json.load(f)
    trip_calc(site_data["sites"])


if __name__ == '__main__':
    main()
