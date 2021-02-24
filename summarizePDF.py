import pdfplumber
import os
from summarizer import Summarizer
from summarizer.coreference_handler import CoreferenceHandler
from fpdf import FPDF
import spacy


def use_coreference():
    spacy.load('en_core_web_lg')
    handler = CoreferenceHandler(spacy_model='en_core_web_lg')
    return Summarizer(sentence_handler=handler)


# TODO: find out why this seg faults when true
use_coref = False


def summarize():
    file_name = get_name()
    pdf = pdfplumber.open(file_name)
    print("Imported a PDF with " + str(len(pdf.pages)) + " pages")

    text = read_pdf(pdf)
    summarized = summarize_string(text)
    # fix encoding issues with text
    summarized = summarized.encode('latin-1', 'replace').decode('utf-8')

    # remove file extension from the name
    file_name = file_name.split('.', 1)[0]
    output_name = file_name + "-summarized.pdf"
    save_text(summarized, output_name)


def summarize_string(text):
    # run the summarizer
    if use_coref:
        model = use_coreference()
    else:
        model = Summarizer()

    print("summarizing")
    summarized = model(body=text)
    return summarized


def read_pdf(pdf):
    # read in the text
    text = ""
    for pg in pdf.pages:
        print("Processing page " + str(pg.page_number))
        text += pg.extract_text()
    return text


def get_name():
    path = input("Enter the full path of the pdf you want to summarize: ")
    # expand ~ for user home directory, needed because python is processing the dir string
    return os.path.expanduser(path)


def save_text(text, output_name):
    ''' uncomment to print to text file
    with open(file_name + "-summarized", 'w') as f:
        f.write(summarized)
    '''
    # output the summarized text to a pdf
    output_pdf = FPDF()
    output_pdf.add_page()
    output_pdf.set_font("Arial", size=12)
    # multi_cell auto line breaks (wrap text)
    output_pdf.multi_cell(200, 10, text, align='L')
    output_pdf.output(output_name)
