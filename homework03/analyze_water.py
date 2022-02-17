#!/usr/bin/env python3
import json
import math
from typing import List
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


TURBIDITY_THRESHOLD = 1.0 #  in NTU
DECAY_FACTOR = 0.02 #  per hour

def calc_turbidity(a0: float, I90: float) -> float:
    '''
    Given a calibration constant value and a detector current value,
    this function will return the turbidity in NTU.

    Args:
        a0 (float): The calibration constant of a water sample.
        I90 (float): The detector current value of a water sample.

    Returns:
        turbidity (float): The turbidity (in NTU) of the sample.
    '''
    return a0 * I90 

def calc_threshold_min_time(T: float) -> float:
    '''
    When given a turbidity value in NTU, this function returns the 
    amount of time (in hours) it would take for the water sample to
    be safe for use.

    Args:
        T (float): The turbidity measurement (in NTU) of the water sample.
    
    Returns:
        hours (float): The amount of time it will take for the turbidity
                       to be under the safety threshold.
    '''
    return math.log(TURBIDITY_THRESHOLD/T)/math.log(1-DECAY_FACTOR) if\
        (T >= TURBIDITY_THRESHOLD) else 0

def print_results(T: float, hours: float):
    '''
    Given a turbidity value (in NTU) and time value (in hours), this
    function prints information on the sample and whether the sample
    is safe for use.

    Args:
        T (float): The turbidity (in NTU) of the sample.
        hours (float): The amount of time it will take for the turbidity
                       to be under the safety threshold.
    '''
    print('Average turbidity based on five most recent measurements =',\
        T, 'NTU')
    if( T >= TURBIDITY_THRESHOLD):
        logging.warning('Turbidity is above threshold for safe use.')
    else:
        logging.info('Turbidity is below threshold for safe use.') 
    print('Minimum time required to return below a safe threshold =',\
        hours, 'hours') 

def main():
    with open('turbidity_data.json', 'r') as f:
        data = json.load(f)
    
    # Assumes that the last five entries are the most recent.
    most_recent_data = data['turbidity_data'][-5:]
    
    # Unravels the data
    a0_list = []
    I90_list = []
    for i in range(len(most_recent_data)):
        a0_list.append(most_recent_data[i]['calibration_constant'])
        I90_list.append(most_recent_data[i]['detector_current'])

    T = calc_turbidity(sum(a0_list)/len(a0_list), sum(I90_list)/len(I90_list))    
    print_results(T, calc_threshold_min_time(T))

if __name__ == '__main__':
	main()
