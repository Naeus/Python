from data import saatler, randevular

class Appointments:
    def __init__(self, avail_hours, booked_hours=None, is_circular=False):
        self.configurations(avail_hours, booked_hours, is_circular)
        self.book_booked_data()

    # for handling convertions and 'stuff'
    def configurations(self, avail_hours, booked_hours, is_circular):
        self.appointments = self.unwrapper(avail_hours)
        self.appointments_len = len(self.appointments)
        self.appointments_times = tuple(self.appointments.keys())
        self.appointments_quotas = list(self.appointments.values())
        self.booked = None
        if booked_hours:
            self.booked = self.unwrapper(booked_hours, are_values_lists=True)
            #self.booked_times = tuple(self.booked.keys())
            #self.booked_group_sizes = tuple(self.booked.values())
        self.max_quota = sum(self.appointments_quotas)
        self.is_circular = is_circular

    # returns a list of available hours for a given grp_siz
    def bookable_hours(self, grp_siz):
        bookable_hours = list()
        for hour in self.appointments_times:
            if self.is_avail(hour, grp_siz):
                bookable_hours.append(hour)

        return bookable_hours

    # returns the range the book needs to take place from start_i to end_i
    def book_range(self, hour, grp_siz):
        # hour randevu saatinin, saatlerde olduğu index
        start_i = self.appointments_times.index(hour)
        temp_end_i = (start_i + grp_siz)
        # eğer tek seferde saat listesine baştan başlamaya izin verme
        if not self.is_circular:
            # if it's not circular then limit the possible appointment up to len
            end_i = min(temp_end_i, self.appointments_len)
            recurrance = 0
        else:
            end_i = temp_end_i % (self.appointments_len + 1)
            recurrance = grp_siz // self.appointments_len

        return start_i, end_i, recurrance

    #book from booked hours data
    def book_booked_data(self):
        if self.booked:
            for hour, grp_sizes in self.booked.items():
                for grp_siz in grp_sizes:
                    self.book(hour, grp_siz)

    #Returns true if all hours in range start_i to end_i has at least 1 quota
    def is_quota_avail(self, start_i, end_i):
        quota_range = self.appointments_quotas[start_i: end_i]
        if quota_range:
            #eğer hour randevu saatinin, saatlerde olduğu indexten,
            # grp_siz uzağa kadar bakınca randevu kotası mevcutsa
            if(all (i > 0 for i in quota_range)):
                return True
            else:
                return False
        else:
            return False

    # Returns True if the hour is bookable for a group size of grp_siz
    def is_avail(self, hour, grp_siz):
        # update available max quota
        self.max_quota = sum(self.appointments_quotas)

        if self.max_quota >= grp_siz:

            start_i, end_i, recurrance = self.book_range(hour, grp_siz)
            #if self.is_circular is False
            if not self.is_circular:

                if(grp_siz <= (self.appointments_len - start_i)):
                    return self.is_quota_avail(start_i, end_i)
                else:
                    return False
            else:
                return self.is_quota_avail(start_i, end_i)
        else:
            return False

    #books the given hour for the given grp_siz returns False if unavail
    def book(self, hour, grp_siz):
        if self.is_avail(hour, grp_siz):

            start_i, end_i, recurrance = self.book_range(hour, grp_siz)
            #randevuyu onayla ve gerekli kotaları azalt
            for i in range(self.appointments_len):
                self.appointments_quotas[i] -= recurrance
            for i in range(start_i, end_i):
                self.appointments_quotas[i] -= 1
        else:
            return False

    # reformats the date into an easily workable form
    def unwrapper(self, data_list, are_values_lists=False):
        #data_listin birinci elemanının anahtarlarından ilk ikisi
        value_option = tuple(data_list[0].keys())[0]
        key_option = tuple(data_list[0].keys())[1]
        dict_list = list()
        unwrapped_dict = dict()

        for datum in data_list:
            dict_list.append({datum[key_option]:datum[value_option]})

        unwrapped_dict = self.dict_list_to_dict(dict_list, are_values_lists)
        return unwrapped_dict

    # according to https://stackoverflow.com/a/44687752/7032856 since 3.6 regular
    # dictionaries do have order
    def dict_list_to_dict(self, dict_list, are_values_lists):
        dictionary = {}

        for k, v in [(key, d[key]) for d in dict_list for key in d]:

            if are_values_lists:
                if k not in dictionary:
                    dictionary[k]=[v]
                else:
                    dictionary[k].append(v)
            else:
                dictionary[k] = v

        return dictionary

def musait_saatler(saatler, randevular, kisi_sayisi):
    my_bookings = Appointments(saatler, randevular)
    return my_bookings.bookable_hours(kisi_sayisi)

if __name__ == "__main__":
    print(musait_saatler(saatler, randevular, 2))
