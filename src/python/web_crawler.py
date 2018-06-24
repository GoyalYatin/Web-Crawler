from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Main_Page"
conn = urlopen(url)
pageData = conn.read()
conn.close()

try:
    bs = BeautifulSoup(pageData, "lxml")
except:
    bs = BeautifulSoup(pageData, "html5lib")

headers = "Title, Link, Value\n"
filename = "scrapped.csv"
f = open(filename, "w")
f.write(headers)

# print(bs.h1)
# print(bs.find("h1", {"id": "firstHeading"}).string)
# print(bs.find("h1", {"id": "firstHeading"}).text)

bodyContent = bs.find("div", {"id": "bodyContent"})
links = bodyContent.findAll("a", href=re.compile("(/wiki/)+([A-Za-z0-9_:()])"))

for link in links:
    # print(link.get('title'), link.get('href'), link.text)
    try:
        f.write(link.get('title') + "," + link.get('href') + "," + link.text + "\n")
    except TypeError:
        continue
    except UnicodeEncodeError:
        continue

f.close()
