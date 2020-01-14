from helpers import*
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote
from googleimagescraper import*
import pandas as pd
import os.path

df = pd.read_csv("returns.csv")

for i in range(1000):
    if os.path.isfile('Images/'+str(i)+'.png'):
        print ("File "+str(i)+'.png '+'exists')
    else:
        print ("File "+str(i)+'.png '+' does not exist')
        df = df[df.id != i]
