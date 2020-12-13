Web Scraping Homework - Mission to Mars
    Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

#Section 1: Scraping
    ##Complete initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

    ##NASA Mars News 
        ###Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text

    ##JPL Mars Space Images - Featured Image
        ###Use splinter to navigate the site and find the image url for the current Featured Mars Image.

    ##Mars Facts
        ###Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
        ###Use Pandas to convert the data to a HTML table string.

    ##Mars Hemispheres
        ###Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.

#Section 2: MongoDB and Flask Application
    ##Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
        
    ##app.py
        ###Use VSC to import flask(Flask, render_template, redirect), flask_pymongo(Pymongo), and scrape_mars to create web application that connects to mongoDB where data from scrape_mars is stored.

    ##scrape_mars   
        ###Use code created in Jupyter Notebook to scrape websites above. Use dictionary to store data in mongoDB that will be updated when scrape function is called.

    ##index.html 
        ###Format web application using HTML. Using bootstrap, add jumbotron with button that will scrape new information from the URLs. Add all elements from scrape_mars/mongoDB and add HTML formatting to achieve desired visual outcome on web application. 




