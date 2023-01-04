from RenamePDF import snippet, formatString, newName, formatTime

folderPath = r'/Users/jeromelefebvre/GitHub/Extract-Snippets-from-PDFs/testFiles/'

assert snippet(folderPath + '20210331 1528 - UBER   *TRIP - 981.pdf', r'ご利用先\s*:\s(.*)') == 'PAYMATE*Kirkham Lndry'

assert snippet(folderPath + '20210331 1528 - UBER   *TRIP - 981.pdf', r'ご利用金額（円）\s*:\s(\d*)') == '174'

assert snippet(folderPath + '20210331 1528 - UBER   *TRIP - 981.pdf', r'Date: (.*)') == '31 March 2021 at 15:47'

assert formatString('{0}', ['31 March 2021 at 15:47']) == '31 March 2021 at 15:47'

assert formatTime('31 March 2021 at 15:47', r'%d %B %Y at %H:%M') == '20210331 1547'

#assert newName(folderPath + '20210331 1528 - UBER   *TRIP - 981.pdf', '{datetime.strptime(v[0], "%d %B %Y at %H:%M").strftime("%Y%m%d %H%M")} - {v[1]} - {v[2]}', [r'Date: (.*)', r'ご利用先\s*:\s(.*)', r'ご利用金額（円）\s*:\s(\d*)']) == "20210331 1547 - PAYMATE*Kirkham Lndry - 174.pdf"

assert newName(folderPath + '20210331 1528 - UBER   *TRIP - 981.pdf', '{0} - {1} - {2}', '%d %B %Y at %H:%M', r'Date: (.*)', r'ご利用先\s*:\s(.*)', r'ご利用金額（円）\s*:\s(\d*)') == "20210331 1547 - PAYMATE*Kirkham Lndry - 174.pdf"
#python3 path '{0:timeformat} - {1}' 're1' 're2'