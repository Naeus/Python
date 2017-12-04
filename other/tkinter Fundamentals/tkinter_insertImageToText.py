import tkinter as tk

def add_image():
    text.image_create(tk.END, image = img) # Example 1
    #text.window_create(tk.END, window = tk.Label(text, image = img)) # Example 2

root = tk.Tk()

text = tk.Text(root)
text.pack(padx = 20, pady = 20)

tk.Button(root, text = "Insert", command = add_image).pack()

#img = tk.PhotoImage(file = "64x64.png")

with open("64x64.png", 'rb') as img_file:
    imgData = img_file.read()


#if need embedded data
img = tk.PhotoImage(data = imgData)

'''
if needed embedded image data

run print(imgData)
copy the output to
imgData = [OUTPUT HERE]
'''

root.mainloop()
