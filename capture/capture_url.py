import urllib
import urllib2
from bs4 import BeautifulSoup
localDir = "/home/typ/item/"

def getContent(url):

    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    return content

#def getImage(info):
#    soup = BeautifulSoup(info, "html.parser")
#    imgAll = soup.find_all('img', class_="BDE_Image")
#    print imgAll
#    x=1
#    for img in imgAll:
#        url_img = img['src']
#        print localDir + '%s.jpg' %x
#        # urllib.urlretrieve()
#        urllib.urlretrieve(url_img, localDir + '%s.jpg' % (x))
#        x=x+1

if __name__ == '__main__':

	url = 'http://open.aispeech.com/doc/wiki/doc_aiengine_native'
	info=getContent(url)
	print info
# print info
#	print getImage(info)
