import requests
from bs4 import BeautifulSoup 
import re #Regular expression pattern matching
import sys #for argument parsing
import json
import os

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error : Please enter Ted Talk Downloader")

r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, 'html.parser')

script_tag = soup.find("script", id="__NEXT_DATA__")
data = json.loads(script_tag.string)

player_data_raw = data["props"]["pageProps"]["videoData"]["playerData"]
player_data = json.loads(player_data_raw)

# Get the MP4 URL — using the first available h264 file (usually 1200k quality)
result_mp4 = player_data["resources"]["h264"][0]["file"]

print("Downloading:", result_mp4)

file_name = os.path.basename(result_mp4.split('?')[0])

print("Storing video in ...." + file_name)

r = requests.get(result_mp4)

with open(file_name, 'wb') as f :
    f.write(r.content)

print("Download finished")