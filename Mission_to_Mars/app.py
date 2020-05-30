# Dependencies and Setup
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri = "mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    latest_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", data = latest_data)

# Route to import scrape_mars.py
@app.route("/scrape")
def scrape():

    # Call scrape
    mars_data = scrape_mars.scrape()
    mongo.db.collection.update({}, mars_data, upsert = True)
    return redirect("/")

# Run
if __name__ == "__main__":
    app.run(debug = True)