from tkinter import *
import random


def diceroll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(number)}')
    label.pack()


root = Tk()
root.title("Dice Simulator")
root.geometry('400x500')
label = Label(root, font='Vendana 300 bold', text="")
button = Button(root, font=('Vendana', 25, 'bold'),
                text="Dice Roll", command=diceroll, bg='lightblue', fg='red')
button.pack()
root.mainloop()
