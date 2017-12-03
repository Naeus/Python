#! python3

import tkinter as tk

class CalculatorFrame(tk.Frame):                                                #Class for Calculator frame
    def __init__(self, master=None):                                            #How we initialize CalculatorFrame, and what is done when it's initialized.
        super().__init__(master)
        self.screen = EntryFrame(self)
        self.numpad = NumPad(self, self.number_button_press)

        #sets the focus to screen
        self.screen.entry1.focus_set()
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)
        self.columnconfigure(0, weight=1)
        self.screen.grid(row=0, sticky="news")
        self.numpad.grid(row=1, sticky="news")

    def widget_resize_event(self, event, widgetObjects):                               #Event that handles fontsize of widget's text upon resizing
        fontSize = event.height // 4                                            #should be along the lines of min(height/3, width /char_length)

        try:
            for eachObject in widgetObjects:
                eachObject.configure(font=("default", fontSize, "normal"))            #setting the fontsize of the widget
        except:
            widgetObjects.configure(font=("default", fontSize, "normal"))            #setting the fontsize of the widget

    def number_button_press(self, number):
        #cursor is always at beginning
        self.screen.entry1.icursor('end')
        #insert the number into screen
        self.screen.entry1.insert('end', number)

class NumPad(tk.Frame):
    def __init__(self, master=None, button_command=lambda *args: ''):
        super().__init__(master)
        self.button_command = button_command
        self.buttons(master=self)

    def buttons(self, master, buttonsNum=10, size=(4, 2), fntSize=12, tabEnabled=False):
        buttons = list((tk.Button(master=master, text=str(num), width=size[0], height=size[1], font=("Default", fntSize, "normal"), takefocus=tabEnabled, command=lambda var=num: self.button_command(var))) for num in range(buttonsNum-1, -1, -1))
        negateButton = tk.Button(master=master, text=chr(177), width=size[0], height=size[1], font=("Default", fntSize, "normal"), takefocus=tabEnabled)
        buttons.append(negateButton)
        equalsButton = tk.Button(master=master, text="=", width=size[0], height=size[1], font=("Default", fntSize, "normal"), takefocus=tabEnabled, command=lambda: equalsButton.destroy())
        buttons.append(equalsButton)




        self.buttons = tuple(buttons)

        rowLength = 3
        for i in range(len(buttons)):
            rowNumber = i // rowLength
            colNumber = i % rowLength
            self.buttons[i].grid(row=rowNumber, column=colNumber, sticky="news")
            master.rowconfigure(rowNumber, weight=1)
            master.columnconfigure(colNumber, weight=1)

            #self.buttons[i].bind("<Configure>", lambda event, widgetObjects=self.buttons: CalculatorFrame.widget_resize_event(event, widgetObjects)) #WORK IN PROGRESS

class operationPad(tk.Frame):
    def __init__(self, master=None, button_command=lambda *args: ''):
        self.button_command = button_command
        super().__init__(master)



class EntryFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        vcmd = (self.register(self.is_valid), '%S', '%s', '%P')
        self.text = tk.StringVar()
        self.isDoubleOperation = False
        self.isDoublePoint = False
        self.lastChar = ''

        self.entry1 = tk.Entry(master=master, justify="right", font=("Default", 24, "normal"),
         insertontime="0", textvariable=self.text)
        self.entry1.configure(validate="key", validatecommand=vcmd)
        self.entry1.configure(relief="flat")
        self.entry1.grid(sticky="news")
        self.rowconfigure(0, weight=1)

    def white_list(self, text, keepTable="0123456789+-*/ ."):
        from collections import defaultdict
        d = defaultdict(str, str.maketrans(keepTable, keepTable))
        return text.translate(d)

    # ERROR needs rework
    def is_valid(self, char, oldText, newText, numerals=set('0123456789'), operations=set('+-*/')):

        #If typing in
        if len(oldText) < len(newText):
            if newText == self.white_list(newText):
                if not ((self.lastChar == '' or self.lastChar == ' ') and char == ' '):
                    self.lastChar = char
                    return True
                else:
                    return False
            else:
                self.bell()
                return False
        #Can delete everything, always
        else:
            return True

mainWindow = tk.Tk()                                                            #Creating the main window
mainWindow.title("")                                                  #Setting the title of the main window
mainWindow.iconbitmap(default="C:\\Users\\Naelone Maxwell\\Documents\\GitHub\\Python\\other\\asd.ico")
CalculatorFrame(mainWindow).pack(fill='both', expand=True)

#mainWindow.resizable(False, False)
mainWindow.mainloop()

'''
'''
