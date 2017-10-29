import tkinter as tk

root = tk.Tk()
frame1 = tk.Frame(root)
frame1.grid(row = 0, column =0,sticky = "news")
label1 = tk.Label(frame1, text = "Left", bg="red")
label1.pack(fill="both", expand=True)

frame2 = tk.Frame(root)
frame2.grid(row = 0, column = 1,sticky = "wens")
label2 = tk.Label(master=frame2, text = "Right", bg="blue")
label2.pack(fill="both", expand=True)

tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 1, weight=1)

root.mainloop()
