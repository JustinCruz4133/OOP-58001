from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("My First GUI")

btn1 = Button(window, text = "Click Me", fg = "White", bg = "Black")
btn1.place(x = 50, y = 120)

txtfld = Entry(window, border = 5)
txtfld.place(x = 50, y = 70)

lbl = Label(window, text = "My First Demo", font = "Verdana")
lbl.place(x = 50, y = 20)




window.mainloop()