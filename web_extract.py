import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import shutil
import chromedriver_autoinstaller # pip install chromedriver-autoinstaller

chromedriver_autoinstaller.install() # To update your chromedriver automatically



download_dir = 'output/download_pdf'

preferences = {
                "profile.default_content_settings.popups": 0,
                "download.default_directory": os.getcwd() + os.path.sep + download_dir + os.path.sep,
                "directory_upgrade": True,
                # "download.default_directory": "C:/Users/XXXX/Desktop", #Change default directory for downloads
                "download.prompt_for_download": False, #To auto download the file
                "download.directory_upgrade": True,
                "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
            }

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', preferences)

# driver = webdriver.Chrome(executable_path='driver/chromedriver', options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

base_url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/'
pmc_id = 'PMC1507461'
pmid = '6797614'

driver.get("{}/{}".format(base_url, pmc_id))
timeout = 5
try:
    publication_type = 'pmc-sidebar__formats'
    pub_type_element_present = EC.presence_of_element_located((By.CLASS_NAME, publication_type))
    WebDriverWait(driver, timeout).until(pub_type_element_present)
    # element_present = EC.presence_of_element_located((By.ID, 'article-details'))
    # WebDriverWait(driver, timeout).until(element_present)
    print('element 1 found, done')


    publication_type = 'int-view'
    pub_type_element_present = EC.presence_of_element_located((By.CLASS_NAME, publication_type))
    WebDriverWait(driver, timeout).until(pub_type_element_present)
    element = driver.find_element(By.PARTIAL_LINK_TEXT, 'PDF')
    value = element.get_attribute('href')
    print('element 2 found, done')
    print(f'get value {value}')

    driver.get(value)
    time.sleep(3)

    file_name = os.path.basename(value)
    file_path = os.path.join(download_dir, file_name)
    if file_name.endswith('.tar.gz'):
        os.rename(file_path, os.path.join(download_dir, pmid + '.tar.gz'))
    elif file_name.endswith('.pdf'):
        os.rename(file_path, os.path.join(download_dir, pmid + '.pdf'))
    else:
        raise ValueError('An unknown file type!')




except TimeoutException:
    print("Timed out waiting for page to load")