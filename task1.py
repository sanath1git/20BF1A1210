import requests
from datetime import datetime, timedelta
import os
from flask import Flask
 

app = Flask(__name__)
 

@app.route('/trains',methods=['GET'])
def GET_TRAINS():
    res = {}
    token = os.environ['ACCESS_TOKEN']
    response = requests.get('http://104.211.219.98/train/trains', headers={'Authorization': 'access_token {token}'}).json()
    current_time = datetime.now()

    min_departure_time = current_time + timedelta(minutes=30)

    filtered_trains = [
        train for train in response['trains']
        if datetime.strptime(response['departure_time'], '%H:%M:%S') + timedelta(minutes=response["delay"]) > min_departure_time.time() > min_departure_time
    ]

    filtered_trains = sorted(filtered_trains,key=lambda train: (-train['availability'], train['fare']))

    return filtered_trains
 
if __name__ == '__main__':
    app.run()