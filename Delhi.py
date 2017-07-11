import requests
from bs4 import BeautifulSoup

url = "http://delhihighcourt.nic.in/dhc_case_status_list_new.asp?SNo=1&SRecNo=0&ctype=ALL&cyear=2017"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

g_data = soup.find("ul", {"class": "clearfix grid"}).text


print g_data