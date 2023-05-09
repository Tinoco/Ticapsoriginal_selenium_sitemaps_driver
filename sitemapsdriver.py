# TIME TO AWAITING REFRESHS
import time

# SELENIUM LIBRARY TO ENABLE DRIVER MODE
from selenium import webdriver

# TQDM PROGRESS BAR
from tqdm import tqdm

# IDENTIFY LARGE XML FILE
import advertools as adv

# INDEXING YOUR LARGE SITEMAPS
sitemap = adv.sitemap_to_df("https://ticapsoriginal.com/static/sitemaps2.xml")

# TYPE CASTING URL TO LIST
urls = sitemap["loc"].to_list()

browser = webdriver.Chrome()

# WALK ON ALL URLS
for item in tqdm(urls):
    browser.get(item)
    time.sleep(40)
