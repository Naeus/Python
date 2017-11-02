import tkinter as tk

#a class that has 2 columns of frames inside
class TwoFrames(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        #creates 2 frame objects and passes self as parent, which means object created using TwoFrames class is the parent
        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)

        #manages 2 frames geometry
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid(row=0, column=1, sticky="nsew")

        #enables resizing for 0th row, and 1st and 2nd columns of an object of this class
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

class TwoLabels(tk.Frame):
    def __init__(self, master=None, color=True):
        super().__init__(master)

        #creates 2 Label objects with TwoLabels object as parent
        self.label1 = tk.Label(self)
        self.label2 = tk.Label(self)

        #configures the background color of labels for demonstrative purposes
        if color:
            #label1 will have red color
            self.label1.configure(bg="black")
            #label2 will have blue color
            self.label2.configure(bg="white")
        else:
            #label1 will have blue color
            self.label1.configure(bg="white")
            #label2 will have red color
            self.label2.configure(bg="black")


        #manages the geometry
        self.label1.grid(column=0, row=0, sticky="nsew")
        self.label2.grid(column=0, row=1, sticky="nsew")

        #enables resizing like above, but this time for 2 rows and 1 column
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

#creates the mainWindow
mainWindow = tk.Tk()

#creates a mainFrame that has 2 frames in it
mainFrame = TwoFrames(mainWindow)

#manages geometry of mainFrame and display it
mainFrame.pack(fill="both", expand=True)

#creates row_labels1 and row_labels2, both has 2 colored labels in them
row_labels1 = TwoLabels(mainFrame.frame1, True)
row_labels2 = TwoLabels(mainFrame.frame2, False)

#manages geometry of labels inside frames and displays them
row_labels1.pack(fill="both", expand=True)
row_labels2.pack(fill="both", expand=True)

#run the application
mainWindow.mainloop()
