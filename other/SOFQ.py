from tkinter import *

root = Tk()
class Buttons:
    def __init__(self,master,ImperialText,MetricText,metricVal):
        self.ImperialText = ImperialText
        self.MetricText = MetricText



        self.master = master
        self.Text1 = (ImperialText +'-'+ MetricText)
        self.button = Button(self.master,text= self.Text1,command = self.calc)
        self.button.grid(column = 0)
        self.button.config(height= 3,width=30)

    def calc(self):
        self.EntryStr = None
        self.entry = Entry(self.master)
        self.label = Label(self.master,text = 'Enter '+self.ImperialText)

        self.entry.grid(column = 1,row = 1)
        self.label.grid(column = 1,row = 0)

        self.entry.bind('<Return>',self.valid)

    def valid(self):
        print (str(self.entry.get()))

button1 = Buttons(root,'inches','centimetres',2.54)
button2 = Buttons(root,'miles','kilometres',1.6093)
button3 = Buttons(root,'foot','metres',0.3048)
button4 = Buttons(root,'yards','metres',0.9144)
button5 = Buttons(root,'gallons','litres',4.546)
button6 = Buttons(root,'pounds','kilograms',0.454)
button7 = Buttons(root,'ounces','grams',0.454)

root.mainloop()
