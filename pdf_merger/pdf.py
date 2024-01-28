
# install PyPDF2 module 
from PyPDF2 import PdfMerger
import os

# create pdfMerger() object to access
merger = PdfMerger()

# looping through all the .pdf files in the directory and merging them into one single PDF file.
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        print(file)
        merger.append(file)

# combine all those files and create another file
merger.write("MergedPDF.pdf")
merger.close()  
