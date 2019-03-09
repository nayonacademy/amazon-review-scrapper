import os
import csv
import time
import logging
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename='logfile.log',format='%(asctime)s - %(message)s', level=logging.INFO)

class ScrapBaseClass:
    def __init__(self,html,csv,url):
        self.html = html
        self.csv = csv
        self.url = url

        if not os.path.isdir(os.path.join(BASE_DIR,self.html)):
            os.system('mkdir '+self.html)
            logging.info("Successfully create '{}' file".format(self.html))

        if not os.path.isdir(os.path.join(BASE_DIR,self.csv)):
            os.system('mkdir '+self.csv)
            logging.info("Successfully create '{}' file".format(self.csv))
