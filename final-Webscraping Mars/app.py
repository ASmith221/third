from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape
import os

from flask_pymongo import MongoClient



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"

mongo = PyMongo(app)

#conn='mongodb://localhost:27017'
#client = MongoClient(url)
#client=PyMongo.MongoClient(conn)
#db=client.mission_to_mars
#collection=db.mars()




@app.route('/')
def index():
	mission_to_mars = mongo.db.mission_to_mars.find_one()
	return render_template("index.html", mission_to_mars=mission_to_mars)

@app.route('/scrape')
def scrape():
	mission_to_mars = mongo.db.mission_to_mars
	mission_to_mars_data = scrape.scrape()
	mission_to_mars.update({}, mission_to_mars_data, upsert=True)
	return redirect("http://localhost:5000/",code=302)

if __name__ == "__main__":
	app.run(debug=True)