import os
import natsort
from PyPDF2 import PdfFileMerger
from pathlib import Path

def get_dir():
    dir_path = Path(input("Enter the full directory path of pdfs you want to merge: "))
    # expand ~ for user home directory, needed because python is processing the dir string
    return dir_path.expanduser()

def get_files(dir):
    # python sorted() doesnt do alphanumeric (natural) sort
    alphanum_sorted = natsort.natsorted(dir.glob("*.pdf"))
    return alphanum_sorted

def merge_files(paths):
    merger = PdfFileMerger()
    for pdf in paths:
        print("Merging: " + str(pdf))
        merger.append(str(pdf));
    return merger

def merge():
    file_dir = get_dir()
    pdf_files = get_files(file_dir)
    merged = merge_files(pdf_files)
    # write the entire merged pdf then close the merger
    output_path = file_dir / "{}-merged.pdf".format(str(file_dir.name))
    print("Writing merged PDF to: " + str(output_path))
    merged.write(str(output_path))
    merged.close()