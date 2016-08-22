from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    #return "Hello World!!"
    r = requests.get("https://1faoejtuza.execute-api.us-east-1.amazonaws.com/prod/gsx-challenge")
    return r.content

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
