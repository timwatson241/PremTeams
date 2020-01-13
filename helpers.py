import time
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote

def grab_image(url, file_name):
    html = urlopen(url)
    soup = BeautifulSoup(html, features="lxml")
    # NEED TO REMOVE IMAGES OF GOALIES (COLLECT POSITION OR IGNORE WHEN GOALKEEPER)
    for res in soup.findAll('img', {'class': 'img'}):
        src = res.get('src')
        player_number = res.get('data-player')
    full = "https:" + src.replace('Photo-Missing',player_number)
    urllib.request.urlretrieve(full, "Images/"+file_name+".png")
    

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
    while True and i!=5:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        i+=1
    soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.close()
    return soup
