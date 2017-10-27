#! Python3

import tkinter as tk

root = tk.Tk()
frame=tk.Frame(root)
frame.pack(fill="both", expand=True)

button = tk.Button(frame, text="Kutsal aklın nerde?")
button.pack(fill="both", expand=True)

def resizeEvent(event):
    fontSize = int(min((event.height//3), event.width * 1.5 / len(button.cget("text"))))
    button.configure(font=("default", fontSize, "normal"))
    print(fontSize)

button.bind("<Configure>", resizeEvent)

root.mainloop()
