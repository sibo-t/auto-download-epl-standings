
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import os
import sys
import random


# Create options object for headless mode
chrome_options = Options()

if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
    # Set the default download directory to the root folder
    prefs = {'download.default_directory' : sys.argv[1]}
    chrome_options.add_experimental_option('prefs', prefs)

chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.rotowire.com/soccer/league-table.php")
time.sleep(random.randint(5,10))

# Hover over button
button = driver.find_element(By.XPATH, '//*[@id="standings"]/div[2]/div[2]/button[2]')

ActionChains(driver)\
    .move_to_element(button)\
    .perform()

time.sleep(random.randint(5,10))

ActionChains(driver)\
    .click()\
    .perform()

time.sleep(random.randint(5,10))


driver.quit()
