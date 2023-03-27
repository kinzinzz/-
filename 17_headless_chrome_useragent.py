from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=")