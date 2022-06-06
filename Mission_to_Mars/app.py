from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
# import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# setup mongo connection
# conn = "mongodb://localhost:27017/mars"
# client = pymongo.MongoClient(conn)

# connect to mongo db and collection
# db = client["mars"]
# collection = db["mars_info"]

# test_insert = {"test":"Inserting test line to create database and collection for mars info"}
# x = collection.update_many({},test_insert, upsert=True)
# x = collection.insert_one(test_insert)

# print(scrape_mars.nasa_mars_news)
# Run the scrape function to get LATEST MARS NEWS
# nasa_mars_news = scrape_mars.scrape_info()
# Update the Mongo database using update and upsert=True
# collection.update({}, nasa_mars_news, upsert=True)
# produce = db.produce

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars=mars)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    
    # Run the scrape function to get LATEST MARS NEWS
    mars = mongo.db.mars
    nasa_mars_news = scrape_mars.scrape_info()
    mars.update({}, nasa_mars_news, upsert=True)
    # print(nasa_mars_news)
    # Update the Mongo database using update and upsert=True
    # mongo.db.collection.update({}, nasa_mars_news, upsert=True)

    # # Run the scrape function to get MARS IMAGES
    # mars_images = scrape_mars.scrape_images()

    # # Update the Mongo database using update and upsert=True
    # mongo.db.collection.update({}, mars_images, upsert=True)
    
    # # Run the scrape function to get MARS FACTS
    # mars_facts = scrape_mars.scrape_facts()

    # # Update the Mongo database using update and upsert=True
    # mongo.db.collection.update({}, mars_facts, upsert=True)

    # Redirect back to home page
    # return redirect("/")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)