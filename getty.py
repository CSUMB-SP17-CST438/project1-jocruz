# import llaves
import requests
import random
import json
import os
# 
class imageLoc:
    def __init__(self,link):
        self.l = link
    def __str__(self):
        return self.l

def getIMG():
    url = "https://api.gettyimages.com:443/v3/search/images?fields=comp&license_models=royaltyfree&minimum_size=large&sort_order=best_match&phrase=puppies"
    header = {"Api-Key": os.environ['gettyKey']}
    response = requests.get(url, headers = header)
    imgs = response.json()
    size = len(imgs['images'])
    i = random.randint(1,size-1)
    uri = imgs['images'][i]['display_sizes'][0]['uri']
    img = imageLoc(uri)
    return img
    
# print(json.dumps(imgs, indent=2))