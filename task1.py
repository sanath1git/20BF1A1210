import requests
from datetime import datetime, timedelta
import os
from flask import Flask
 

app = Flask(__name__)
 

@app.route('/trains',methods=['GET'])
def GET_TRAINS():
    token = os.environ['ACCESS_TOKEN']
    response = requests.get('http://104.211.219.98/train/trains', headers={'Authorization': 'access_token {token}'})

    current_time = datetime.now()


    return ""
 



if __name__ == '__main__':
 
    
    app.run()