import os
import csv
from bs4 import BeautifulSoup
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
html_location = os.path.join(BASE_DIR, 'html')

file_list = os.listdir(html_location)

with open(os.path.join(BASE_DIR,'csv/review.csv'),'w',newline="") as csvfile:
    fieldname = ["Date","Rating","Review"]
    write = csv.DictWriter(csvfile,fieldnames=fieldname)
    write.writeheader()
    for file in file_list:
        filename = os.path.join(html_location,file)
        f = open(filename,'r')
        soup = BeautifulSoup(f.read(), 'html.parser')

        for divs in soup.findAll('div', attrs={'class': 'a-section review'}):
            review_date = divs.find("span", {"class": "a-size-base a-color-secondary review-date"}).text.strip()
            rating = divs.find("span", {"class": "a-icon-alt"}).text
            review_text = divs.find("span", {"class": "a-size-base review-text"}).text
            write.writerow({'Date':review_date,'Rating':rating,'Review':review_text})
