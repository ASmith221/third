# Dependencies

from bs4 import BeautifulSoup as bs

import requests
import pymongo
from splinter import Browser

import tweepy

import time
import pandas as pd

All_Mars_Info={}

def Scraped_data():

        # Twitter API Keys
        consumer_key = "3REpngub1g5pFnxOrmFy7RA7u"
        consumer_secret = "B8Z6Qp4NsxDsEblyUwTqrQAd4CoCMAPkM9R8a81tGrOcy5fwwm"
        access_token = "338862045-4oYBBr7iESvJCw7u9KEhUxBFIdSmMGwi9sohBk5z"
        access_token_secret = "yQHd23XHo5iIrhFuVdJLq2aXgT4kHbV2BK7sNvz5X2fKc"
        api_key="24c85411d38cdd9b4b1601ca2a92276d"




# Setup Tweepy API Authentication
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())



#Browser Chromedriver

        executable_path = {"executable_path": "/Users/Adrienne/Downloads/chromedriver.exe"}
        browser = Browser("chrome", **executable_path, headless=False)


#set up URL
        news_url = "https://mars.nasa.gov/news/"
        browser.visit(news_url)
        #html = browser.html
        #soup = BeautifulSoup(html, "html.parser")


# Get info from Mars News URL
        url = "https://mars.nasa.gov/news/"
        response = requests.get(url)

        soup = bs(response.text, 'html.parser')

        news_title = soup.find('div', 'content_title', 'a').text

        news_p = soup.find('div', 'rollover_description_inner').text

        All_Mars_Info['news_title']=news_title
        All_Mars_Info['news_p']=news_p


        image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(image_url)
        html = browser.html
        soup = bs(html, "html.parser")


# Images from jpl.nasa.gov
        url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url2)
        browser.find_by_id('full_image').click()
        featured_image_url = browser.find_by_css('.fancybox-image').first['src']
        print(featured_image_url)


        image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(image_url)
        html = browser.html
        soup = bs(html, "html.parser")

        image = soup.find("img", class_="thumb")["src"]
        featured_image_url = "https://www.jpl.nasa.gov" + image
        print(featured_image_url)
        All_Mars_Info['featured_image_url']=featured_image_url


# Twitter API Keys
        #def get_file_contents(filename):
                       #try:
                        #with open(filename, 'r') as f:
                                #return f.read().strip()
                                #except FileNotFoundError:
                        #print("'%s' file not found" % filename)
        #return (get_file_contents)

        # Setup Tweepy API Authentication
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


        target_user = "MarsWxReport"
        tweet = api.user_timeline(target_user, count =1)
        mars_weather = ((tweet)[0]['text'])
        print(mars_weather)
        featured_image_url

        # dataframe
        facts_url = "https://space-facts.com/mars/"
        browser.visit(facts_url)
        mars_data = pd.read_html(facts_url)
        mars_data_db = pd.DataFrame(mars_data[0])
        mars_facts = mars_data.to_html(header = False, index = False)
        mars_facts
        All_Mars_Info['mars_facts']=mars_facts



        hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(hemispheres_url)
        html = browser.html
        soup = bs(html, "html.parser")
        mars_hemisphere = []

        products = soup.find("div", class_ = "result-list" )
        hemispheres = products.find_all("div", class_="item")

        for hemisphere in hemispheres:
                title = hemisphere.find("h3").text
                title = title.replace("Enhanced", "")
                end_link = hemisphere.find("a")["href"]
                image_link = "https://astrogeology.usgs.gov/" + end_link    
                browser.visit(image_link)
                html = browser.html
                soup=bs(html, "html.parser")
                downloads = soup.find("div", class_="downloads")
                image_url = downloads.find("a")["href"]
                mars_hemisphere.append({"title": title, "img_url": image_url})

                mars_hemisphere

                #All_Mars_Info['mars_hemisphere']=mars_hemisphere

        All_Mars_Info={
                "mars_hemisphere":mars_hemisphere,
                "mars_weather":mars_weather,
                "news_title":news_title,
                "featured_image_url":featured_image_url,
                "mars_data_db": mars_data_db
        }
        return All_Mars_Info

Scraped_data()


