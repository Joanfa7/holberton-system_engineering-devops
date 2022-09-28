#!/usr/bin/python3
''' Module of nomber of subsccribers '''

import requests


def top_ten(subreddit):
    ''' Comment '''
    url = "https://www.reddit.com/r/{}/.json?limit=10".format(subreddit)
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64)\
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
                Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response = response.json().get('data').get('children')
        for post in response:
            title = post.get('data').get('title')
            print(title)
    else:
        print("None")
