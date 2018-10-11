from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options 
import os
import time


chrome_options = Options()
download_dir = '/home/jay/projects/python_projects/campaign_finance_scraper/out'
prefs = {'download.default_directory': download_dir,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': False,
        'safebrowsing.disable_download_protection': True}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
command_result = driver.execute("send_command", params)
driver.get('http://media.ethics.ga.gov/Search/Campaign/Campaign_ByContributions_RFR.aspx?NameID=27792&FilerID=C2017001358&CDRID=130153&Name=Abbott,%20David%20&Year=2017&Report=Final%20Report%20and%20Termination%20Statement')
selector = 'ctl00_ContentPlaceHolder1_Campaign_ByContributions_RFResults2_Export'
try:
    result = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.ID, selector)))
    click = driver.find_element_by_id(selector).click()
    while not os.path.exists('{}/StateEthicsReport.csv'.format(download_dir)):
        time.sleep(1)
    if os.path.isfile('{}/StateEthicsReport.csv'.format(download_dir)):
        f = open('{}/StateEthicsReport.csv'.format(download_dir))
        print(f.name)
        print(f.read())
except Exception as e:
    print(e)

