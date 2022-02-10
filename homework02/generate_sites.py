#!/usr/bin/env python3

import json
import random

LATITUDE_LOWER_BOUND = 16.0
LATITUDE_UPPER_BOUND = 18.0
LONGITUDE_LOWER_BOUND = 82.0
LONGITUDE_UPPER_BOUND = 84.0
METEORITE_COMPOSITIONS = ["stony", "iron", "stony-iron"]

def random_site(meteor_id):
    """
    This function creates a dictionary with randomly generated latitude,
    longitude, and composition to describe a meteorite landing site.
    
    Args:
        meteor_id (int): A label used to identify a meteorite site

    Returns:
        meteor_info (dictionary): A dictionary that contains the randomly
                                  generated meteor information. It contains
                                  float and string values.
    """
    lat = random.random() * (LATITUDE_UPPER_BOUND - LATITUDE_LOWER_BOUND)\
          + LATITUDE_LOWER_BOUND
    lon = random.random() * (LONGITUDE_UPPER_BOUND - LONGITUDE_LOWER_BOUND)\
          + LONGITUDE_LOWER_BOUND
    comp = METEORITE_COMPOSITIONS[random.randint(0,2)]
    
    meteor_info = {"site_id": meteor_id, "latitude": lat, "longitude": lon,\
                   "composition": comp}
    return meteor_info


def main():
    data = {}
    data["sites"] = []     
    for i in range(1,6):  # Creates 5 sites to add to the data['sites'] list.
        data["sites"].append(random_site(i))
    
    with open('meteorites.json', 'w') as out:
        json.dump(data,out, indent=2)



if __name__ == '__main__':
    main()


