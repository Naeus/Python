#! python3

import tkinter as tk

class CalculatorFrame(tk.Frame):                                                #Class for Calculator frame
    def __init__(self, master=None):                                            #How we initialize CalculatorFrame, and what is done when it's initialized.
        super().__init__(master)
        self.screen = EntryFrame(self)
        self.numpad = NumPad(self)
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=4)
        tk.Grid.columnconfigure(self, 0, weight=1)
        self.screen.grid(row=0, sticky="news")
        self.numpad.grid(row=1, sticky="news")                              #There's only one column

    def widget_resize_event(event, widgetObjects):                               #Event that handles fontsize of widget's text upon resizing
        fontSize = event.height // 4                                            #should be along the lines of min(height/3, width /char_length)

        try:
            for eachObject in widgetObjects:
                eachObject.configure(font=("default", fontSize, "normal"))            #setting the fontsize of the widget
        except:
            widgetObjects.configure(font=("default", fontSize, "normal"))            #setting the fontsize of the widget

class NumPad(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.buttons(master=self)

    def buttons(self, master, buttonsNum=10, size=(4, 2), fntSize=12, tabEnabled=False):
        buttons = list((tk.Button(master=master, text=str(num), width=size[0], height=size[1], font=("Default", fntSize, "normal"), takefocus=tabEnabled)) for num in range(buttonsNum-1, -1, -1))
        negateButton = tk.Button(master=master, text=chr(177), width=size[0], height=size[1], font=("Default", fntSize, "normal"), takefocus=tabEnabled)
        buttons.append(negateButton)
        pointButton = tk.Button(master=master, text=".", width=size[0], height=size[1], font=("Default", fntSize, "normal"), takefocus=tabEnabled, command=lambda: pointButton.destroy())
        buttons.append(pointButton)
        self.buttons = tuple(buttons)

        rowLength = 3
        for i in range(buttonsNum+2):
            rowNumber = i // rowLength
            colNumber = i % rowLength
            self.buttons[i].grid(row=rowNumber, column=colNumber, sticky="news")
            tk.Grid.rowconfigure(master, rowNumber, weight=1)
            tk.Grid.columnconfigure(master, colNumber, weight=1)

            self.buttons[i].bind("<Configure>", lambda event, widgetObjects=self.buttons: CalculatorFrame.widget_resize_event(event, widgetObjects)) #WORK IN PROGRESS


class EntryFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        vcmd = (self.register(self.is_valid), '%S')
        self.text = tk.StringVar()

        self.entry1 = tk.Entry(master=master, justify="right", font=("Default", 24, "normal"),
         insertontime="0", textvariable=self.text)
        self.entry1.configure(validate="key", validatecommand=vcmd)
        self.entry1.configure(relief="flat")
        self.entry1.grid(sticky="news")
        self.entry1.focus_set()


    def is_valid(self, char, validChars=set('0123456789+-*/ ')):
        if char in validChars:
            return True
        else:
            self.bell()
            return False

mainWindow = tk.Tk()                                                            #Creating the main window
mainWindow.title("")                                                  #Setting the title of the main window
mainWindow.iconbitmap(default="C:\\Users\\Naelone Maxwell\\Documents\\GitHub\\Python\\other\\asd.ico")
CalculatorFrame(mainWindow).pack(fill='both', expand=True)

#mainWindow.resizable(False, False)
mainWindow.mainloop()

'''
'''
