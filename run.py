import os
from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfFileMerger
import json

# Set config
with open('config.json') as json_data_file:
    data = json.load(json_data_file)
    pagenumber = data["page"]
    outfile = data["outputFileName"]

# Gets all files in the working directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Filters down to PDF files only
files = filter(lambda f: f.endswith(('.pdf','.PDF')), files) 

merger = PdfFileMerger()

# Sets each file in the files array to "pdf"
for pdf in files:

    # Meger all files put the second file after page 10
    merger.merge(pagenumber, pdf)

# Output the file    
merger.write(outfile)

