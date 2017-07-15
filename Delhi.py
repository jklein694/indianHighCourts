from bs4 import BeautifulSoup
import requests
import pandas as pd


count = range(1000)
page_num = count[::8]

page_c1 = []
page_c2 = []
page_c3 = []

c1 = soup.find_all('span', class_="pull-left width-33 title al")
c2 = soup.find_all('span', class_="pull-left width-30 title al")
c3 = soup.find_all('span', class_="pull-left width-30 title al last")
for i in page_num:
    html= "http://delhihighcourt.nic.in/dhc_case_status_list_new.asp?ayear=&pyear=&SNo=1&SRecNo={}&dno=&dyear=&ctype=ALL&cno=&cyear=1980&party=&adv=".format(i)
    x = requests.get(html)
    soup = BeautifulSoup(x.text)
    for n in c1:
        page_c1.append(n.text)
    for n in c2:
        page_c2.append(n.text)
    for n in c3:
        page_c3.append(n.text)


# Initialize pandas DataFrame
data = pd.DataFrame()

data['1'] = page_c1
data['2'] = page_c2
data['3'] = page_c3

def reduce_space(data):
    data = map(lambda x: x.replace(' ', ''), data)
    data = map(lambda x: x.replace('\r', ''), data)
    data = map(lambda x: x.replace('\n', ''), data)
    data = map(lambda x: x.replace('\t', ''), data)
    return data

data['1'] = reduce_space(data['1'])
data['2'] = reduce_space(data['2'])
data['3'] = reduce_space(data['3'])

new_header = data.iloc[0]
data = data[1:]
data.columns = new_header

print data

data.to_excel('Delhi.xls')

'''
url = "http://delhihighcourt.nic.in/dhc_case_status_list_new.asp?ayear=&pyear=&SNo=1&SRecNo=0&dno=&dyear=&ctype=ALL&cno=&cyear=1980&party=&adv="
r = requests.get(url)
soup = BeautifulSoup(r.text)

foo = []
for i in range(100):
    foo.append(i)

print foo[::7]


print soup.prettify()

g_data = []

for i in soup.find_all('span', class_="pull-left width-33 title al"):
    for n in i.text:
        data = map[lambda x: x.replace('t/', ''), i.text]
        g_data.append(i.text)
print g_data




for i in range(1, 11):
    html= '"http://delhihighcourt.nic.in/dhc_case_status_list_new.asp?ayear=&pyear=&SNo=1&SRecNo={}&dno=&dyear=&ctype=ALL&cno=&cyear=1980&party=&adv='.format(i)
    x = requests.get(html)
    people.append(x.json())


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

'''
