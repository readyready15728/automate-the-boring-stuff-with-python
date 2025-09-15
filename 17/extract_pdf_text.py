from pdfminer.utils import enc
import pypdf
import pdfminer.high_level

PDF_FILENAME = 'Recursion_Chapter1.pdf'
TEXT_FILENAME = 'recursion.txt'

text = ''

try:
    reader = pypdf.PdfReader(PDF_FILENAME)

    for page in reader.pages:
        text += page.extract_text()
except Exception as e:
    text = pdfminer.high_level.extract_text(PDF_FILENAME)

with open(TEXT_FILENAME, 'w', encoding='utf-8') as f:
    f.write(text)
