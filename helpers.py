import time
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import re

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
