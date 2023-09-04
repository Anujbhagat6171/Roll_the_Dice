#pip install pillow

from tkinter import*
from random import choice
from PIL import Image,ImageTk

root=Tk()
root.title("Roll The Dice!!")
root.geometry("400x400+500+100")

dice =['1rr.png','2rr.png','3rr.png','4rr.png','5rr.png','6rr.png']

def f1():
	img1=ImageTk.PhotoImage(Image.open(choice(dice)))
	lbl.configure(image=img1)
	lbl.image=img1

btn=Button(root, text='Roll it!!', font=('calibri',20,'bold'), command=f1)
btn.pack(pady=10)

img1=ImageTk.PhotoImage(Image.open(choice(dice)))
lbl=Label(root, image=img1)
lbl.pack(pady=10)

root.mainloop()
