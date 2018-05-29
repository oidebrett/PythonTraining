from urllib.request import urlopen
from xml.dom import minidom
import collections

# extract the headlines from the feed
def extractString(doc):
   str = ""
   for node in doc.getElementsByTagName('channel'):
      for title in node.getElementsByTagName('title'):
         str = str + title.firstChild.data + "\n"
   return str

# extract the feed from the url
def getRSSString(url):
    results = []
    rssString = ""
    results.append(minidom.parse(urlopen(url)))
    for webDoc in results:
        rssString = rssString + extractString(webDoc)
    return rssString



# START HERE ...
feedFile = open ("./Section 3 - Strings/feeds.txt","r")
feedURL = feedFile.readline()
feed = getRSSString(feedURL)



# Read the RSS feed from the URL provided
#feed = getRSSString("https://www.apple.com/main/rss/hotnews/hotnews.rss")

# Display the results
print(feed.capitalize())
print(feed.upper())
print(feed.lower())

feed = feed.lower()
vowelCount = 0
vowelCount = vowelCount + feed.count('a')
vowelCount = vowelCount + feed.count('e')
vowelCount = vowelCount + feed.count('i')
vowelCount = vowelCount + feed.count('o')
vowelCount = vowelCount + feed.count('u')

print("vowel count= ", vowelCount)


#print(feed.replace("Garda","cop"))

# Display the number of lines
#print("There are %d lines in this feed" %feed.count("\n"))

words = feed.split()
print(collections.Counter(words).most_common(5))

feedFile.close()