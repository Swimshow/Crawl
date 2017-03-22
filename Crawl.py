import requests
from bs4 import BeautifulSoup

lazy= "http://www.kijiji.ca"







def spider(maxNumPages):
    page =1
    fw = open('KijijiGuitarStuff.txt','w')
    while page < maxNumPages:
            url = "http://www.kijiji.ca/b-grand-montreal/guitar/"
            extra = "k0l80002"

            #special condition where we dont concat anything
            if page==1:
                realurl = url+extra
            else:
                realurl = url +"page-"+str(page)+"/"+extra

            source_code = requests.get(realurl)
            plaintxt = source_code.text
            soup = BeautifulSoup(plaintxt)
            for link in soup.findAll('a',{'class':'title enable-search-navigation-flag '}):
                title = link.string
                #print(title)

                href = link.get('href')
                itemurl = lazy+href
                itemPriceInfo(itemurl)

            page=page+1


def itemPriceInfo(specificPageURL):
    source_code = requests.get(specificPageURL)
    plaintxt = source_code.text
    soup = BeautifulSoup(plaintxt)
    for item in soup.findAll('span',{'itemprop':'name'}):
        print(item.string + "<--PAGE")
    for link in soup.findAll('a'):
        href= link.get('href')
        #fw.write(href +"\n")
        print(href)




fw = open('KijijiGuitarStuff.txt','w')
spider(2)
fw.close()

# http://www.kijiji.ca/b-grand-montreal/guitar/k0l80002
#
# http://www.kijiji.ca/b-grand-montreal/guitar/page-2/k0l80002
