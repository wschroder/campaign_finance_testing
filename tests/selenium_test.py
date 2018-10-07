from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium uses Firefox to fetch the webpage. Have to install geckodriver in order to use or will throw error.
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
driver.get('http://media.ethics.ga.gov/search/Campaign/Campaign_Namesearchresults.aspx?CommitteeName=&LastName=a&FirstName=&Method=0')

link = 'ctl00_ContentPlaceHolder1_Search_List_ctl05_lnkViewID'

# This clicks the button attached to the javascript doPostBack function 
click = driver.find_element_by_id(link).click()
# This fetches the div that contains the table with the candidate name, filer id, office sought,
# candidate information link, and status
try: 
    result = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_UpdatePanel1')))
except Exception as e:
    print(e)

# This iterates through the div, selecting all td elements and printing their text
for element in result.find_elements_by_tag_name('td'):
    print(element.text)
driver.quit()
