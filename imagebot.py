# coding=UTF-8

import tweepy
import glob
import random
import os
import shutil
from ConfigParser import SafeConfigParser

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

parser = SafeConfigParser()
parser.read("config.cfg")

api_key = parser.get('keys_and_token', 'api_key')
api_secret = parser.get('keys_and_token', 'api_secret')
oauth_token = parser.get('keys_and_token', 'oauth_token')
oauth_token_secret = parser.get('keys_and_token', 'oauth_token_secret')

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(oauth_token, oauth_token_secret)
api = tweepy.API(auth)

def imagebot(folder):
    images = glob.glob(folder + "*")
    image_open = images[random.randint(0,len(images))-1]
    image_size = os.path.getsize(image_open)
    status = "This is a random image from your screenshots folder"
#next lines format the image for twitter
    if image_size >= 3072 * 1024:
        os.system("sips -Z 1024 " + image_open)
    api.update_with_media(image_open, status)
    #next lines copy the used screenshot to a selected copied image folder.
    shutil.copy(image_open, "screenshots/copied_images/")
    os.remove(image_open)
#The following line is where you set your image folder
imagebot("screenshots/")