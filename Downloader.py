'''
Created on May 28, 2016

@author: Marcus
'''
from urllib import request
import random

def download_web_image(url):
    number=random.randrange(1,1000)
    full_name=str(number)+".jpg"
    request.urlretrieve(url, full_name)

download_web_image("http://i.imgur.com/dbg7fdP.jpg")