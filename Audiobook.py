import pyttsx3
import PyPDF2
from tkinter.filedialog import*


book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.runAndWait()
    rate = player.getProperty('rate')
    player.setProperty('rate', 150)
    player.say(text)
