#!python3

import os
import subprocess
from pytube import YouTube
import random
import requests
import re
import string

def foldertitle(url):
    try:
        res = requests.get(url)
    except:
        print('no internet')
        return False

    plain_text = res.text

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]
    else:
        print('Incorrect attempt.')
        return False
    return cPL

def link_snatcher(url):
    our_links = []
    try:
        res = requests.get(url)
    except:
        print('no internet')
        return False

    plain_text = res.text

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]
    else:
        print('Incorrect Playlist.')
        return False

    tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
    mat = re.findall(tmp_mat, plain_text)

    for m in mat:
        new_m = m.replace('&amp;', '&')
        work_m = 'https://youtube.com/' + new_m
        # print(work_m)
        if work_m not in our_links:
            our_links.append(work_m)

    return our_links

BASE_DIR = os.getcwd()
os.system('cls' if os.name == 'nt' else 'clear')
print('YOUTUBE PLAYLIST DOWNLOADER')
url = str(input("\ninsert the url of the playlist: \n"))
print('\nChose Video Quality :- \n To choose 360p, type "360p" \n To choose 720p, type "720p" \n')
user_res = str(input()).lower()
print('...You choosed ' + user_res + ' resolution\n.')

our_links = link_snatcher(url)
os.chdir(BASE_DIR)
new_folder_name = foldertitle(url)
print(new_folder_name[:7])

try:
    os.mkdir(new_folder_name[:7])
except:
    print('folder already exists')

os.chdir(new_folder_name[:7])
SAVEPATH = os.getcwd()
print(f'\n files will be saved to {SAVEPATH}')

x=[]
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        pathh = os.path.join(root, name)
        if os.path.getsize(pathh) < 1:
            os.remove(pathh)
        else:
            x.append(str(name))

print('\nconnecting...\n')

print()
for link in our_links:
    print(" downloading " + YouTube(link).title)
    
    yt = YouTube(link)
    if user_res == '360p':
        try:
            yt.streams.filter(res='360p').first().download(SAVEPATH)
        except:
            print('error')
    elif user_res == '720p':
        try:
            yt.streams.filter(res='720p').first().download(SAVEPATH)
        except:
            print('error')
    else:
        print('error')
    print()

print('done')

