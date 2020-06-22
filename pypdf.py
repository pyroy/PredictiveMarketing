import pydf
pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
