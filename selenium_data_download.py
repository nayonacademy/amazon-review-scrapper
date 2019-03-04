from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
html_location = os.path.join(BASE_DIR, 'html')

for i in range(20,22):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = f"https://www.amazon.com/E12SV-Single-Carpeted-Subwoofer-Enclosure/product-reviews/B0013N0UEE/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={i}"
    print(url)
    driver.get(url)
    file_path = os.path.join(html_location,str(i)+".html")
    with open(file_path, "w") as f:
        f.write(driver.page_source)
    time.sleep(5)
    driver.close()
