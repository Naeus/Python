import tkinter as tk

root = tk.Tk()

text = tk.Text(root)
text.pack()

text.insert('end', "This text is non-elided.")
text.tag_add('mytag', '1.13', '1.17')
text.tag_config('mytag', elide=True)

def toggle_elision():
    # cget returns string "1" or "0"
    if int(text.tag_cget('mytag', 'elide')):
        text.tag_config('mytag', elide=False)

    else:
        text.tag_config('mytag', elide=True)


tk.Button(root, text="Toggle", command=toggle_elision).pack()

root.mainloop()
