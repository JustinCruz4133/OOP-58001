from tkinter import *
win = Tk()
win.geometry("400x200+10+10")
win.title("Grid Manager")

#this is where you put your widgets

txt1 = Entry(win, bd = 2, justify = "center")
txt1.grid(row = 0, column = 0)
txt1.insert(0, "row 0" + " " + "Column 0")

txt2 = Entry(win, bd = 2, justify = "center")
txt2.grid(row = 0, column = 1)
txt2.insert(0, "row 0" + " " + "Column 1")

txt3 = Entry(win, bd = 2, justify = "center")
txt3.grid(row = 0, column = 2)
txt3.insert(0, "row 0" + " " + "Column 2")

txt4 = Entry(win, bd = 2, justify = "center")
txt4.grid(row = 1, column = 0)
txt4.insert(0, "row 1" + " " + "Column 0")

txt5 = Entry(win, bd = 2, justify = "center")
txt5.grid(row = 1, column = 1)
txt5.insert(0, "row 1" + " " + "Column 1")

txt6 = Entry(win, bd = 2, justify = "center")
txt6.grid(row = 1, column = 2)
txt6.insert(0, "row 1" + " " + "Column 2")

txt7 = Entry(win, bd = 2, justify = "center")
txt7.grid(row = 2, column = 0)
txt7.insert(0, "row 2" + " " + "Column 0")

txt8 = Entry(win, bd = 2, justify = "center")
txt8.grid(row = 2, column = 1)
txt8.insert(0, "row 2" + " " + "Column 1")

txt9 = Entry(win, bd = 2, justify = "center")
txt9.grid(row = 2, column = 2)
txt9.insert(0, "row 2" + " " + "Column 2")

txt10 = Entry(win, bd = 2, justify = "center")
txt10.grid(row = 3, column = 0)
txt10.insert(0, "row 3" + " " + "Column 0")

txt11 = Entry(win, bd = 2, justify = "center")
txt11.grid(row = 3, column = 1)
txt11.insert(0, "row 3" + " " + "Column 1")

txt12 = Entry(win, bd = 2, justify = "center")
txt12.grid(row = 3, column = 2)
txt12.insert(0, "row 3" + " " + "Column 2")

win.mainloop()