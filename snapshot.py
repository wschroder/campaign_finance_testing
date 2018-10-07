import requests

page = requests.get('http://media.ethics.ga.gov/search/Campaign/Campaign_Namesearchresults.aspx?CommitteeName=&LastName=a&FirstName=&Method=0')

with open('/home/jay/projects/python_projects/campaign_finance_scraper/samples/test_profile.html', 'w') as f:
    f.write(page.text)
    f.close()

    
