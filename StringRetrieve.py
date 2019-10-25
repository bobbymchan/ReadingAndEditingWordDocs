# Get single string for a word document

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

#print(getText('C:\\Users\\####\\Desktop\\Python Code\\Section 14\\demo.docx'))
