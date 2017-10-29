import tkinter as tk

def btn_func(master):
    SubFrame(master).grid(sticky="news")

    #ERROR needs tweaking
    tk.Grid.rowconfigure(master, 1, weight=1)
    tk.Grid.columnconfigure(master, 0, weight=1)



class MainFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)

        self.frameLeft = tk.Frame(master=self)
        self.frameLeft.grid(row=0, column=0, sticky="news")
        #self.labelLeft = tk.Label(master=self.frameLeft, text="Left", bg="red")
        #self.labelLeft.grid(sticky="wens")
        tk.Grid.rowconfigure(self.frameLeft, 0, weight=1)
        tk.Grid.columnconfigure(self.frameLeft, 0, weight=1)

        self.frameRight = tk.Frame(master=self)
        self.frameRight.grid(row=0, column=1, sticky="news")
        self.buttonRight = tk.Button(master=self.frameRight, text="Right", bg="blue", command=lambda master=self.frameLeft: btn_func(master))
        self.buttonRight.grid(sticky="news")
        tk.Grid.rowconfigure(self.frameRight, 0, weight=1)
        tk.Grid.columnconfigure(self.frameRight, 0, weight=1)



class SubFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.button = tk.Button(master=self)
        #self.button.configure(text="Button {num}".format(num=i))
        self.button.grid(sticky="news")
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)






app = tk.Tk()
masterFrame = MainFrame(master=app)
masterFrame.pack(fill="both", expand=True)

app.mainloop()
