from selenium import webdriver
import pandas as pd
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
link = ''

try:
    ua = UserAgent()
    user_agent = ua.random
    print(user_agent)
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(link)

    # DO STUFF

    driver.close()
    driver.quit()
except Exception as e :
    print(f' Scriped ended due to {e}')