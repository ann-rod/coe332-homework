## Water Turbidity Test
*Contains my solutions for homework03 assigned in COE 332.*

The code within this directory reads in the file turbidity_data.json, which stores data of collected water samples, and calculates the turbidity of the samples as well as the amount of time it would take for
samples to be safe for use. 

## Files:
**analyze_water.py**:
This program reads in the data from turbidity_data.json and takes the average calibration constant and detector current values, respectively, of the 5 most recent entries (assuming the last 5 entries are the most recent).
Then, the program calculates the turbidity of the water samples using the data and prints out information about the samples including turbidity and how long it would take for the water samples to be usable if the turbidity
levels are above a certain threshold.


**test_analyze_water.py**:
This program performs a variety of unit tests on the functions from analyze_water.py to ensure it functions properly. It can be used with pytest.


 *turbidity_data.json*:
This data file can be downloaded from https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json using the 'wget' command in the terminal.



  ***Caution: Make sure that the file turbidity_data.json exists in the same directory as the rest of this code before using.***

## Instructions:
In order to successfully run this code, you must:

  **1.** Download this directory.
  
  **2.** Download turbidity_data.json from the link above, making sure it's in the copy of this directory on your computer.
  
  **3.** Optional: install pytest in order to use test_analyze_water.py
  
  **4.** Run analyze_water.py
  
  **5.** Optional: Run pytest to check for errors in analyze_water.py
  

 ## Results:
This programs prints the turbidity of the water sample data inputted as well as the amount of time it would take for the water to be safe for use if the turbidity is above a safe threshold. This information can be used to determine if and when
the water samples measured would be safe to use or consume.
