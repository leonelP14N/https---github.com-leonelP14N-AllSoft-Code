import webbrowser
from tkinter import *

root= Tk();

root.title('Meu App Browser')
root.geometry('450x300')

def AbrirGoogle():
    webbrowser.open('www.google.com')

bbgoogle= Button(root, text='Abrir o Google', command=AbrirGoogle).pack(pady=20)

root.mainloop()

