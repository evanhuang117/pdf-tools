from pathlib import Path

import natsort
from PyPDF2 import PdfFileMerger
import glob
import tqdm
import os
import pikepdf

def get_dir():
    dir_path = Path(input("Enter the full directory path of pdfs you want to merge: "))
    # expand ~ for user home directory, needed because python is processing the dir string
    return dir_path.expanduser()

def get_files(dir):
    # python sorted() doesnt do alphanumeric (natural) sort
    # convert_pptx(dir)
    alphanum_sorted = natsort.natsorted(dir.glob("*.pdf"))
    return alphanum_sorted

# this requires unoconv to be installed
def convert_pptx(dir):
    extension = "pptx"
    files = [f for f in glob.glob(dir + "/**/*.{}".format(extension), recursive=True)]
    for f in tqdm.tqdm(files):
        command = "unoconv -f pdf \"{}\"".format(f)
        os.system(command)

def merge_files(paths):
    merger = PdfFileMerger()
    for pdf in paths:
        try:
            print(f"Merging: {str(pdf)}")
            merger.append(str(pdf));
        except ValueError:
            repaired = pikepdf.open(pdf, allow_overwriting_input=True)
            repaired.save(pdf)
            print(f"\tRepairing: {str(pdf)}")
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
