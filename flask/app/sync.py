import requests
import json
from helper import *

#SYNC
def sync_with_others(ip, blocks):
    for block in blocks:
        requests.post('http://'+ ip +':5000/add', data = block)
