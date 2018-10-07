from lxml import html 

with open('/home/jay/projects/python_projects/campaign_finance_scraper/samples/test_profile.html') as f:
    page = f.read()
    tree = html.fromstring(page)
    res = tree.xpath(".//a[@class='lblentrylink']")
    for item in res:
        print(item.get('id'))
    f.close()
