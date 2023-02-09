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
