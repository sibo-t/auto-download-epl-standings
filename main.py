
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

def download_csv():
    """Opens the page to download the latest EPL standings

    Args:
        n (int): Try to look for n amount of unique tweets
        look_up (str): Topic of the tweets
    """

    # Create options object for headless mode
    chrome_options = Options()
    
    # Set the default download directory to the root folder
    prefs = {'download.default_directory' : '/home/sibo-t/work/auto-download-epl-standings'}
    chrome_options.add_experimental_option('prefs', prefs)

    # Disable the download dialog
    # chrome_options.add_experimental_option("prefs", {"download.prompt_for_download": False})
    # chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.rotowire.com/soccer/league-table.php")
    time.sleep(10)

    # Hover over button
    button = driver.find_element(By.XPATH, '//*[@id="standings"]/div[2]/div[2]/button[2]')

    ActionChains(driver)\
        .move_to_element(button)\
        .perform()

    time.sleep(10)

    ActionChains(driver)\
        .click()\
        .perform()

    time.sleep(10)


    driver.quit()

if __name__ == '__main__':
    download_csv()