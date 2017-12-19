import pandas as pd
from data import saatler, randevular

#book randevular to saatler, return new saatler
def book_booked_data(saatler, randevular):

    sa_df = pd.DataFrame(saatler)
    ra_df = pd.DataFrame(randevular)
    #book the book df
    pd.options.mode.chained_assignment = None  # default='warn'
    for ra_index, grp_siz, ra_time in ra_df.itertuples():
        sa_index_of_time_match = sa_df.index[sa_df['saat'] == ra_time].tolist()[0]
        sa_df_grp_siz_buffer = sa_df[sa_index_of_time_match:sa_index_of_time_match + grp_siz]

        if (sa_df_grp_siz_buffer['kota'] > 0).all():
            sa_df_grp_siz_buffer['kota'] = sa_df_grp_siz_buffer['kota'].apply(lambda a: a-1)
    pd.options.mode.chained_assignment = 'warn'

    new_saatler = list(sa_df.to_dict('records'))
    return new_saatler

def bookable_hours(saatler, kisi_sayisi):
    sa_df = pd.DataFrame(saatler)
    bookable_hours = list()

    for sa_index, quota, sa_time in sa_df.loc[sa_df['kota'] > 0].itertuples():
        if (sa_df.iloc[sa_index:sa_index + kisi_sayisi]['kota'] > 0).all():
            bookable_hours.append(sa_time)

    return bookable_hours

def musait_saatler(saatler, randevular, kisi_sayisi):
    return bookable_hours(book_booked_data(saatler, randevular), kisi_sayisi)

if __name__ == "__main__":
    print(musait_saatler(saatler, randevular, 2))
