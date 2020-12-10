import pyttsx3
import PyPDF2
 #open the pdf and read binary
book=open('halfgirlfriend.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)

#count the pages

pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
for num in range(9,pages):
    page = pdfReader.getPage(10)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

