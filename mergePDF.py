import os
import natsort
from PyPDF2 import PdfFileMerger

def get_dir():
    dir = input("Enter the full directory path of pdfs you want to merge: ")
    # check for proper formatting of dir
    if dir[-1] != '/':
        dir += '/'
    # expand ~ for user home directory, needed because python is processing the dir string
    return os.path.expanduser(dir)

def get_files(dir):
    # python sorted() doesnt do alphanumeric (natural) sort
    alphanum_sorted = natsort.natsorted([name for name in os.listdir(dir) if name.endswith(".pdf")])
    return [dir + name for name in alphanum_sorted if name.endswith(".pdf")]

def merge_files(paths):
    merger = PdfFileMerger()
    for pdf in paths:
        print("Merging: " + pdf)
        merger.append(pdf);
    return merger

def merge():
    dir = get_dir()
    pdf_files = get_files(dir)
    merged = merge_files(pdf_files)
    # write the entire merged pdf then close the merger
    # last / in dir name causes an empty string at end of list so filter it out
    parent_dir = list(filter(None, dir.split('/')))[-1]
    output_name = dir + parent_dir + "-merged.pdf"
    print("Writing merged PDF to: " + output_name)
    merged.write(output_name)
    merged.close()