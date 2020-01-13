from helpers import*
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote


url = 'https://www.premierleague.com/players/13286/Tammy-Abraham/overview'


grab_image(url, 'file_name')

