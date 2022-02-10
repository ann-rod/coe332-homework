# homework02
*Contains my solutions for homework02 assigned in COE 332.*

The code within this directory creates randomly generated meteorite landing data and stores it within a .json file. The created .json file is then used
to calculate how long it would take to travel to each site for a sample and prints the results.

## Functions:
**generate_sites.py**:
Creates a list of dictionaries with each dictionary containing an id, latitude, longitude, and meteorite composition keys. The list is then saved as a dictionary with key 'sites' to the file 'meteorites.json'.


**calculate_trip.py**:
Reads in the data from 'meteorites.json' and uses it to calculate and print how long a trip to sample each site (in given order) would take.


 **meteorites.json**:
A data file created by the program 'generate_sites.py' that is rewritten every time 'generate_sites.py' is run. It contains a dictionary whose value is a list of dictionaries with meteorite site information.



  ***Caution: ALWAYS run 'generate_sites.py' first when using this code and make sure a
           'meteorites.json' file exists in the directory before using 'calculate_trip.py'.***


 ## Results:
This program prints specifics on a journey to sample each meteorite that was randomly generated. It takes into account a starting point, travel speed, planet radius, distance, and the composition of the meteorite. It should print time updates at each leg of the trip and a summary with the total time and total distance the trip should take.
