from tkinter import *

root = Tk()
h = 500
w = 250*2

root.geometry(f"{w}x{h}")
root.resizable(height=False, width=False)
root.title('Currency converter')
root.resizable(width=False, height=False)

canva = Canvas(root, width=w, height=h, bg='orange')
frame = Frame(root, bg='orange')
title = Label(frame, text='Currency converter', bg='orange', font='Arial, 40', foreground='yellow')


from_currency = Entry(frame, width=w, font='Arial, 10')
from_currency.insert(END, 'Enter in the  currency you\'d like to convert from(clear this text): ')

to_currency = Entry(frame, width=w, font='Arial, 10')
to_currency.insert(END, 'Enter in the  currency you\'d like to convert from(clear this text): ')

amount = Entry(frame, width=w, font='Arial, 10')
amount.insert(END, 'Enter amount(clear this text): ')

result = Entry(frame, width=w, font='Arial, 10')

