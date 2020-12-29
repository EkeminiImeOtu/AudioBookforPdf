import time
import pyttsx3
import PyPDF2

def audiobook():
    book = open("poordad.pdf", "rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(pages)
    speaker = pyttsx3.init()
    engine = pyttsx3.init()
    rate = speaker.getProperty("rate")
    print(rate)
    speaker.setProperty("rate", 150)
    speaker.setProperty("volume", 1)
    
   

    for num in range (1, pages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
       
        time.sleep(10)
        
audiobook()
   

