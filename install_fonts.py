# native modules
import os
import urllib.request
import zipfile
import subprocess
import glob

# Pre-build
if (not os.path.exists("./temp/font_files")):
    os.mkdir("./temp/font_files")

# .py files
import __constants


def run():
def download_font(url):
    fileName = os.path.basename(url) 

    print(f'fileName = {url}')
    try:
        retrieve_response = urllib.request.urlretrieve(
            url, f'./temp/font_files/{fileName}' )
        file_path = retrieve_response[0]
        return file_path
    except:
        print(f'Failed to download: {fileName}')

