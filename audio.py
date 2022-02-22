from cProfile import label
from importlib.resources import path
import click
from matplotlib import image
from matplotlib.pyplot import text, title
from nbformat import read
import pyttsx3
import PyPDF2
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog



bg='#ffdab9'

app=Tk()
app.geometry('300x400')
app.title('AudioBook')
app.configure(bg=bg)



path=None

def click():
    global path
    path = filedialog.askopenfilename()
    print(path)
    
    
def talk():
    page_n = page_number_box.get()
    if path and page_n:
         # init the speaker
         speaker = pyttsx3.init()

         # Open the pdf
         book = open(path, 'rb')

         # Read the pdf
         read_file = PyPDF2.PdfFileReader(book)

         # Choosing the page that we want to read
         page = read_file.getPage(int(page_n))

         # Extract the text from the page
         text = page.extractText()
         
         speaker.setProperty('rate',150)
         speaker.setProperty('volume', 0.7)
         
         voices = speaker.getProperty('voices')
         speaker.setProperty('voice', voices[0].id)

         speaker.say(text)
         speaker.runAndWait()
    


image = Image.open('download.jpeg')
imageResized = image.resize((150,100), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(imageResized)


logo = Label(app, image=image1 ,bg=bg)
logo.pack()


title = Label(app, text='Let listen to the book',bg=bg,font='none 20')
title.pack()


page_number = Label(app, text='Please enter the page number',bg=bg)
page_number.pack(pady=(50,0))


page_number_box = Entry(app,bg=bg,)
page_number_box.pack()


open_PDF = Button (app,text='Open',width=18,command= click)
open_PDF.pack(pady=(40,0))


say_PDF = Button(app, text='Talk', width=18, command=talk)
say_PDF.pack(pady=(40,0))



app.mainloop()

