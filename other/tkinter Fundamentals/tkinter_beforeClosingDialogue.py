import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def on_closing():
    response = messagebox.askyesnocancel("NaePad - Unsaved File", "Do you want to save before leaving?")
    print(ara)
    if ara:
        root.destroy()
    elif ara is None:
        print("asd")

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
