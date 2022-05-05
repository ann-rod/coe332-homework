## ISS Tracker App Example Flowchart

![This flowchart shows the functionality of the /read-data route of the ISS Tracking app found in my ISS Tracking App repo. Description of flowchart written in the README.](https://github.com/ann-rod/coe332-homework/blob/main/homework07/read-data-flowchart.png)

This flowchart shows the functionality of the /read-data route of the ISS Tracking app found [here](https://github.com/ann-rod/ISS-Tracker-app).

The /read-data Flask route of the ISS Tracking app is meant to initialize data within a program by reading in two files of data from the local computer. When accessed, the route searches for the two files in the local directory (this would require that both files be named appropriately and stored in the same folder as the app), and opens them for reading. 

For each file, the program will read all of its contents and convert them into a python dictionary object in order to make the data accesible to the program. 

Currently, once each file's contents are stored in their respective python dictionaries, the user will receive a successful upload message. However, in a future update it is planned to add an additional step to this program that uploads the two dicitionaries into a Redis server before returning a success message. This would allow the data to persist if the user exits the program or loses the original data files.
