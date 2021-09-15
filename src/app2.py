import json
from flask import Flask, request

app = Flask(__name__)
@app.route("/",methods=["POST"])
def home():
    json.dump(request.json, open("input.json", "w"),indent=4,sort_keys=True)
    return "Hi from Flask"

app.run(port=1234)