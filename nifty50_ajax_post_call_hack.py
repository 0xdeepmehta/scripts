import requests
from bs4 import BeautifulSoup

_from = input("Enter From Date: ")
_to = input("Enter To Date: ")
url = "https://www.indiainfoline.com/\
live-market/company/ajax-get-historical-data"

def getData(_from, _to):
    page = requests.post(url, data={
        'periodFrom': _from,
        'periodTo': _to,
        'c_historicalId':'20559',
	'activeExchange': 'nse'
        })
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.prettify())
    else:
        print(page.status_code, "Fatal Error!")
getData(_from, _to)


"""
Useful Data: 
url: https://www.indiainfoline.com/live-market/company/ajax-get-historical-data

method: POST

parameters: .post(url, data={
	'periodFrom': '04-Oct-2019',
  	'periodTo': '04-November-2017',
 	'c_historicalld':'20559',
	'activeExchange': 'nse'
})
response-code: 200

content: {"HUGE"}
"""
