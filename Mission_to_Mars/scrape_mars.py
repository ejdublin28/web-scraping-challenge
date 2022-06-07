#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


##Top Mars News

#Creating Dictionary Value Outside of Definition
nasa_mars_news = {}

def scrape_info():
    #Setting up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Giving Website URLs
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    #Scraping using Beautiful Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # test = soup.find_all('content_title').text
    # test = {}
    nasa_mars_news['title'] = soup.find(class_="content_title").text
    nasa_mars_news['text'] = soup.find(class_="article_teaser_body").text
    # test['b'] = soup.find("p",class_="content_title").get_text()

    browser.quit()

    return nasa_mars_news


scrape_info()

nasa_mars_news['title']


##Mars Space Images

#Creating Dictionary Value Outside of Definition
mars_images = {}
relative_image_path = []

def scrape_images():
    #Setting up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Giving Website URL
    # Example:
    image_url = 'https://spaceimages-mars.com/'
    browser.visit(image_url)

    time.sleep(1)

    #Scraping using Beautiful Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Getting image filepath for headerimage
    relative_image_path = soup.find('img',class_='headerimage fade-in')["src"]
    mars_images.update({'image': image_url + relative_image_path})

    browser.quit()

    return mars_images

scrape_images()


relative_image_path


##Mars Facts

#Creating Dictionary Value Outside of Definition
mars_facts = {}
earth_facts = {}
tbl_headers = []
tbl_details = []


def scrape_facts():
    #Setting up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Giving Website URL
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)

    time.sleep(1)

    #Scraping using Beautiful Soup
    html = browser.html
    soup = bs(html, "html.parser")

    facts_tbl = soup.find('table',class_="table")
    facts_tbl

    for i in facts_tbl.find_all('th'):
        row_label = i.text
        tbl_headers.append(row_label)
    
    for i in facts_tbl.find_all('td'):
        row_details = i.text
        tbl_details.append(row_details)

    for i in range(0,len(tbl_headers)):
        mars_facts.update({tbl_headers[i]:tbl_details[2*i]})
        earth_facts.update({tbl_headers[i]:tbl_details[(2*i)+1]})
    #nasa_mars_news['text'] = soup.find(class_="article_teaser_body").text
    # test['b'] = soup.find("p",class_="content_title").get_text()
    
    browser.quit()

    return mars_facts, earth_facts


scrape_facts()


##Hemisphere Images

#Creating Dictionary With Titles and Images

hem_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
]
