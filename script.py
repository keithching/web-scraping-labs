# http request
import requests
# scraping
from bs4 import BeautifulSoup
import urllib.request
import os

def getdata(url):
    r = requests.get(url)
    return r.text

HOST = "https://sakurazaka46.com"

htmldata = getdata("https://sakurazaka46.com/s/s46/contents_list?ima=2445&cd=104&ct=fc_photo_048&so=ID")

# with open('source.html') as fp:
    # print(fp)
soup = BeautifulSoup(open('source.html'), 'html.parser')
# print(soup)

with open('html_data.txt', 'w') as f:
    f.write(htmldata)

# soup = BeautifulSoup(htmldata, 'html.parser')

# create a folder in the file system in the container
# a bind mount is used to mirror to the local machine
def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

IMAGE_DIR = 'images'

my_makedirs(IMAGE_DIR)

number_of_photos = 0

with open('url_list.txt', 'w') as f:
    for index, item in enumerate(soup.find_all('img')):
        style = item.get('style')
        if (style):
            url = style.split('(', 1)[1].split(')')[0] # getting the substring within the parenthesis
            url = url.replace('/300_300_102400', '') # trim string
            fullUrl = HOST + url
            f.write(fullUrl)
            f.write('\n')
            
            number_of_photos += 1

            filepath = IMAGE_DIR + '/' + str(index) + '.jpg'
            # only write to file system if not exist
            if not os.path.exists(filepath):
                urllib.request.urlretrieve(fullUrl, filepath)

print('operation completed for ' + str(number_of_photos) + ' photos')