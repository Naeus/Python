import tkinter as tk


root = tk.Tk()


def mousewheel(event):
    print(event.delta)
    textbox.yview_scroll(int(-1*(event.delta/120)), "units")

textbox = tk.Text(root, height=30, width=60, font="Arial")
textbox.grid(row=6,sticky="s")
textbox.bind_all("<MouseWheel>", mousewheel)

root.mainloop()
