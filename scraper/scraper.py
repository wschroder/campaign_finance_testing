import requests
from root_url import Url
import driver_config
from driver_config import driver 

class Scraper():


    base_string = 'http://media.ethics.ga.gov/search/Campaign/Campaign_Namesearchresults.aspx?CommitteeName=&LastName={}&FirstName=&Method=0'

    def __init__(self, sur_letter):
        self.fetch_url = base_string.format(sur_letter)
    
    def build_urls(self):
        driver.get(fetch_url)
        

    def scrape(self):
        pass
                
