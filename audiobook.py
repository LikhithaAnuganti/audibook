import pyttsx3
import PyPDF2
book=open('griet.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
chutki=pyttsx3.init()
readFrom=pdfReader.getPage(1)
text = readFrom.extractText()
print(text)
chutki.say(text) 
chutki.runAndWait()