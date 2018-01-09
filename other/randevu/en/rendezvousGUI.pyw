import tkinter as tk
from tkinter import ttk
import pandas as pd
import rendezvous_pandas as rd_pd


class Rendezvous(tk.Tk):
    """ Produces a GUI with time schedule, group size selector, and a booking button.
    """

    def __init__(self, schedule, appointments=None):
        super().__init__()
        self.title("Rendezvous")
        self.resizable(False, False)
        self._s = schedule
        self.a = appointments
        self._grp_siz = 0
        self._max_grp_siz = self.maximum_available_group_size(self._s, self.a)
        _s_df = pd.DataFrame(self._s)
        self._s_df_time_col = _s_df.columns.tolist()[1]
        self._sched_times = _s_df[self._s_df_time_col].tolist()

        
        self._create_widgets()
        self._display_widgets()
        self._update_schedule()

    def update(self):
        """ Updates entire GUI with the latest self.a.
        """
        
        self._max_grp_siz = self.maximum_available_group_size(self._s, self.a)
        self._group_size_frame.max_value = self._max_grp_siz
        self._group_size_frame.max_value_update()
        self._update_schedule()

    def _create_widgets(self):
        self._schedule = Schedule(self, self._sched_times, self._grp_siz)
        self._group_size_frame = GroupSize(self, self._max_grp_siz)
        self._group_size_frame.selector.bind("<<ComboboxSelected>>",
                                            self._update_schedule)
        self._book_btn = tk.Button(self, text="Book", command=self.book)

    def _display_widgets(self):
        self._schedule.pack()
        self._group_size_frame.pack()
        self._book_btn.pack(side='right', padx=4, pady=4)

    def _update_schedule(self, *event):
        """ Updates the time schedule based on the selected group size and self.a.
        """

        self._schedule.selected_time.set("")
        self._grp_siz = int(self._group_size_frame.selector.get())
        self._schedule.grp_siz = self._grp_siz
        _avail_times = rd_pd.avail_times_for_a_grp_siz(self._s, self.a, self._grp_siz)
        self._schedule.sel_range_update()

        for btn in self._schedule.time_table:
            if btn['value'] in _avail_times:
                btn['state'] = 'normal'
            else:
                btn['state'] = 'disabled'

    def book(self):
        """ Updates self.a and entire GUI based on it, if a booking's been made.
        """

        _selected_time = self._schedule.selected_time.get()

        if _selected_time:
            if self.a:
                _a_df = pd.DataFrame(self.a)
                new_appointment_df = pd.DataFrame([[self._grp_siz, _selected_time]],
                                                    columns=_a_df.columns.tolist())
                _a_df = _a_df.append(new_appointment_df)
            else:
                _a_df = pd.DataFrame([[self._grp_siz, _selected_time]],
                                                    columns=['col1', 'col2'])

            self.a = list(_a_df.to_dict('records'))     # can be easily exported
            self.update()

    @staticmethod
    def maximum_available_group_size(schedule, appointments):
        """ Returns the maximum available group size. 
        """

        _max_grp_siz = 1
        while rd_pd.avail_times_for_a_grp_siz(schedule, appointments, _max_grp_siz):
            _max_grp_siz += 1
            if _max_grp_siz > 9:
                break
        _max_grp_siz -= 1
        return _max_grp_siz


class Schedule(tk.LabelFrame):
    """ Produces a schedule with the items in sched_times.
    """

    def __init__(self, master, sched_times, grp_siz):
        super().__init__(master)
        self['text'] = "Schedule"
        self.grp_siz = grp_siz
        self.selected_time = tk.StringVar()
        self.time_table = list()
        self._row_len = 4

        for i, time in enumerate(sched_times):
            self.time_table.append(tk.Radiobutton(self, text=time, value=time,
                                                    variable=self.selected_time,
                                                    indicatoron=False,
                                                    state='disabled'))
            self.time_table[i]['command'] = lambda a=i: self.sel_range_update(a)
            self.time_table[i].grid(row=i // self._row_len,
                                    column=i % self._row_len,
                                    sticky='nsew')


    def sel_range_update(self, btn_num=None):
        """ Updates 'selected' status of appointment buttons, selects a range of time
        based on the self.grp_siz.
        """

        _select_range = list()
        for i, btn in enumerate(self.time_table):
            btn['offrelief'] = 'raised'
            if btn_num == i:
                for j in range(1, self.grp_siz):
                    _select_range.append(i + j)
                    
        for item in _select_range:  # 1.    needed to separate this from above loop
                                    #       for no apparent reason.
            self.time_table[item]['offrelief'] = 'sunken'
                    

class GroupSize(tk.LabelFrame):
    """ Produces a frame that lets the user to select the group size for an
    appointment.
    """

    def __init__(self, master, max_value=None):
        super().__init__(master)
        self['text'] = "Group Size"
        self.var = tk.IntVar()
        self.selector = ttk.Combobox(self, state='readonly', textvariable=self.var)
        self.selector.pack(fill='both', expand=True)
        self.max_value = max_value
        self.max_value_update()

    def max_value_update(self):
        """ Updates the select values based on self.max_value.
        """

        if self.max_value:
            _values = list()
            for i in range(self.max_value):
                _values.append(i+1)
            self.selector['values'] = _values
            self.var.set(self.selector['values'][0])


if __name__ == '__main__':
    try:
        from data2 import free_schedule, appointments
    except:
        sub_root = tk.Tk()
        tk.Label(sub_root, text="Warning: data2.py wasn't found!").pack()
        sub_root.after(3000, sub_root.destroy)
        sub_root.mainloop()
        free_schedule = [
            {'quota': 3, 'time': '09:00'},
            {'quota': 3, 'time': '09:20'},
            {'quota': 3, 'time': '09:40'},
            {'quota': 3, 'time': '10:00'},
            {'quota': 3, 'time': '10:20'},
            {'quota': 3, 'time': '10:40'},
            {'quota': 2, 'time': '11:00'},
            {'quota': 2, 'time': '11:20'},
            {'quota': 2, 'time': '11:40'}
        ]
        appointments = [
            {'number_of_people': 2, 'time': '10:40'},
            {'number_of_people': 3, 'time': '09:00'},
            {'number_of_people': 1, 'time': '11:40'},
            {'number_of_people': 2, 'time': '11:20'},
            {'number_of_people': 1, 'time': '09:40'},
            {'number_of_people': 3, 'time': '09:00'},
            {'number_of_people': 4, 'time': '10:00'}
        ]

    root = Rendezvous(free_schedule)
    root.mainloop()