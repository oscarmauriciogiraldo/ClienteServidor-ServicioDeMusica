from tkinter import *

root = Tk()
root.geometry('300x300')
root.title("SputiFai")
#root.iconbitmap(r'melody.ico')

text = Label(root, text='Lista de Reproduccion!')
text.pack()


def play_btn():
    print("Hey! This play button works pretty well!")


photo = PhotoImage(file='ondas-sonoras.png')
btn = Button(root, image=photo, command=play_btn)
btn.pack()

root.mainloop()