from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
# import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    news = mongo.db.news.find_one()
    images = mongo.db.images.find_one()
    facts = mongo.db.facts.find_one()
    hems_1 = mongo.db.hems_1.find_one()
    hems_2 = mongo.db.hems_2.find_one()
    hems_3 = mongo.db.hems_3.find_one()
    hems_4 = mongo.db.hems_4.find_one()
    
    # Return template and data
    return render_template("index.html", news=news, images=images, facts=facts, hems_1=hems_1, hems_2=hems_2, hems_3=hems_3, hems_4=hems_4)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    
    mars = mongo.db

    # Run the scrape function to get LATEST MARS NEWS
    nasa_mars_news = scrape_mars.scrape_info()
    mars.news.update({}, nasa_mars_news, upsert=True)

    # Run the scrape function to get MARS IMAGES
    mars_images = scrape_mars.scrape_images()
    mongo.db.images.update({}, mars_images, upsert=True)
    
    # Run the scrape function to get MARS FACTS
    mars_facts = scrape_mars.scrape_facts()
    mars.facts.update({}, mars_facts, upsert=True)

    # Run the scrape function to get MARS HEMISPHERE IMAGES
    mars_hems = scrape_mars.hem_urls
    
    mars.hems_1.update({},mars_hems[0], upsert=True)
    mars.hems_2.update({},mars_hems[1], upsert=True)
    mars.hems_3.update({},mars_hems[2], upsert=True)
    mars.hems_4.update({},mars_hems[3], upsert=True)
    # for i in range(0,3):
    #     mars.hems_[i].update({},mars_hems[i], upsert=True)

    # mars.hems.insert_one({},mars_hems[0], upsert=True)
    # mars.hems.insert_one({},mars_hems[1], upsert=True)
    # mars.hems.insert({},mars_hems[2], upsert=True)
    # mars.hems.insert_one({},mars_hems[3], upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)