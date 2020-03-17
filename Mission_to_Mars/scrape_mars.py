from bs4 import BeautifulSoup  
from splinter import Browser
import pandas as pd
import requests


def openWebpage():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

mars_data={}


def scrape():


	#title, paragraph
	#news_url='https://mars.nasa.gov/news/'
	#browser.visit(news_url)
	#html=browser.html
	#soup=BeautifulSoup(html, 'lxml')

  url = 'https://mars.nasa.gov/news/'
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'lxml')	
  element = soup.find('div', class_="content_title") 
  news_title = element.text.strip() 
  element = soup.find('div', class_="rollover_description_inner")
  news_paragraph = element.text.strip()
  mars_data["News_Title"] = news_title
  mars_data["News_Text"] = news_paragraph
	#image
  browser = openWebpage()
  url_futured="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
  browser.visit(url_futured)	
  button=browser.find_by_id("full_image")
  button.click()
  html=browser.html
  soup=BeautifulSoup(html, 'lxml')
  img = soup.find('img', class_="fancybox-image")
  featured_image_url = imgUrl + img['src']
  mars_data["image"]=featured_image_url
  browser.quit
	

	#weather
  browser = openWebpage()
  browser.visit("https://twitter.com/marswxreport?lang=en")
  time.sleep(1)
  html = requests.get("https://twitter.com/marswxreport?lang=en").text
  soup = BeautifulSoup(html, 'lxml')
  try:
        tweet = soup.find_all('div', class_="js-tweet-text-container")
        i = 0
        for tweets in tweet:
            if "InSight" in tweet[i].text:
                tweetText = tweet[i].text.split("pic")[0]
                break
            i += 1
        mars_data["Weather"] = tweetText
  except:
        mars_data["Weather"] = "Not found"
  browser.quit

    #table

  url_facts='https://space-facts.com/mars/'
  browser.visit(url_facts)
  facts_html=pd.read_html(url_facts)
  facts_html=facts_html[0]
  facts_html.columns=['Description','value']
  facts_html.set_index('Description', inplace=True)
  mars_table=facts_html.to_html(index=true, header=True)
  mars_data["table"]=mars_table





  url_hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
  browser = openWebpage()
  browser.visit(url_hemi)
  html = browser.html
  soup = BeautifulSoup(html_hemi, 'lxml')
  items = soup.find_all('div', class_='item')
  hemi_image_urls = []
  hemi_main_url = 'https://astrogeology.usgs.gov'



  for i in items:


   		title = i.find('h3').text
   		partial_img_url = i.find('a', class_='itemLink product-item')['href']
   		browser.visit(hemi_main_url + partial_img_url)
   		partial_img_html = browser.html
    
     
   		soup = BeautifulSoup( partial_img_html, 'lxml')
   		img_url = hemi_main_url + soup.find('img', class_='wide-image')['src']
   		hemi_image_urls.append({"title" : title, "img_url" : img_url})
   		Hemisphere={"title":title,"img url":hemi_image_urls}
   		browser.back()

  mars_data['hemisphere']=Hemisphere
    

  return mars_data






if __name__ == "__main__":
    print(scrape_all())










