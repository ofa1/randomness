import docx
import re
sourcedir = 'C:/Users/omahmed/Dropbox/0mair - Azhar/Books/Juma Khutba Books/4th Book/Khutbas - 2017/'
doc = docx.Document(sourcedir + 'Motivation drives effort.docx')
arabicRegex = re.compile('[ا-ي]+')
nextTranslationText = 0

doc.styles['Normal'].font.name = 'Palatino Linotype'
doc.styles['Normal'].font.size = docx.shared.Pt(11)

def handleEnglishRun(r):
    r.font.name = 'Palatino Linotype'
    r.font.size = docx.shared.Pt(11)

def handlePara(p):
    global nextTranslationText
    if re.match(arabicRegex, p.text):
        # print(p.text)
        nextTranslationText = 1
    elif nextTranslationText == 1:
        nextTranslationText = 0
        for run in p.runs:
            # print(run.text, run.font.name)
            if run.font.name == 'Tahoma':
                handleEnglishRun(run)
    elif 'List' not in p.style.name:
        print(p.style)
        p.style = doc.styles['Normal']
        print(p.style)



# for para in doc.paragraphs:
#     handlePara(para)

for style in doc.styles:
    print(style)
    if style.get('font'):
        style.font.name = 'Palatino Linotype'
doc.save(sourcedir+'mm1.docx')