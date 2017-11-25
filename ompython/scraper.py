from bs4 import BeautifulSoup
import requests

url = "https://trading.scottrade.com/home/default.aspx"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all('hpc-numeric hpc-positive')

for link in links:
	print(link.text)
	print(link['hpc-table-row hpc-even'])