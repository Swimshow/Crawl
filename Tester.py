from urllib import request
import random
import os



def downloadPhoto(url):
    os.chdir(os.getcwd() +"//ImagesTaken")
    print(os.getcwd())
    name1 = random.randrange(1,1000)
    fullname = str(name1) + ".jpg"
    urllib.request.urlretrieve(url, fullname)

#downloadPhoto("https://scontent-yyz1-1.xx.fbcdn.net/v/t1.0-0/p75x225/13900288_10153808529818657_5564793178075307713_n.jpg?oh=6c0c3a02dfe3a7dba1aff4e0f2e1e2ff&oe=593C1B33")
aphURL = 'http://chart.finance.yahoo.com/table.csv?s=APH.V&a=1&b=3&c=2017&d=2&e=3&f=2017&g=d&ignore=.csv'

def downloadCSV(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    fw = open('aph.csv','w')
    for line in lines:
        fw.write(line + "\n")
    fw.close()




downloadCSV(aphURL)

