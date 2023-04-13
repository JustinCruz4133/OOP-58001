from tkinter import *
class MyExam:
    def __init__(self, mid):

        self.lbl1 = Label(mid, text = "My Full Name")
        self.lbl1.place(x=200, y=20)
        self.lbl2 = Label(mid, text = "Enter Given Name:")
        self.lbl2.place(x=100, y=50)
        self.lbl3 = Label(mid, text = "Enter Middle Name:")
        self.lbl3.place(x=100, y=80)
        self.lbl4 = Label(mid, text = "Enter Last Name:")
        self.lbl4.place(x=100, y=110)
        self.lbl5 = Label(mid, text = "My Full Name is:")
        self.lbl5.place(x=100, y=150)

        self.input1 = Entry(mid, bd=2)
        self.input1.place(x=300, y=50)
        self.input2 = Entry(mid, bd=2)
        self.input2.place(x=300, y=80)
        self.input3 = Entry(mid, bd=2)
        self.input3.place(x=300, y=110)

        self.result4 = Entry(mid, bd=2, width = 30)
        self.result4.place(x=300, y=150)

        self.showfullbtn = Button(mid, text = "Show Full Name", command = self.show_full)
        self.showfullbtn.place(x=200, y=180)

    def show_full(self):
        self.result4.delete(0, 'end')
        Gname = str(self.input1.get())
        Mname = str(self.input2.get())
        Lname = str(self.input3.get())
        result = Gname + " " + Mname + " " + Lname
        self.result4.insert(END, str(result))

EXAM = Tk()
midterm = MyExam(EXAM)
EXAM.geometry("500x300+10+10")
EXAM.title("Midterm Exam Problem 2")
EXAM.mainloop()