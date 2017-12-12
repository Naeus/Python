import tkinter as tk

class AppName(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)

        <create the rest of your GUI here>

if __name__ == "__main__":
    root = AppName()
    root.mainloop()
