import time
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import re
from google_images_download import google_images_download   #importing the library
import os
from selenium import webdriver
import time
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote
import pandas as pd
import os.path
import csv
import cv2

Teams = ["AFC Bournemouth", "Arsenal","Aston Villa","Brighton & Hove Albion","Burnley","Chelsea","Crystal Palace","Everton","Leicester City","Liverpool","Manchester City","Manchester United","Newcastle United","Norwich City","Sheffield United","Southampton","Tottenham Hotspur","Watford","West Ham United","Wolverhampton Wanderers"]

def grab_image(url, file_name):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="lxml")
    results = soup.body.find_all(string=re.compile('.*{0}.*'.format('Goalkeeper')), recursive=True)
    if len(results) != 0:
        return None
    else:
        for res in soup.findAll('img', {'class': 'img'}):
            src = res.get('src')
            player_number = res.get('data-player')
        full = "https:" + src.replace('Photo-Missing',player_number)
        urllib.request.urlretrieve(full, "Images/"+file_name+".png")
        return player_number

def get_club(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, features="lxml")
    club = None
    for res in soup.findAll("a",{'class': "playerbadgeContainer"}):
        href = res.get('href')
        club = href.split('/')[3]
        if club != None:
            return club

    if club == None:
        tables = soup.findChildren('table')
        my_table = tables[2]
        rows = my_table.findChildren('a')
        href = rows[0]['href']
        club = href.split('/')[3]
        return club

def scroll(driver):
    i=0
    while True and i!=7:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        i+=1
    soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.close()
    return soup

def scrape_from_google(number,team):
    os.mkdir("Images/"+team)
    response = google_images_download.googleimagesdownload()   #class instantiation
    arguments = {"keywords":team+" home jersey","limit":number,"print_urls":True,"output_directory":"Images", "image_directory":team}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)

def add_google_images(start_number,qty,Teams):
    for team in Teams:
        scrape_from_google(qty,team)
        directory = os.fsencode('Images/'+team)
        for file in os.listdir(directory):
             filename = os.fsdecode(file)
             os.rename('Images/'+team+'/'+filename,'Images/'+str(start_number)+'.png')
             with open('returns.csv','a') as fd:
                 writer = csv.writer(fd,lineterminator = '\n')
                 writer.writerow([start_number,team])
             start_number+=1

def resize(img):
    im = cv2.imread(img)
    im = cv2.resize(im,(500,500),interpolation=cv2.INTER_AREA)
    cv2.imwrite('1000'+img,im)
