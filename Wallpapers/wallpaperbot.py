#!/usr/bin/env python3.6

import praw
import io
import os
import random
from PIL import Image
from imgurpython import ImgurClient
import configparser

def getResolution(image):
    im = Image.open(image)
    if (im.size[0] < 1024 or im.size[1] < 768):
        return False
    else:
        return True

def select_image(dir_path):
    image_file = None
    while not image_file:
        image_file = os.path.join(
            dir_path, random.choice(os.listdir(dir_path))
        )
        if not getResolution(image_file):
            image_file = None
        else:
            return image_file

def get_configs():
    config_parser = configparser.RawConfigParser()
    config_file_path = r'./creds.ini'
    config_parser.read(config_file_path)
    reddit_creds = {
        'client_id'       : config_parser.get('reddit_creds', 'client_id'),
        'client_secret'   : config_parser.get('reddit_creds', 'client_secret'),
        'username'        : config_parser.get('reddit_creds', 'username'),
        'password'        : config_parser.get('reddit_creds', 'password'),
        'user_agent'      : config_parser.get('reddit_creds', 'user_agent'),
    }
    imgur_creds = {
        'client_id'       : config_parser.get('imgur_creds', 'client_id'),
        'client_secret'   : config_parser.get('imgur_creds', 'client_secret'),
        'access_token'    : config_parser.get('imgur_creds', 'access_token'),
        'refresh_token'   : config_parser.get('imgur_creds', 'refresh_token'),
    }
    return reddit_creds, imgur_creds

my_path = "./unusedWallpapers"
reddit_creds, imgur_creds = get_configs()
print(reddit_creds)
print(imgur_creds)

reddit = praw.Reddit(client_id=reddit_creds['client_id'],
                     client_secret=reddit_creds['client_secret'],
                     password=reddit_creds['password'],
                     username=reddit_creds['username'],
                     user_agent=reddit_creds['user_agent'])

imgur_client = ImgurClient(imgur_creds['client_id'],
                           imgur_creds['client_secret'],
                           imgur_creds['access_token'],
                           imgur_creds['refresh_token'])

image = select_image(my_path)
im = Image.open(image)
title = f'From my collection [{im.size[0]}x{im.size[1]}]'
print(title)
imgur_post = {
    'name': title,
    'title': title,
}

image_url = imgur_client.upload_from_path(image, config=imgur_post, anon=False)
print(image_url['link'])

wallpapers_subreddit = reddit.subreddit('wallpapers')
wallpapers_subreddit.submit(title=title,
                            url=image_url['link'],
                            send_replies=True)
os.rename(image,
          os.path.join('./usedWallpapers/', os.path.basename(image))
         )
