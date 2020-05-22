from flask import Flask, jsonify, request, render_template
#from flask_restful import Api, Resource
from candice import chat

app = Flask(__name__)


@app.route("/")
def home():
    # print("Hello World")
    return render_template("home2.html")

@app.route("/get")
def get_bot_response():
    print("We are here")
    userText = request.args.get('msg')
    print(userText)
    # print("Hello World")
    reply = chat(userText)
    return str(reply)
    # return "Kushal"

app.run(debug=True)
