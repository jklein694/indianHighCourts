# creating a table to store data in right format
# get requests
# writing a for loop to increase SRecNo=0 by 8 ever search 0,8,16,24
import requests
from bs4 import BeautifulSoup

url = "http://delhihighcourt.nic.in/dhc_case_status_list_new.asp?ayear=&pyear=&SNo=1&SRecNo=0&dno=&dyear=&ctype=ALL&cno=&cyear=1980&party=&adv="
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

g_data = soup.find_all("ul", {"class": "clearfix grid"})
oddLists = soup.find("li", {"class": "clearfix odd"})
evenLists = soup.find("li", {"class": "clearfix even"})

# print (g_data)

# How do I loop through odd, even, odd, even, instead of all odds then all evens
# how to get text from a find_all
for item in g_data:
    # print (oddLists)
    # print (evenLists.text)

# print (oddLists.text)
# print (evenLists.text)
    print ("This is line 1 info: {}This is line 2 info: {}".format(oddLists.text, evenLists.text))
    #
    # print (oddLists)
    # print (evenLists)