#! python3

import tkinter

class Frame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #self.pack()

    def num_pad(self, size=(2, 1), fntSize=8):
        self.negateBtn = tkinter.Button(self, text=chr(177), width=size[0],
                                        height=size[1])
        #self.negateBtn = tkinter.Button(self, text=chr(177), width=size[0], height=size[1], font=("Default", 8, "normal"))
        self.negateBtn.grid(row=3, column=0)

        self.pntBtn = tkinter.Button(self, text=".", width=size[0], height=size[1])
        self.pntBtn.grid(row=3, column=1)

        self.zeroBtn = tkinter.Button(self, text="0", width=size[0], height=size[1])
        self.zeroBtn.grid(row=3, column=2)

        self.oneBtn = tkinter.Button(self, text="1", width=size[0], height=size[1])
        self.oneBtn.grid(row=2, column=0)

        self.twoBtn = tkinter.Button(self, text="2", width=size[0], height=size[1])
        self.twoBtn.grid(row=2, column=1)

        self.threeBtn = tkinter.Button(self, text="3", width=size[0], height=size[1])
        self.threeBtn.grid(row=2, column=2)

        self.fourBtn = tkinter.Button(self, text="4", width=size[0], height=size[1])
        self.fourBtn.grid(row=1, column=0)

        self.fiveBtn = tkinter.Button(self, text="5", width=size[0], height=size[1], command=exit)
        self.fiveBtn.grid(row=1, column=1)

        self.sixBtn = tkinter.Button(self, text="6", width=size[0], height=size[1])
        self.sixBtn.grid(row=1, column=2)

        self.sevenBtn = tkinter.Button(self, text="7", width=size[0], height=size[1], state="disable")
        self.sevenBtn.grid(row=0, column=0)

        self.eightBtn = tkinter.Button(self, text="8", width=size[0], height=size[1], relief="groove")
        self.eightBtn.grid(row=0, column=1)

        self.nineBtn = tkinter.Button(self, text="9", width=size[0], height=size[1])
        self.nineBtn.grid(row=0, column=2)


    def opr_pad(self, size=(2, 1), fntSize=8):
        self.addBtn = tkinter.Button(self, text="+", width=size[0], height=size[1])
        self.addBtn.grid(row=0, column=0)

        self.subBtn = tkinter.Button(self, text="-", width=size[0], height=size[1])
        self.subBtn.grid(row=0, column=1)

        self.prdBtn = tkinter.Button(self, text="*", width=size[0], height=size[1])
        self.prdBtn.grid(row=1, column=0)

        self.divBtn = tkinter.Button(self, text="/", width=size[0], height=size[1])
        self.divBtn.grid(row=1, column=1)

        self.eqlBtn = tkinter.Button(self, text="=", width=size[0], height=size[1])
        self.eqlBtn.grid(row=2, column=0)

        self.sqrtBtn = tkinter.Button(self, text=chr(8730), width=size[0], height=size[1])
        self.sqrtBtn.grid(row=2, column=1)

        self.rprcBtn = tkinter.Button(self, text="1/x", width=size[0], height=size[1])
        self.rprcBtn.grid(row=3, column=0)

        self.pcntBtn = tkinter.Button(self, text="%", width=size[0], height=size[1])
        self.pcntBtn.grid(row=3, column=1)








mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
frame1 = Frame(master=mainWindow)
frame2 = Frame(master=mainWindow)
frame1.num_pad()
frame2.opr_pad()
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
mainWindow.resizable(False, False)
mainWindow.mainloop()
