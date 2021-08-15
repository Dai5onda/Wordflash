import docx

doc = docx.Document(r"C:\Users\AN515-52\Downloads\Wordflash2.docx")

DocParag = (doc.paragraphs) 

for doc in DocParag:
    print(doc.text)
