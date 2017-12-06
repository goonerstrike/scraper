import urllib2
from bs4 import BeautifulSoup

downloads = "http://downloads.ocp.sd.spawar.navy.mil"
page = urllib2.urlopen(downloads)
soup = BeautifulSoup(page)
print soup.prettify()
print soup.title
