# Meteorite Landing Analysis: Homework 04
*Contains my solutions for homework04 assigned in COE 332.*

The code within this directory writes a summary of calculations made from a meteorite landing data file.

## Files:
**ml_data_analysis.py**:

-Reads in data from *Meteorite_Landings.json*.
-Calculates the amount of meteorites in the set, where they landed, and the class of each meteorite.
-Prints a summary message of the data that contains the calculations mentioned above.



**test_ml_data_analysis.py**:

-A series of tests done on each function of *ml_data_analysis.py* to make sure everything is running correctly.
-Requires installation of pytest.



**Meteorite_Landings.json**:

-A data file that contains a dictionary with a key of 'meteorite_landings' that contains a list of dictionaries filled with data on a particular meteorite landing.
-Each dictionary entry represents a meteorite and includes its name, ID, class, mass, latitude, longitude, and GeoLocation.



**Dockerfile**:

-Contains the information necessary to create a container that successfully runs this code.



## How to Run this Code:

**Using an existing image on Docker Hub:**

(To run this code using the image that has already been created.)
-Download the application by typing into the command line 'docker pull annrod/ml_data_analysis:hw04'
-Run the application using the command 'docker run --rm -it annrod/ml_data_analysis:hw04 /bin/bash'
-The program can now be used within the python interactive mode. Use 'python3 ml_data_analysis.py Meteor_Landings.json' to run the code.
~~~~
docker pull annrod/ml_data_analysis:hw04
docker run --rm -it annrod/ml_data_analysis:hw04 /bin/bash
python3 ml_data_analysis.py Meteor_Landings.json
~~~~


**Building a New Image from a Dockerfile:**

-Download the code in this directory.
-Open up *Dockerfile* using your text editor of choice and make the necessary changes.
-Build a new image by typing 'docker build -t username/ml_data_analysis:hw04 .' in the command line.
-Run the application by using the command 'docker run --rm -it username/ml_data_analysis:hw04 /bin/bash'
-The program can now be used within the python interactive mode. Use 'python3 ml_data_analysis.py Meteor_Landings.json' to run the code.
~~~~
docker build -t username/ml_data_analysis:hw04 .
docker run --rm -it username/ml_data_analysis:hw04 /bin/bash
python3 ml_data_analysis.py Meteor_Landings.json
~~~~


**Run with sample data (Meteorite_Landings.py):**

-To use with the sample data, run either set of instructions above.


**Run with your own data:**

-


**Run tests using pytest:**

-Download the application using any of the methods above.
-Once in the python interactive mode, make sure that pytest is installed by typing 'pytest --version'. If there are no error messages pytest installed properly.
-Make sure you are in the 'code' directory by typing 'cd ~/code/'. Make sure the files listed above are in your current directory (you can check by using the commands 'ls').
-Use the 'pytest' command on the command line.
-Pytest will then perform tests on the code, and if it still works correctly, all the tests should pass.
~~~~
pytest --version
cd ~/code/
pytest
===================================================== test session starts =====================================================
platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
rootdir: /
collected 6 items                                                                                                             

test_ml_data_analysis.py ......                                                                                         [100%]

====================================================== 6 passed in 0.01s ======================================================
~~~~


##Input Data:
The data used in this program can be found at: https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json

For this code to work, data should be in a .json file in the format of a dictionary that holds a list or dictionaries with the meteorite data.
ex:
~~~~
{
  "meteorite_landings": [
    {
      "name": "Ruiz",
      "id": "10001",
      "recclass": "L5",
      "mass (g)": "21",
      "reclat": "50.775",
      "reclong": "6.08333",
      "GeoLocation": "(50.775, 6.08333)"
    },
    ~~~~
