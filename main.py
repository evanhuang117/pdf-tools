import sys
import os
from PyPDF2 import PdfFileMerger

def get_files():
    dir = sys.argv[1]
    return [dir + name for name in os.listdir(dir)

def merge_files():

if __name__ == '__main__':

