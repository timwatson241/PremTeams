from helpers import*
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote
import csv

Teams = ["AFC Bournemouth", "Arsenal","Aston Villa","Brighton & Hove Albion","Burnley","Chelsea","Crystal Palace","Everton","Leicester City","Liverpool","Manchester City","Manchester United","Newcastle United","Norwich City","Sheffield United","Southampton","Tottenham Hotspur","Watford","West Ham United","Wolverhampton Wanderers"]

driver = webdriver.Chrome()
driver.get('https://www.premierleague.com/players')

soup = scroll(driver)

links=[]

for link in soup.findAll('a', {'class': 'playerName'}):
    try:
        links.append(link['href'])
    except KeyError:
        pass

print(len(links))

number_images = 0


teams=[]


for link in links:
    updated_link = 'https:'+quote(link)
    try:
        #GRAB IMAGE BUT ONLY IF NOT A GOALIE
        player_number = grab_image(updated_link, str(number_images))
        if player_number != None:
            #IF NOT A GOALIE, GET THE CLUB AND ADD IT TO THE LIST
            club = get_club(updated_link)
            teams.append([number_images , club])
            number_images+=1
            print(number_images)

    except: pass

with open('returns.csv', 'w') as f:
    writer = csv.writer(f,lineterminator = '\n')
    writer.writerow(['id','team'])
    for val in teams:
        writer.writerow([val[0],val[1]])

#print(teams[10])
#print(teams[100])
#print(teams[200])
