import pypdf

writer = pypdf.PdfWriter()
writer.append('Recursion_Chapter1.pdf')
writer.encrypt('swordfish', algorithm='AES-256')

with open('encrypted.pdf', 'wb') as f:
    writer.write(f)
