from functions import *
from variables import *

canva.pack()
frame.place(relwidth=0.9, relheight=1, relx=0.05, rely=0.05)
title.pack()


from_currency.place(y=100, height=30)
to_currency.place(y=130, height=30)
amount.place(y=160, height=30)
result.place(y=360, height=30)


ConvertButton = Button(frame, width=w, bg='darkorange', text='CONVERT', font='Arial, 20', fg='yellow', command=Convert)
ConvertButton.pack(pady=150)

Label(frame, text='Result', font='Arial, 20', fg='yellow', bg='orange').place(y=308, x=175)


if __name__ == '__main__':
    root.mainloop()