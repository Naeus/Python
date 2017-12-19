import tkinter as tk
from PIL import Image, ImageTk
#required for getting files in a path
import os

class ImageViewer(tk.Label):
    def __init__(self, master, path):
        super().__init__(master)

        self.path = path
        self.image_index = 0

        self.list_image_files()
        self.show_image()

        self.bind('<Button-1>', self.show_next_image)
        self.bind('<Button-3>', self.show_prev_image)

    def list_files(self):
        (_, _, filenames) = next(os.walk(self.path))
        return filenames

    def list_image_files(self):
        self.image_files = list()
        for a_file in self.list_files():
            if a_file.lower().endswith(('.jpg', '.png', '.jpeg')):
                self.image_files.append(a_file)

    def show_image(self):
        img = Image.open(self.path + "\\" + self.image_files[self.image_index])
        self.img = ImageTk.PhotoImage(img)
        self['image'] = self.img

    def show_next_image(self, *args):
        self.image_index = (self.image_index + 1) % len(self.image_files)
        self.show_image()

    def show_prev_image(self, *args):
        self.image_index = (self.image_index - 1) % len(self.image_files)
        self.show_image()

root = tk.Tk()

mypath = r"C:\Users\Public\Pictures\Sample Pictures"
a = ImageViewer(root, mypath)
a.pack()

root.mainloop()
