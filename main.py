from helpers import*
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote


driver = webdriver.Chrome()
driver.get('https://www.premierleague.com/players')

soup = scroll(driver)

links=[]

for link in soup.findAll('a', {'class': 'playerName'}):
    try:
        links.append(link['href'])
    except KeyError:
        pass

print(links)
print(len(links))

number_images = 0
number_noimages=0

teams=[]

for link in links:
    updated_link = 'https:'+quote(link)
    try:
        grab_image(updated_link, str(number_images))
        number_images+=1
        club = get_club(updated_link)
        print(updated_link)
        print(club)
        teams.append(club)
    except: 
        print(print(updated_link))
        print('No Image/Club ' + str(number_noimages))
        number_noimages+=1
    

print(teams[10])
print(teams[100])
print(teams[200])

