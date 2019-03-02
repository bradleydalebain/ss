import youtube_dl
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from collections import OrderedDict
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess


proxies = {'http': 'http://192.168.43.1:8000'}
headers = {'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


proxy = "192.168.43.1:8000"

options = webdriver.ChromeOptions()
#options.add_argument('headless')

options.add_argument('--user-data-dir=/home/brad/.config/google-chrome')
options.add_argument('--proxy-server=%s' % proxy)
options.binary_location='/usr/bin/google-chrome'
url = 'https://openload-movies.tv/?s=%s'
query = input('Search Query: \n')
browser = webdriver.Chrome(chrome_options=options)
URL = url%query
browser.get(URL)
time.sleep(7.3)
od = OrderedDict()
titles = []

def download():
    win_han = browser.window_handles
    browser.switch_to_window(win_han[1])
    browser.find_element_by_class_name('fa-download').click()
    win_han.clear()
    

    
    download2()

def download2():
    time.sleep(20)
    win_han = browser.window_handles
    browser.switch_to_window(win_han[2])
    browser.find_element_by_id('makingdifferenttimer').click()
    win_han.clear()
    download3()


def download3():
    time.sleep(12)
    win_han = browser.window_handles
    browser.switch_to_window(win_han[3])
    browser.find_element_by_id('download').click()
    win_han.clear()
    download4()

    
def download4():
    ydl_opts = {'--proxy':'http://192.168.43.1:8000','--external-downloader':'aria2c','--external-downloader-args':'-x10'}
    time.sleep(11.4)
    win_han = browser.window_handles
    browser.switch_to_window(win_han[3])
    d = browser.find_element_by_class_name('button').get_attribute('href')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([d])
#retrieve titles from search page
for title_divs in browser.find_elements_by_class_name('title'):
    for links in title_divs.find_elements_by_tag_name('a'):
        titles.append(links.text)


#store titles in user friendle library

counter = 0
while counter < len(titles):
    od.update({counter:titles[counter]})
    counter += 1

for k,v in od.items():
    print(k,v)

selection = int(input('Enter the # corresponding to the correct movie: \n'))
for k,v in od.items():
    if selection == k:
        selected_title = v

follow = browser.find_element_by_link_text(selected_title)
follow.send_keys(Keys.CONTROL + Keys.RETURN)
download()
#browser.switch_to_window(win[1])
#time.sleep(17)
