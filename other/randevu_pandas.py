import pandas as pd


def book_booked_data(saatler, randevular):
    """ Books the randevular df in saatler df, and returns new available hours in the
    same format as saatler.
    """

    sa_df = pd.DataFrame(saatler)
    ra_df = pd.DataFrame(randevular)

    pd.options.mode.chained_assignment = None       # to ignore overwriting warning
    for ra_index, grp_siz, ra_time in ra_df.itertuples():
        sa_idx_of_time_match = sa_df.index[sa_df['saat'] == ra_time].tolist()[0]
        sa_df_grp_siz_bfr = sa_df[sa_idx_of_time_match:sa_idx_of_time_match + grp_siz]

        if (sa_df_grp_siz_bfr['kota'] > 0).all():
            sa_df_grp_siz_bfr['kota'] = sa_df_grp_siz_bfr['kota'].apply(lambda a: a-1)
    pd.options.mode.chained_assignment = 'warn'     # put it back to default

    new_saatler = list(sa_df.to_dict('records'))    # return an updated list of avail.
    return new_saatler                              # hours in the same format.

def bookable_hours(saatler, kisi_sayisi):
    """ Returns a list of available hours for a group size of kisi_sayisi in saatler.
    """

    sa_df = pd.DataFrame(saatler)
    bookable_hours = list()

    for sa_index, quota, sa_time in sa_df.loc[sa_df['kota'] > 0].itertuples():
        if (sa_df.iloc[sa_index:sa_index + kisi_sayisi]['kota'] > 0).all():
            bookable_hours.append(sa_time)

    return bookable_hours

def musait_saatler(saatler, randevular, kisi_sayisi):
    """ Returns available hours for a group size of kisi_sayisi in saatler given that
    randevular is booked in saatler.
    """

    return bookable_hours(book_booked_data(saatler, randevular), kisi_sayisi)

if __name__ == "__main__":
    try:
        from data import saatler, randevular
    except:
        print("Warning: data.py wasn't found!\n")
        saatler = [
            {'kota': 3, 'saat': '09:00'},
            {'kota': 3, 'saat': '09:20'},
            {'kota': 3, 'saat': '09:40'},
            {'kota': 3, 'saat': '10:00'},
            {'kota': 3, 'saat': '10:20'},
            {'kota': 3, 'saat': '10:40'},
            {'kota': 2, 'saat': '11:00'},
            {'kota': 2, 'saat': '11:20'},
            {'kota': 2, 'saat': '11:40'}
        ]
        randevular = [
            {'kisi_sayisi': 2, 'saat': '10:40'},
            {'kisi_sayisi': 3, 'saat': '09:00'},
            {'kisi_sayisi': 1, 'saat': '11:40'},
            {'kisi_sayisi': 2, 'saat': '11:20'},
            {'kisi_sayisi': 1, 'saat': '09:40'},
            {'kisi_sayisi': 3, 'saat': '09:00'},
            {'kisi_sayisi': 4, 'saat': '10:00'}
        ]
    input(musait_saatler(saatler, randevular, 2))