import time
import requests
import os
import webbrowser

import pyscreenshot as ImageGrab
from imgurpython import ImgurClient

imgur_image_endpoint = "https://api.imgur.com/3/image"
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

client = ImgurClient(CLIENT_ID, CLIENT_SECRET)

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

if __name__ == '__main__':
    im = ImageGrab.grab()
    file_name = time.strftime("%Y%m%d-%H%M%S") + '.jpg'
    im.save(file_name)

    r = client.upload_from_path(file_name, {}, anon=False)
    print(r['link'])
    addToClipBoard(r['link'])
    print('link added to clipboard')
    os.remove(file_name)

    webbrowser.open(r['link'])