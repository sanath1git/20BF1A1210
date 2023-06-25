import requests
from flask import Flask,request
from urllib.parse import urlparse

app = Flask(__name__)
 

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False

@app.route('/numbers')

def geta_uls_response():
    links = []
    res = []
    query_urals = request.query_string
    url = query_urals.split(b"&")
    for i in url:
        respon = requests.get(i.decode("ascii").split("=")[1])
        if respon.status_code == 200:
            res = res + respon.json()["numbers"]
    res = list(set(res))
    res.sort()
    return res



if __name__ == '__main__':
 
    
    app.run()