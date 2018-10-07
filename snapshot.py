import requests
import string

search_string = 'http://media.ethics.ga.gov/search/Campaign/Campaign_Namesearchresults.aspx?CommitteeName=&LastName={}&FirstName=&Method=0'
for char in string.ascii_lowercase:
    current_string = search_string.format(char)
    file_name = 'candidate_{}'.format(char)
    page = requests.get(search_string)
    with open('/home/jay/projects/python_projects/campaign_finance_scraper/samples/{}'.format(file_name), 'w') as f:
        f.write(page.text)
        f.close()

    
