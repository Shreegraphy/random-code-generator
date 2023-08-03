import random
from tkinter import *
def random_quote():
    with open('qoutes.txt', 'r') as file:
        q = file.readlines()
        random_q = random.choice(q)
        print(random_q.strip())
        

root = Tk()
root.geometry('100x100')

btn = Button(root, text='Click me!', bd='5', command=random_quote)
btn.pack(side='top')


root.mainloop()
