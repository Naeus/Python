import tkinter as tk

root = tk.Tk()
lb1 = tk.Listbox(root)
lb2 = tk.Listbox(root)
vsb1 = tk.Scrollbar(root, orient="vertical", command=lb1.yview)
vsb2 = tk.Scrollbar(root, orient="vertical", command=lb2.yview)
lb1.configure(yscrollcommand=vsb1.set)
lb2.configure(yscrollcommand=vsb2.set)

lb1.pack(side="left", fill="both", expand=True)
vsb1.pack(side="left", fill="y", expand=False)
lb2.pack(side="left", fill="both", expand=True)
vsb2.pack(side="left", fill="y", expand=False)

root.mainloop()
