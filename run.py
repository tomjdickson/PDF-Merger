import os
from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfFileMerger

# Gets all files in the working directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Filters down to PDF files only
files = filter(lambda f: f.endswith(('.pdf','.PDF')), files) 

merger = PdfFileMerger()

for pdf in files:

    merger.append(pdf)

merger.write("result.pdf")

