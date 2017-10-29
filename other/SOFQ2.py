import tkinter as tk

initRoot = tk.Tk()

def new_Window():
    width = entry1.get()
    height = entry2.get()
    #initRoot.destroy()
    initRoot.geometry(width + "x" + height)
    #root.mainloop()
    #root

label1 = tk.Label(initRoot, text="Width:")
entry1 = tk.Entry(initRoot)

label2 = tk.Label(initRoot, text="Height:")
entry2 = tk.Entry(initRoot)

button1 = tk.Button(initRoot, text="Done", command=new_Window)

label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
button1.grid(row=2, columnspan=2)


initRoot.mainloop()
