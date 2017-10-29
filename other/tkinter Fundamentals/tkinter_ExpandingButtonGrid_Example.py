#https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter

import tkinter as tk

root = tk.Tk()
frame=tk.Frame(root)
frame.pack(fill="both", expand=True)

for x in range(10):
    for y in range(5):
        btn = tk.Button(frame)
        btn.grid(column=x, row=y, sticky="news")
        tk.Grid.rowconfigure(frame, y, weight=1)
    tk.Grid.columnconfigure(frame, x, weight=1)

root.mainloop()
