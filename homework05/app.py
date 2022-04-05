from flask import Flask, request
import json
import redis


app = Flask(__name__)

@app.route('/data', methods = ['GET', 'POST'])
def data(search_start = 0: int) -> str:
    '''
    This app contains two methods that allow the user to post or retrive data, respectively,
    from a redis database server.

    METHODS:
        POST: Posts the ML_Data_sample.json data into the database as a hash.
        GET: Returns the data stored in the database as a json list.
    
    Args:
        search_start (int): An integer that indicates the index at which the user wishes
                            to begin retrieval of data. Defaults to 0 if unspecified.

    Returns:
        POST method:
            string (str): A confirmation message if the posting process runs successfully.
        
        GET method:
            list (list): A json list with the meteorite landing data. 
    '''
    if(request.method == 'POST'):
        counter = 0
        #load data into redis database
        data_dict = json.load(open('ML_Data_Sample.json','r'))
        data_list = data_dict['meteorite_landings']
        for d in data_list:
            data = data_list[d]
            rd.hset(str(counter), mapping={'name': data['name'],\
                    'id': data['id'], 'recclass': data['recclass'],\
                    'mass (g)': data['mass (g)'], 'reclat': data['reclat'],\
                    'reclong': data['reclong'], 'GeoLocation': data['GeoLocation']})
            counter += 1
        return 'Meteorite Landing data uploaded.'

    elif(request.method == 'GET'):
        # read data out of redis
        # return data as a json list
        # BONUS: add start query parameter for value at which to start return from
        return_data = []
        for key,value in rd.hscan_iter():
            return_data.append(json.loads(value.decode('utf-8')))
        return return_data
            
    else:
        # return error message with the correct methods to use
        return '    The method given does not exist.\n        To update\
                the data, please use "POST".\n        To retrieve data,\
                please use "GET".'

if __name__ == '__main__':
    rd = redis.Redis(host='172.17.0.19', port='6379')
    app.run(debug=True, host='0.0.0.0')
