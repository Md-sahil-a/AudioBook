import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')
pdfread = PyPDF2.PdfFileReader(book)
pages = pdfread.numPages
print(pages)
speak = pyttsx3.init()
for num in range(7, pages):
    page = pdfread.getPage(7)
    text = page.extractText()
    speak.say("Hello everyone I am a Reader, please listen carefully")
    speak.say(text)
    speak.runAndWait()
