#required for anything GUI related
import tkinter as tk
#required for fileopen and save options
from tkinter import filedialog
#required for file's basename
import os

#Nae Unicode text entering is missing

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.titleVar = tk.StringVar()
        self.title("Untitled - NaePad")
        self.iconbitmap(default="C:\\Users\\Naelone Maxwell\\Documents\\GitHub\\Python\\other\\asd.ico")

        self.mainFrame = MainFrame(self)
        self.mainFrame.pack(fill="both", expand=True)

        self.mainFrame.text.focus_set()


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        #creates and displays the Menu
        self.menu = MainMenu(master)
        master.config(menu=self.menu)

        #path of the current file
        self.curFilePath = ''

        self.text = tk.Text(self, wrap="none")
        #color scheme
        self.text.config(bg='#282c34',fg='#abb2bf', selectbackground='#3e4451')
        self.text.grid(row=0, column=0, sticky="nsew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.scroll_bar_config()
        self.menu_command_config()
        self.key_binds_config()


    #scrollbar configurations for self.text widget
    def scroll_bar_config(self):

        self.scrollY = AutoScrollbar(self, orient="vertical", command=self.text.yview)
        self.scrollY.grid(row=0, column=1, sticky="nsew")
        self.text['yscrollcommand'] = self.scrollY.set

        self.scrollX = AutoScrollbar(self, orient="horizontal", command=self.text.xview)
        self.scrollX.grid(row=1, column=0, sticky="nsew")
        self.text['xscrollcommand'] = self.scrollX.set

    def menu_command_config(self):

        #New
        self.menu.file.entryconfig(0, command=self.new_file)

        #Open...
        self.menu.file.entryconfig(1, command=self.open_file)

        #Save
        self.menu.file.entryconfig(2, command=self.save_file)

        #Save as
        self.menu.file.entryconfig(3, command=self.save_as_file)


        #Cut
        self.menu.edit.entryconfig(0, command=self.cut)

        #Copy
        self.menu.edit.entryconfig(1, command=self.copy)

        #Paste
        self.menu.edit.entryconfig(2, command=self.paste)

        #Delete
        self.menu.edit.entryconfig(3, command=self.delete)

    def key_binds_config(self):
        self.text.bind('<Control-n>', self.new_file)
        self.text.bind('<Control-N>', self.new_file)
        self.text.bind('<Control-o>', self.open_file)
        self.text.bind('<Control-O>', self.open_file)
        self.text.bind('<Control-s>', self.save_file)
        self.text.bind('<Control-S>', self.save_file)
        #BALI doesn't work
        self.text.bind('<Control-Shift-s>', self.save_as_file)
        self.text.bind('<Control-Shift-S>', self.save_as_file)

    def new_file(self, *args):
        self.text.delete("1.0", "end")
        self.curFilePath = ''

    def open_file(self, *args):

        #get filepath from user with gui
        filePath = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"),("All files", "*.*")))

        # if filePath is selected
        if filePath:
            try:
                #open only UTF-8 encoded files
                with open(filePath, encoding="UTF-8") as f:
                    self.text.delete("1.0", "end")
                    self.text.insert("1.0", f.read())
            #if it's not UTF-8 then
            except UnicodeDecodeError:
                #open as ANSI encoding
                with open(filePath, encoding="ANSI") as f:
                    self.text.delete("1.0", "end")
                    self.text.insert("1.0", f.read())

            #update window name to file name
            self.master.title(os.path.basename(f.name) + " - NaePad")

            #update current file path
            self.curFilePath = filePath

    def save_file(self, *args):
        #if there's already a file
        if self.curFilePath:
            try:
                #open only UTF-8 encoded files
                with open(self.curFilePath, 'w', encoding="UTF-8") as f:
                    f.write(self.text.get('1.0', 'end-1c'))
            #if it's not UTF-8 then
            except UnicodeDecodeError:
                #open as ANSI encoding
                with open(self.curFilePath, 'w', encoding="ANSI") as f:
                    f.write(self.text.get('1.0', 'end-1c'))

            #update window name to file name
            self.master.title(os.path.basename(f.name) + " - NaePad")

        else:
            self.save_as_file()

    def save_as_file(self, *args):
        self.curFilePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"),("All files", "*.*")))
        #Checks wether a file is selected or not
        if self.curFilePath:
            self.save_file()


    def cut(self):
        #Is anything selected?
        if self.text.tag_ranges(tk.SEL):
            self.text.clipboard_clear()
            #append to cleared clipboard the (selection)
            self.text.clipboard_append(self.text.get(tk.SEL_FIRST, tk. SEL_LAST))
            self.text.delete(tk.SEL_FIRST, tk. SEL_LAST)

    def copy(self):
        #Is anything selected?
        if self.text.tag_ranges(tk.SEL):
            self.text.clipboard_clear()
            #append to cleared clipboard the (selection)
            self.text.clipboard_append(self.text.get(tk.SEL_FIRST, tk. SEL_LAST))

    def paste(self):
        #Is anything selected?
        if self.text.tag_ranges(tk.SEL):
            #keeping a reference on where the selection starts
            selFirstIndex = self.text.index(tk.SEL_FIRST)
            #removing selection first
            self.text.delete(tk.SEL_FIRST, tk. SEL_LAST)
            #copying from clipboard
            self.text.insert(selFirstIndex, self.text.clipboard_get())

        else:
            self.text.insert(tk.INSERT, self.text.clipboard_get())

    def delete(self):
        #Is anything selected?
        if self.text.tag_ranges(tk.SEL):
            self.text.delete(tk.SEL_FIRST, tk. SEL_LAST)


#MainMenu object that contains Sub-menus
class MainMenu(tk.Menu):
    def __init__(self, master):
        super().__init__(master, tearoff=0)
        self.master = master

        #create Menu Options
        self.file = FileMenu(self)
        self.add_cascade(label="File", menu=self.file)

        self.edit = EditMenu(self)
        self.add_cascade(label="Edit", menu=self.edit)


#Menu class that handles File Operations
class FileMenu(tk.Menu):
    def __init__(self, master):
        super().__init__(master, tearoff=0)
        self.master = master

        self.add_command(label="New                Ctrl + N")
        self.add_command(label="Open...          Ctrl + O")
        self.add_command(label="Save               Ctrl + S")
        self.add_command(label="Save As...      Ctrl + Shift + S")


        #add the line before exit
        self.add_separator()
        #destroy's the grandparent, which is assumed to be a toplevel
        self.add_command(label="Exit                 Alt + F4", command=master.master.destroy)


#Menu class that handles editorial operations
class EditMenu(tk.Menu):
    def __init__(self, master):
        super().__init__(master, tearoff=0)

        self.add_command(label="Cut              Ctrl + X")
        self.add_command(label="Copy           Ctrl + C")
        self.add_command(label="Paste          Ctrl + V")
        self.add_command(label="Delete         Delete")


#http://effbot.org/zone/tkinter-autoscrollbar.htm
class AutoScrollbar(tk.Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
        tk.Scrollbar.set(self, lo, hi)


def test():
    with open(__file__, "rU") as f:
        root.mainFrame.text.insert("1.0", f.read())


if __name__ == "__main__":
    root = MainWindow()
    #test()
    root.mainloop()
