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


def uncompress_font_file(zip_path):
    zip_name = os.path.basename(zip_path)
    folder_name = zip_name.split(".")[0]
    extract_path = "./temp/font_files/" + folder_name

    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(extract_path)

        print(f'Successfully uncompressed file {zip_name} on folder {extract_path}')
        extracted_files = getAllFiles(extract_path, __constants.font_extension)
        
        print('\n'.join('{}: {}'.format(*file) for file in enumerate(extracted_files)))
        return extracted_files
    except:
        print(f'Failed to uncompress: {zip_path}')
