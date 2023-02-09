# Native modules
import os

# Pre-build
if not os.path.exists("./temp"):
    os.mkdir("./temp")

# .py files
import install_fonts


install_fonts.run()
