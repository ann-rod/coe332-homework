# Meteorite Landing Data Flask App with Redis database

## This app allows the user to post and retrieve meteorite landing data that is stored in a Redis database.


Use this link to download the data used in this app:
https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json 

Type the following command in the terminal to download into the current directory:
~~~
wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
~~~


## Redis Database

  **Create a Redis database to store the data in**:
  -Make sure you are logged in to Docker and have installed it into your computer (see this [link](https://docs.docker.com/engine/install/ubuntu/) for help downloading Docker)
  -Type the following line into your terminal.
  ~~~
  docker run -d -p 6426:6379 -v $(pwd)/data:/data:rw --name=<username>-redis redis:6 --save 1 1
  ~~~
  -If you wish to change any of the settings above, here is what they refer to:
    - '-d' runs the portal in the background.
    - '-p 6426:6379' specifies which of your local ports (here we used 6424) will connect to the default container port (6379).
    - '-v $(pwd)/data:/data:rw' this section mounts the current directory into the container to be edited by the database in read/write (rw) mode. The '-v' flag indicates that you wish to mount a directory, and what follows is the local path you wish to mount. Notice that we added '/data' at the end to allow the database to create a data folder to add to.
    - '--name=<username>-redis' allows the user to name the server so that it is easier to locate.
    - 'redis:6' refers to the default image of the redis database that Docker contains.
    - '--save 1 1' tells the database to store its backups at a rate of 1 backup every 1 second, respectively. These backups will save to the data folder that we allowed the database to create.
    

## Dockerfile
  
  **Build Your own Dockerfile**:
  -Download the code in this directory.
  -Open up *Dockerfile* using your text editor of choice and make the necessary changes (whether you need to use different versions of the software used    or would prefer to come up with your own commands)
  -Build a new image by typing 'docker build -t <username>/app.py:latest .' in the command line.
  -Run the application by typing 'docker run --name "<name your container>" -d -p 5024:5000 <username>/app.py:latest'.
~~~~
docker build -t docker build -t <username>/app.py:latest .
docker docker run --name "<name your container>" -d -p 5024:5000 <username>/app.py:latest
~~~~

  **Using the Complete Dockerfile Provided**:
  -If you wish to use the Dockerfile provided, and downloaded everything in the repo, change into the directory where the code is, simply type the following into the terminal:
~~~~
docker build -t docker build -t <username>/app.py:latest .
docker docker run --name "<name your container>" -d -p 5024:5000 <username>/app.py:latest
~~~~

 ## Using the App 
 
 The app contains to methods:
 
 **POST**: send the meteorite landing data into the database.
 
 Command:
 
 ~~~
 curl localhost:5024/data -X POST
 ~~~
 
 
 **GET**: retrieve the data in the database as a list.
 
 Command:
 
 ~~~
 curl localhost:5024/data GET
 ~~~

