#Demo on how to read and parse a webpage
import urllib.request

page = urllib.request.urlopen("https://www.hodsonbayhotel.com/")
text = page.read().decode("utf8")
print(text)