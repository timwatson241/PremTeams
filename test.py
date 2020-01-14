from helpers import*
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote
import pandas as pd
import os.path
import os
import csv
import cv2

df = pd.read_csv("returns.csv")

for i in range(2000):
    if os.path.isfile('Images/'+str(i)+'.png'):
        print ("File "+str(i)+'.png '+'exists')
    else:
        print ("File "+str(i)+'.png '+' does not exist')
        df = df[df.id != i]

df.to_csv(r'returns2.csv',index=False)

directory = os.fsencode('Images/')
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     print(filename)
     resize('Images/'+filename)
