#! Python3

import tkinter as tk
from tkinter.font import Font

def resizeEvent(event, widget):
    widget.unbind("<Configure>")

    widgetFont = Font(font=widget['font'])
    currentWidth = widget.winfo_width()
    currentHeight = widget.winfo_height()

    while ((reqWidth(widgetFont, widget) < currentWidth) and (reqHeight(widgetFont, widget) < currentHeight)) and widgetFont['size'] > 1:
        widgetFont['size'] += 1

    while ((reqWidth(widgetFont, widget) > currentWidth) or (reqHeight(widgetFont, widget) > currentHeight)) and widgetFont['size'] > 1:
        widgetFont['size'] -= 1

    widget['font'] = widgetFont

    widget.bind("<Configure>", lambda event,  widget = widget : resizeEvent(event, widget))

def reqWidth(font, widget):
    return font.measure(widget['text'])

def reqHeight(font, widget):
    return font.metrics("linespace")

def font_resizable(widget, isResizable=True):
    if isResizable:
        widget.bind("<Configure>", lambda event,  widget = widget : resizeEvent(event, widget))

if __name__ == "__main__":

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)
    frame.grid_rowconfigure(0, weight=1, uniform=True)
    frame.grid_rowconfigure(1, weight=1, uniform=True)
    frame.grid_columnconfigure(0, weight=1, uniform=True)

    button = tk.Button(frame, text="Kutsal aklın nerde?")
    button.grid(row=0, column=0, sticky="nsew")

    button1 = tk.Button(frame, text="Durma öyle!")
    button1.grid(row=1, column=0, sticky="nsew")

    font_resizable(button)
    font_resizable(button1)

    root.mainloop()
