import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


# Create instance of Flask
app = Flask(__name__)


# Tester function
@app.route("/")
def hello():
    return "Hello World!"


# Set how & where to run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)     # change to debug=False when in production mode
