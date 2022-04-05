docker build -t ann-rod/hw05:latest .
docker run --name "annrod-flask" -d -p 5024:5000 ann-rod/hw05:latest


docker run -d -p 6426:6379 -v $(pwd)/data:/data:rw --name=annrod-redis redis:6 --save 1 1

# Meteorite Landing Data Flask App with Redis database

## This app allows the user to post and retrieve meteorite landing data that is stored in a Redis database.


Use this link to download the data used in this app:
https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json 

Type the following command in the terminal to download into the current directory:
~~~
wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
~~~




