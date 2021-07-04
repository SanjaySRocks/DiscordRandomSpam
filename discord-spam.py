import requests
import time
import json
import os


with open("config.json","r") as f:
    config = json.load(f)


# load configs
token = config['token']
channel = str(config['channel_id'])

# Inputs
n = input("How many times ?: ")
delay = input("Enter delay in seconds: ")



header = {
    'authorization': token
}

for i in range(0,int(n)):
    data = requests.get("https://api.kanye.rest/")
    jsondata = data.json()
    payload = {
    'content' : jsondata["quote"]
    }

    r = requests.post("https://discord.com/api/v8/channels/"+channel+"/messages", data=payload, headers=header)
    time.sleep(int(delay))