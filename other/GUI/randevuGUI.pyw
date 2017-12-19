import data_frame as df
import randevu_oop as ra
import tkinter as tk
from tkinter.font import Font

class Application(tk.Tk):
    def __init__(self, appointments, availables=None):
        super().__init__()

        self.time_select = BookSelection(self, appointments, availables)
        self.time_select.pack(fill='both', expand=True, padx=10, pady=10)
        self.entry = CharLengthEntry(self)
        self.entry.focus_set()
        #self.entry['command'] = 
        self.entry.pack()

class CharLengthEntry(tk.Entry):
    def __init__(self, master, char_len=2):
        super().__init__()
        self.char_len = char_len
        self['justify'] = 'center'
        self['insertontime'] = 0
        self.configure_width()


    def configure_width(self):
        font = Font(font=self['font'])
        self['width'] = font.measure(self.char_len * "0")
        print(self['width'])

class BookSelection(tk.Frame):
    def __init__(self, master, appointments, availables=None):
        super().__init__(master)
        self.appointments = appointments
        self.availables = availables

        self.row_len = 4

        self.create_widgets()
        self.activate_availables()

        self.layout()

    def activate_availables(self):
        if self.availables:
            for time in self.availables:
                for i in range(len(self.appointments)):
                    if time == self.time_select[i]['text']:
                        self.time_select[i]['state'] = 'active'


    def create_widgets(self):
        appointment_times = tuple(self.appointments.keys())

        self.time_select = list()
        self.selection = tk.StringVar()

        for time in appointment_times:
            self.time_select.append(tk.Radiobutton(self, text=time, value=time,
                                                    variable=self.selection,
                                                    state='disabled',
                                                    indicatoron=False))

    def layout(self):
        for i in range(len(self.appointments)):
            row = i//self.row_len
            col = i%self.row_len
            self.time_select[i].grid(row=row, column=col, sticky="nsew")

            self.rowconfigure(row, weight=1)
            self.columnconfigure(col, weight=1)



if __name__ == "__main__":
    saatler = df.saatler
    randevular = df.randevular

    my_appointments = ra.Appointments(saatler, randevular)

    root = Application(my_appointments.appointments, my_appointments.bookable_hours(2))

    root.mainloop()
