import json
import random

config_file = 'article_app/content_api.json'
stock_file  = 'article_app/quotes_api.json'

# Create Controller additions here
def process_config_file(config = config_file):
    import os
    print(os.getcwd())
    with open(config) as json_file:
        data = json.load(json_file)
    return data

def get_first_article(config = config_file ):
    data = process_config_file(config)['results']
    for primary_node in data:
        for item in primary_node:
            if item == 'tags':
                for i in primary_node[item]:
                    if i['slug'] == '10-promise':
                        return primary_node

def get_random_three_articles(config = config_file):
    arr = []
    exclude = get_first_article(config)
    data = process_config_file(config)['results']
    while (len(arr) < 3):
        choice = random.choice(data)
        if choice != exclude and not choice in arr:
            arr.append(choice)
    return arr

def get_three_stocks(config = stock_file):
    arr = []
    data = process_config_file(config)
    while (len(arr) < 3):
        choice = random.choice(data)
        if not choice in arr:
            arr.append(choice)
    return arr

def retrience_article_by_uuid(uuid):
    data = process_config_file(config_file)['results']
    for primary_node in data:
        if primary_node['uuid'] == uuid:
            return primary_node

