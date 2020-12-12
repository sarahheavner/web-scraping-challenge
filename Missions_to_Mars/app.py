#import dependencies 
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


#initialize Flask
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route('/')
def index():
    mars_info = mongo.db.mars_info.find_one()
    return render_template('index.html', mars_info=mars_info)



# Route that will trigger the scrape function
@app.route('/scrape')
def scraper():

    mars_info = mongo.db.mars_info

    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mars_info.update({}, mars_data, upsert=True)

    #Redirect to home page
    return redirect("/", code=302)




if __name__ == "__main__":
    app.run(debug=True)