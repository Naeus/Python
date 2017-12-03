#! Python3

import tkinter as tk

root = tk.Tk()
frame=tk.Frame(root)
frame.pack(fill="both", expand=True)

button = tk.Button(frame, text="Kutsal aklın nerde?")
button.pack(fill="both", expand=True)

def resizeEvent(event):
    #button.unbind("<Configure>")

    fontSize = 1
    print(fontSize)

    tempButton = tk.Button(root)

    while (tempButton.winfo_reqwidth() < button.winfo_width() and tempButton.winfo_reqheight() < button.winfo_height()) and fontSize > 0:
        fontSize += 1
        tempButton.configure(text=button.cget('text'), font=("default", fontSize, "normal"))
        print(fontSize)

    while (tempButton.winfo_reqwidth() > button.winfo_width() or tempButton.winfo_reqheight() > button.winfo_height()) and fontSize > 0:
        fontSize -= 1
        tempButton.configure(text=button.cget('text'), font=("default", fontSize, "normal"))
        print(fontSize)

    tempButton.destroy()
    fontSize = max(1, fontSize)

    button.configure(font=("default", fontSize, "normal"))
    #button.bind("<Configure>", resizeEvent)

button.bind("<Configure>", resizeEvent)

print(button.cget('font'))

root.mainloop()
