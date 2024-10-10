import requests
from bs4 import BeautifulSoup


def get_channel_id(handle):
    url = f"https://www.youtube.com/{handle}"
    response = requests.get(url, verify=False)
    # print(response.text)
    # print(response.content)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the channel ID in the meta tags
    # channel_id_meta = soup.find("meta", {"itemprop": "name"})

    channel_id_meta = soup.find("meta", {"itemprop": "channelId"})
    if channel_id_meta:
        return channel_id_meta["content"]

    channel_id_meta = soup.find("meta", {"itemprop": "identifier"})
    if channel_id_meta:
        return channel_id_meta["content"]
    return "Channel ID not found"


handle = "@3protv"
channel_id = get_channel_id(handle)
print(f"Channel ID: {channel_id}")
