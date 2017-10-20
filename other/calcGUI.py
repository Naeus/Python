#! python3

import tkinter

def white_list(string1):
    from collections import defaultdict
    keepTable = "0123456789+-*/"
    d = defaultdict(str, str.maketrans(keepTable, keepTable))

    return string1.translate(d)


class Frame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

    def btn_pad(self, size=(4, 2), fntSize=8, tabEnabled=False):
        self.negateBtn = tkinter.Button(self, text=chr(177), width=size[0], height=size[1], takefocus=tabEnabled)
        self.negateBtn.grid(row=3, column=0)

        self.pntBtn = tkinter.Button(self, text=".", width=size[0], height=size[1], takefocus=tabEnabled)
        self.pntBtn.grid(row=3, column=1)

        self.zeroBtn = tkinter.Button(self, text="0", width=size[0], height=size[1], takefocus=tabEnabled)
        self.zeroBtn.grid(row=3, column=2)

        self.oneBtn = tkinter.Button(self, text="1", width=size[0], height=size[1], takefocus=tabEnabled)
        self.oneBtn.grid(row=2, column=0)

        self.twoBtn = tkinter.Button(self, text="2", width=size[0], height=size[1], takefocus=tabEnabled)
        self.twoBtn.grid(row=2, column=1)

        self.threeBtn = tkinter.Button(self, text="3", width=size[0], height=size[1], takefocus=tabEnabled)
        self.threeBtn.grid(row=2, column=2)

        self.fourBtn = tkinter.Button(self, text="4", width=size[0], height=size[1], takefocus=tabEnabled)
        self.fourBtn.grid(row=1, column=0)

        self.fiveBtn = tkinter.Button(self, text="5", width=size[0], height=size[1], takefocus=tabEnabled, command=exit)
        self.fiveBtn.grid(row=1, column=1)

        self.sixBtn = tkinter.Button(self, text="6", width=size[0], height=size[1], takefocus=tabEnabled)
        self.sixBtn.grid(row=1, column=2)

        self.sevenBtn = tkinter.Button(self, text="7", width=size[0], height=size[1], takefocus=tabEnabled, state="disable")
        self.sevenBtn.grid(row=0, column=0)

        self.eightBtn = tkinter.Button(self, text="8", width=size[0], height=size[1], takefocus=tabEnabled, relief="groove")
        self.eightBtn.grid(row=0, column=1)

        self.nineBtn = tkinter.Button(self, text="9", width=size[0], height=size[1], takefocus=tabEnabled)
        self.nineBtn.grid(row=0, column=2)

        self.addBtn = tkinter.Button(self, text="+", width=size[0], height=size[1], takefocus=tabEnabled)
        self.addBtn.grid(row=0, column=3)

        self.subBtn = tkinter.Button(self, text="-", width=size[0], height=size[1], takefocus=tabEnabled)
        self.subBtn.grid(row=0, column=4)

        self.prdBtn = tkinter.Button(self, text="*", width=size[0], height=size[1], takefocus=tabEnabled)
        self.prdBtn.grid(row=1, column=3)

        self.divBtn = tkinter.Button(self, text="/", width=size[0], height=size[1], takefocus=tabEnabled)
        self.divBtn.grid(row=1, column=4)

        self.sqrtBtn = tkinter.Button(self, text=chr(8730), width=size[0], height=size[1], takefocus=tabEnabled)
        self.sqrtBtn.grid(row=2, column=3)

        self.rprcBtn = tkinter.Button(self, text="1/x", width=size[0], height=size[1], takefocus=tabEnabled)
        self.rprcBtn.grid(row=2, column=4)

        self.pcntBtn = tkinter.Button(self, text="%", width=size[0], height=size[1], takefocus=tabEnabled)
        self.pcntBtn.grid(row=3, column=3, sticky="wens")

        self.eqlBtn = tkinter.Button(self, text="=", width=size[0], height=size[1], takefocus=tabEnabled)
        self.eqlBtn.grid(row=3, column=4)


    def scrn(self):
        self.s = tkinter.Entry(self, justify="right", font=("Default", 24, "normal"), insertontime="0", relief="flat")
        self.s.pack(fill="x", expand="1")
        self.s.focus_set()

    def num_repr(self):
        self.num1 = 0

def asd(event):
    print("asd")



def key(event):
    print (white_list("19023801nhjfsdbf a23 2ı34nb +112389+-123/4213/*"))


mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
frame1 = Frame(master=mainWindow)
frame2 = Frame(master=mainWindow)
frame1.btn_pad()
frame2.scrn()
frame2.focus_set()
frame2.s.bind("a", key)
frame1.oneBtn.bind("<Button-1>", key)
frame1.grid(row=1, column=0)
frame2.grid(row=0, sticky="wens")

mainWindow.resizable(False, False)
mainWindow.mainloop()
