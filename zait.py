import requests # to use http protocols
from bs4 import BeautifulSoup # to parse the html code
import json
import re
# identify the url
url ='https://www.thriftbooks.com/browse/?12529col#b.s=mostPopular-desc&b.p=1&b.pp=50&b.col&b.f.t%5B%5D=12529&b.list'
# parsing the content of the html
content = requests.get(url).content
soup = BeautifulSoup(content, 'html.parser')
data= soup.find_all('script')
data_string = data[12].string
data = {}

match = re.search(r'window.searchStoreV2\s*=\s*(\{.*?\});', data_string, re.DOTALL)
# print(match.group(1))

if match:
    works = match.group(1)
    works_json = json.loads(works)
    works = works_json.get("works")
print(works)

with open (r'thrift_books_data.csv','w') as f:
    f.write(f'title,condition,buy_price\n')

for i in works:
    data.update(i)
    title = data['title']
    condition = data['buyNowCondition']
    buy_price = data['buyNowPrice']

    with open(r'thrift_books_data.csv','a') as f:
        f.write(f'{title},{condition},{buy_price}\n')
    
