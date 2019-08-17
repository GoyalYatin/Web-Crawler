from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Main_Page"
conn = urlopen(url)
pageData = conn.read()
conn.close()

print(type(pageData))

try:
    bs = BeautifulSoup(pageData, "lxml")
except:
    bs = BeautifulSoup(pageData, "html5lib")

print(type(bs))
print(bs.title)
print(bs.h1)
print(bs.find("h1", {"id": "firstHeading"}).string)
print(bs.find("div", {"id": "siteSub"}).text)

# tag and its name
tag = bs.h1
print(tag)
print(type(tag))
print(tag.name)
print("==============================")

# attributes of tag
print(tag.attrs)
print(tag['class'])
print(tag.get('id'))

##We can add, remove, and modify a tag’s name and attributes

# modifying tag type
tag.name = "div"

print(tag)
print(tag.name)
print("==============================")

print(tag.attrs)
print("==============================")

# modifying a attribute
tag['id'] = 'yatin'
print(tag.attrs)
print("==============================")

# adding a new attribute
tag['xyz'] = 'abc'
print(tag.attrs)
print("==============================")

# deleting an attribute
del tag['xyz']
print(tag.attrs)
print("==============================")


#Fetching multiple links and putting in csv

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

# Converting the HTML to readable and structured format
print(bs.prettify())