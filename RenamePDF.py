import logging
import traceback
import sys
'''
fileName = "DebugLOGs"
try:
    

    #logging.warning('About to parse a file!!')
except Exception as e:
    f = open("/Users/jeromelefebvre/GitHub/Extract-Snippets-from-PDFs/logs/ERRORS.log", "w")
    sys.exit(0)
    f.write("hey....")
    f.close()
'''


import pdfplumber
import re
from datetime import datetime
import argparse
import sys
import os

logging.basicConfig(filename=rf'/Users/jeromelefebvre/GitHub/Extract-Snippets-from-PDFs/logs/warning.log', 
        encoding='utf-8', 
        level=logging.WARNING, 
        filemode='w', 
        format='%(asctime)s,%(levelname)s,%(message)s')

logging.warning('About to parse a file')


def snippet(pathToPDF, pattern):
    # returns the snippet found given a regular expression    
    logging.warning(f'Pattern: {pattern}')
    logging.warning(f'Path: {pathToPDF}')
    
    p = re.compile(pattern)
    with pdfplumber.open(pathToPDF) as pdf:
        content = pdf.pages[0].extract_text()
        p.search(content).groups()
        
        logging.warning(f'{p.search(content).groups()}')
        return p.search(content).groups()[0]

def formatString(fstring, snippets):
    logging.warning(snippets)
    return fstring.format(*snippets)

def formatTime(inputTime, format):
    try: 
        return datetime.strptime(inputTime, format).strftime(r'%Y-%m-%d %H%M')
    except Exception as e:
        logging.error("Couldn't convert the time")
        logging.error(f'Error: {e}')
        raise NotImplementedError


def newName(pathToPDF, nameFormat, timeFormat, *patterns):
    logging.warning(f'[newName] Patterns: {patterns}')
    snippets = [snippet(pathToPDF, pattern) for pattern in patterns]
    logging.warning(f'all snippers: {snippets}')
    snippets[0] = formatTime(snippets[0], timeFormat)

    return formatString(nameFormat, snippets) + ".pdf"

def safeFilename(name):
    return name.replace('/', '-')

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("format", nargs=1, help="format of the output file")
    parser.add_argument("timeFormat", nargs=1, help="format of the output file")
    parser.add_argument("regx", nargs='+', help="the regular expressions")
    args = parser.parse_args()

    logging.warning(f'all arguments: {args}')
    filePath = sys.stdin.readline().rstrip()

    name = newName(filePath, args.format[0], args.timeFormat[0], *args.regx)
    logging.warning(f'filename: {name}')

    basePath, fileName = os.path.split(filePath)

    os.rename(filePath, basePath + '/' + safeFilename(name))
    

#echo '/Users/jeromelefebvre/GitHub/Extract-Snippets-from-PDFs/testFiles/UFJTest2.pdf' | python3 /Users/jeromelefebvre/GitHub/Extract-Snippets-from-PDFs/RenamePDF.py '{0} - {1} - {2}' '%d %B %Y at %H:%M' 'Date: (.*)' 'ご利用先\s*:\s(.*)' 'ご利用金額（円）\s*:\s(\d*)'


#echo '/Users/jeromelefebvre/Documents/Action/Personal/-1.pdf' | python3 /Users/jeromelefebvre/GitHub/Extract-Snippets-from-PDFs/RenamePDF.py '{0} - {1} - {2}' '%d %B %Y at %H:%M' 'Date: (.*)' 'ご利用先\s*:\s(.*)' 'ご利用金額（円）\s*:\s(\d*)'

'''
echo $1 | python3 /Users/jeromelefebvre/GitHub/Extract-Snippets-from-PDFs/RenamePDF.py '{0} - {1} - {2}¥' '%d %B %Y at %H:%M' 'Date: (.*)' '○ご購入商品:\n(.*)' 'お支払い合計金額:\n(.\d*)円'
'''