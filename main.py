# TODO: fix dependency issues
#import summarizePDF

import mergePDF

#TODO: add option to specify order of merging by outputting list of names
# and asking user to enter csv list of array indices

def prompt_user():
    choice = input("1. Merge PDFs\n")
                   #"2. Summarize a PDF\n")
    if choice == '1':
        mergePDF.merge()
    #elif choice == 2:
    #    summarizePDF.summarize()

if __name__ == '__main__':
    prompt_user()
