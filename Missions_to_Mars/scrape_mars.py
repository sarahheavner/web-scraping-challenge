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

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    titles = soup.find_all(name='div', class_='content_title')
    title_list = [t.text for t in titles]
    news_title = title_list[1]

    paragraphs = soup.find_all(name='div', class_='article_teaser_body')
    paragraph_list = [p.text for p in paragraphs]
    news_p = paragraph_list[0]


    mars_info['news_title'] = news_title
    mars_info['news_p'] = news_p

    return mars_info