
from tkinter import *

root = Tk()
root.geometry('300x300')
root.title("SputiFai")
#root.iconbitmap(r'SputiFai.ico')

text = Label(root, text='Lista de Reproduccion!')
text.pack()

photo = PhotoImage(file='ondas-sonoras.png')
labelphoto = Label(root, image = photo)
labelphoto.pack()

root.mainloop()