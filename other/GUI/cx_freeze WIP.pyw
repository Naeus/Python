import tkinter as tk
from tkinter import filedialog
from cx_Freeze import setup, Executable
import sys, os

class AppName(tk.Tk):
    def __init__(self):
        super().__init__()

        self.name = tk.Entry(self)
        self.version = tk.Entry(self)
        self.description = tk.Entry(self)
        self.open = tk.Button(self, text="Open...", command=self.open)
        self.convert = tk.Button(self, text="Convert", command=self.convert)
        self.script_file = ''
        self.cmd_disabled = tk.BooleanVar()
        self.is_GUI = tk.Checkbutton(self, variable=self.cmd_disabled,
                                        onvalue=True, offvalue=False)
        self.layout()

    def layout(self):
        self.name.pack()
        self.version.pack()
        self.description.pack()
        self.is_GUI.pack()
        self.open.pack()
        self.convert.pack()


    def open(self):
        self.script_file = filedialog.askopenfilename(filetypes=(("Python Files", "*.py"),("Python GUI Files", "*.pyw")))

    def convert(self):
        base = None
        if self.cmd_disabled.get():
            if (sys.platform == "win32"):
                base = "Win32GUI"    # Tells the build script to hide the console.
            elif (sys.platform == "win64"):
                base = "Win64GUI"    # Tells the build script to hide the console.
        setup(
            name=self.name.get(),
            version=self.version.get(),
            description=self.description.get(),
            executables=[Executable(self.script_file, base=base)])

        self.destroy()


if __name__ == "__main__":
    sys.argv.append('build')
    os.environ['TCL_LIBRARY'] = r'C:\Users\Naelone Maxwell\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
    os.environ['TK_LIBRARY'] = r'C:\Users\Naelone Maxwell\AppData\Local\Programs\Python\Python36\tcl\tk8.6'


    root = AppName()
    root.mainloop()
