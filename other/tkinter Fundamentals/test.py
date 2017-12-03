import tkinter_Updating_fontsize_based_on_widget_size3 as fr

import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.calculationSpace = tk.StringVar()

        #MainApplication's calculatorScreen is assigned
        self.calculatorScreen = CalculatorScreen(self, self.calculationSpace)

        #show calculatorScreen
        self.calculatorScreen.grid(row=0, column=0, columnspan=4, rowspan=1, sticky="nsew")

        #set focus_set
        self.calculatorScreen.focus_set()

        self.buttons = CalculatorButtons(self, self.calculationSpace)
        self.buttons.grid(row=1, column=0, columnspan=4, rowspan=4, sticky="nsew")

        self.calculatorScreen.bind("<Return>", self.equal)

        grid_scale(self)

    #No ERROR handling
    def equal(self, event):
        if self.calculationSpace:
            self.calculationSpace.set(str(eval(self.calculationSpace.get())))

#A frame that has entry widget in it
class CalculatorScreen(tk.Label):
    def __init__(self, master, calculationSpace):
        super().__init__(master)
        self.master = master
        self.calculationSpace = calculationSpace
        self.config(textvariable=self.calculationSpace)
        self.config(insertontime=0, justify="right", relief="flat")
        self.validation_configuration()
        fr.font_resizable(self)

    def validation_configuration(self):

        vcmd = (self.register(self.is_valid), '%S', '%s', '%P')
        self.config(validate="key", validatecommand=vcmd)

    # ERROR needs rework
    def is_valid(self, char, oldText, newText):

        #If typing in
        if len(oldText) < len(newText):
            if newText == self.white_list(newText):
                return True
            else:
                self.bell()
                return False
        #Can delete everything, always
        else:
            return True

    def white_list(self, text, keepTable="0123456789+-*/."):
        from collections import defaultdict
        d = defaultdict(str, str.maketrans(keepTable, keepTable))
        return text.translate(d)

#A frame that has calculator buttons
class CalculatorButtons(tk.Frame):
    def __init__(self, master, calculationSpace):
        super().__init__(master)
        self.calculationSpace = calculationSpace

        self.basicoperations = BasicOperations(self, self.calculationSpace)
        self.basicoperations.grid(row=0, column=0, rowspan=4, columnspan=1, sticky="nsew")

        self.numerals = Numerals(self, self.calculationSpace)
        self.numerals.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew")

        self.misc = MiscOperations(self, self.calculationSpace)
        self.misc.grid(row=3, column=1, rowspan=1, columnspan=3, sticky="nsew")

        grid_scale(self)

#A frame that has numerals except for 0 as buttons
class Numerals(tk.Frame):
    def __init__(self, master, calculationSpace, focusEnabled=False):
        super().__init__(master)

        self.calculationSpace = calculationSpace

        # numerals in decimal, so up to 9
        buttonsNum = 9
        #creates an empty list
        self.numButtons = list()
        #number of buttons there will be on each row
        rowLength = 3
        #create the buttons
        for num in range(buttonsNum):
            numeral = str(num + 1)
            #create buttons with numerals
            self.numButtons.append(tk.Button(self, text=numeral))
            fr.font_resizable(self.numButtons[num])
            self.numButtons[num].configure(command=lambda number = numeral: self.button_command(number), takefocus=focusEnabled)
            self.numButtons[num].grid(row=(rowLength - (num // rowLength) - 1), column=num % rowLength, sticky="nsew")

        grid_scale(self)

    def button_command(self, number):
        self.calculationSpace.set(self.calculationSpace.get() + number)
        #self.calculationSpace.insert('end', number)

#A frame that has basic operations buttons
class BasicOperations(tk.Frame):
    def __init__(self, master, calculationSpace, focusEnabled=False):
        super().__init__(master)

        self.calculationSpace = calculationSpace

        self.buttons = list()

        # '+' self.buttons[0]
        self.buttons.append(tk.Button(self, text='+'))
        # '-' self.buttons[1]
        self.buttons.append(tk.Button(self, text='-'))
        # '*' self.buttons[2]
        self.buttons.append(tk.Button(self, text='*'))
        # '/' self.buttons[3]
        self.buttons.append(tk.Button(self, text='/'))

        #configure the geometry and commands
        for i in range(len(self.buttons)):
            buttonID =  self.buttons[i].cget('text')
            fr.font_resizable(self.buttons[i])
            self.buttons[i].configure(command=lambda opr = buttonID: self.button_command(opr))
            self.buttons[i].configure(takefocus=focusEnabled)
            self.buttons[i].grid(row=i, column=0, sticky="nsew")

        grid_scale(self)

    def button_command(self, opr):
        self.calculationSpace.set(self.calculationSpace.get() + opr)

class MiscOperations(tk.Frame):
    def __init__(self, master, calculationSpace, focusEnabled=False):
        super().__init__(master)

        self.calculationSpace = calculationSpace

        self.buttons = list()
        # '=' self.buttons[0]
        self.buttons.append(tk.Button(self, text='='))
        # 'chr(177)' self.buttons[1]
        self.buttons.append(tk.Button(self, text=chr(177)))
        # '0' self.buttons[2]
        self.buttons.append(tk.Button(self, text='0'))

        #configure the geometry and commands
        for i in range(len(self.buttons)):
            buttonID = self.buttons[i].cget('text')
            fr.font_resizable(self.buttons[i])
            self.buttons[i].configure(command=lambda opr = buttonID: self.button_command(opr))
            self.buttons[i].configure(takefocus=focusEnabled)
            self.buttons[i].grid(row=0, column=i, sticky="nsew")

        grid_scale(self)

    #WIP
    def button_command(self, opr):
        calcSpace = self.calculationSpace.get()

        #calcSpace shouldn't be empty
        if calcSpace:
            if opr == '=':
                self.calculationSpace.set(str(eval(calcSpace)))

            #WIP
            elif opr == chr(177):
                pass

            elif opr == '0':
                self.calculationSpace.set(self.calculationSpace.get() + '0')

#a function that enables scaling of a grid that the argument has
def grid_scale(gridParent):
    gridColLength, gridRowLength = gridParent.grid_size()
    print(gridParent.grid_size())

    for row in range(gridRowLength):
        gridParent.rowconfigure(row, weight=1, uniform=True)
    for col in range(gridColLength):
        gridParent.columnconfigure(col, weight=1, uniform=True)

if __name__ == "__main__":
    root = tk.Tk()

    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
