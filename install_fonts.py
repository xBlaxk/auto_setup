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
    for url in __constants.fontURL:
        file_path = download_font(url)
        extracted_files = uncompress_font_file(file_path)
        install_font_file(extracted_files)


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

def getAllFiles(path, extensions):
    extracted_files = []

    for extension in extensions:
        print(f'Looking for /*.{extension}')
        extracted_files.extend(glob.glob(f'{path}/*.{extension}'))

    return extracted_files

def install_font_file(fonts):
    test_font = fonts[0]
    install_command = f'copy "{test_font}" "C:\\Windows\\Fonts"'
    subprocess.run(install_command, shell=True)
    # for font in fonts:
    #     font_name = os.path.basename(font)
    #     install_command = f'copy {font} C:\\Windows\\Fonts'
    #     try:
    #         print(f'Installing font: {font_name}')
    #         subprocess.run(install_command, shell=True)
    #         print(f'Font installed: {font_name}')
    #     except:
    #         print(f'Failed to install the font: {font_name}')

    print("install_tff_file")
