#!/opt/homebrew/bin/python3

import pdfplumber
import sys

import logging, os

fileName = "LOGs.pdf"

# Creates a file in the log folder of the script
# Erases it each time
logging.basicConfig(filename=rf'/Users/jeromelefebvre/GitHub/Extract-Snippets-from-PDFs/logs/{fileName}.log', 
    encoding='utf-8', 
    level=logging.WARNING, 
    filemode='w', 
    format='%(asctime)s,%(levelname)s,%(message)s')

logging.warning('[helper] being called')

filePath = sys.stdin.readline().rstrip()

logging.warning(f'[helper] File to parse {filePath}')

with pdfplumber.open(filePath) as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())



#echo '/Users/jeromelefebvre/Documents/Action/Apple.pdf' | python3 /Users/jeromelefebvre/GitHub/Extract-Snippets-from-PDFs/helper.py | pbpaste