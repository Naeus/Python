import tkinter as tk

def create_f2(event):
    global f2

    print(f2)

    if f2:
        f2.destroy()
        f2 = None

    else:
        f2 = tk.Frame(root, bg='green', width=100, height=100)
        f2.pack()
        f2.bind("<Enter>", create_f1)
        f2.bind("<Leave>", create_f2)

def create_f1(event):
    global f1

    print(f1)

    if f1:
        f1.destroy()
        f1 = None
    else:
        f1 = tk.Frame(root, bg='red', width=100, height=100)
        f1.pack()
        f1.bind("<Leave>", create_f1)
        f1.bind("<Enter>", create_f2)



















root = tk.Tk()

f1 = tk.Frame(root, width=100, height=100, bg='red')
f2 = None

f1.pack()

f1.bind("<Enter>", create_f2)

root.mainloop()