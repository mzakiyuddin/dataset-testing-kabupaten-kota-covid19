# https://sparkbyexamples.com/pandas/pandas-read-multiple-csv-files/

import pandas as pd
import glob

path = "data/periode"
csv_files = glob.glob(path + "/*.csv")

df_list = (pd.read_csv(file) for file in csv_files)

big_df = pd.concat(df_list, ignore_index=True)

big_df.sort_values(by=["provinsi (plot_tk_kab)",
                   "Kabupaten/ Kota"], inplace=True)

big_df.to_csv("data/master.csv", index=False)

# combine with kode_wilayah

kode_wilayah = pd.read_csv("kode_wilayah/kode_wilayah.csv")

big_df.rename({"Kabupaten/ Kota": "name"}, inplace=True, axis=1)

big_df_with_id = pd.merge(big_df, kode_wilayah, on="name", how="left")

big_df_with_id = big_df_with_id[big_df_with_id.columns[[
    2, 1, 12, 0, 11, 3, 4, 5, 6, 7, 8, 9, 10]]]

big_df_with_id.to_csv("data/master_with_id.csv", index=False)
