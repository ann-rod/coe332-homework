# Meteorite Landing Data Flask App with Redis Database and Kubernetes Cluster

## This app allows the user to post and retrieve meteorite landing data that is stored in a Redis database and orchestrated by a Kubernetes cluster.

Use this link to download the data used in this app:
https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json 

Type the following command in the terminal to download into the current directory:
~~~
wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
~~~


** Using this App: **
To use this app along with the Kubernetes cluster, you must first make sure that Kubernetes is installed (see [here](https://kubernetes.io/docs/setup/) for more info.).
To check if Kubernetes has been properly installed, type the following into the terminal:
~~~
kubectl version -o yaml
~~~
If downloaded properly, the terminal will pring a message with client and server version information.


** Deploying to Kubernetes **

Within a Kubernetes cluster, copy and paste all the .yml files within this repository into the directory where Kubernetes is open.
For each file, you must create the pod instance by typing the following into the terminal:
~~~
 kubectl apply -f <file-name>.yml
~~~
This should create instances of the Flask application and Redis server within the Kubernetes cluster that will persist.

At this point, you can curl routes from the terminal as long as you have the IP Address of the Flask service.
To find the IP Address, type:
~~~
kubectl get service
~~~
This will show all the services open in the cluster. Find the one that says 'flask-service', and copy the IP Address listed.

Now, you can use the app methods by typing:
~~~
curl <IP Address>:5000/<method>
~~
In the example above, the '5000' stands for the port number of the Flask app. If you cannot connect to the app, you will have to open the .yml file of the flask service and find the port number listed.

To find the methods that can be used with this app, see my Flask app repository [here](https://github.com/ann-rod/coe332-homework/tree/main/homework05).
