import json
import random
import time
import os
from core import pinBot

bot = pinBot()

bot_dir = os.path.dirname(__file__)
with open(os.path.join(bot_dir,'pinterestBot.json')) as json_data:
    bot_config = json.load(json_data)

with open(os.path.join(bot_dir,'done_pins.json')) as json_data:
    done_pins = json.load(json_data)

# generate posts to post
pin_upload_count = bot_config['periods']['post_to_post_per_day']
available_posts = list(filter(lambda x: x['imageUrl'] not in done_pins ,bot_config['posts']))

if len(available_posts) <= pin_upload_count:
    pin_upload_count = len(available_posts)

if len(available_posts)>0:
    for post in random.sample(available_posts,pin_upload_count):
        bot.createPost(post['imageUrl'],post['note'])
        time.sleep(1)
        done_pins.append(post['imageUrl'])

    with open(os.path.join(bot_dir,'done_pins.json'), 'w') as outfile:
        json.dump(done_pins, outfile)
