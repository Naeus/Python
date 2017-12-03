import tkinter as tk

root = tk.Tk()

c = 0

def space_event(event):
    global c

    print(c)
    c += 1

    if c >= 20:
        root.unbind("<space>")

root.bind("<space>", space_event)

root.mainloop()
