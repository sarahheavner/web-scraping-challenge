#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


#initialize browser
def init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_info = {}

    #Direct browser to Mars News website
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    #Scrape page into soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Find most recent news title and store in variable
    titles = soup.find_all(name='div', class_='content_title')
    title_list = [t.text for t in titles]
    news_title = title_list[1]

    #Find most recent news paragraph teaser and store into variable
    paragraphs = soup.find_all(name='div', class_='article_teaser_body')
    paragraph_list = [p.text for p in paragraphs]
    news_p = paragraph_list[0]

    #Add title and paragraph variables into dictionary
    mars_info['news_title'] = news_title
    mars_info['news_p'] = news_p

    #Direct browser to JPL Mars Space Images - Featured Image
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    #Click through full image and more info buttons to get to fullsize image
    browser.links.find_by_partial_text('FULL IMAGE').click()
    browser.links.find_by_partial_text('more info').click()

    #Create a BeautifulSoup object
    jpl_html = browser.html
    soup = bs(jpl_html, 'html.parser')

    #Find image URL
    image_url = soup.find_all(name='figure', class_='lede')
    image_url = image_url[0].a['href']

    #Create full URL
    featured_image_url = 'https://www.jpl.nasa.gov' + image_url

    #Add image URL into dictionary
    mars_info['featured_image'] = featured_image_url

    #Exit browser after completing scrape
    browser.quit()

    #Return results
    return mars_info

