import tkinter 
from tkinter import *
from textblob import TextBlob

root = Tk()
root.tittle("Spelling Checker")
root.geometry("700*400")
root.config(background="#dae6f6")
def check_spelling():
     word = 'enter_text' .get()
     a = TextBlob (word)
     right = str(a.correct())
     Spell = Label(root, text="Initial Text", font=("poppins", 20), bg="#dae6f6", fg="#36471")
     Spell.place(x=100, y=300)
     Spell.config(text = right)
     heading = Label(root, text="Spelling Checker", font=('Trebuchet Ms', 30, 'bold'), bg='#dae6f6', fg='#364971')
     heading.pack(pady =(50, 0))
     enter_text = Entry(root, justify='center', width=30, font=('poppins',25), bg='white', border=2)
     enter_text . pack(pady=10)
     enter_text.focus()
     button = Button(root, text ='check', font=('arial',20, 'bold'), fg='white', bg='red', command= check_spelling)
     button.pack()
     Spell = Label(root, font=('poppins',20), bg='#dae6f6', fg='#364971')
     Spell. place(X=350, y= 250)
     
     
     root.mainloop ()
     
     
     
     