# https://sparkbyexamples.com/pandas/pandas-read-multiple-csv-files/

import pandas as pd
import glob

# Data Path
path = "data/periode"

# Get All Filename
csv_files = glob.glob(path + "/*.csv")
df_list = (pd.read_csv(file) for file in csv_files)

# Read All File
big_df = pd.concat(df_list, ignore_index=True)

big_df["Tanggal"] = pd.to_datetime(big_df["Tanggal"], format='%d/%m/%Y')

# Sort by date, province, kab/kota
big_df.sort_values(by="Tanggal", inplace=True)
big_df.sort_values(by=["provinsi (plot_tk_kab)",
                   "Kabupaten/ Kota"], inplace=True)

# Save Data to master.csv
big_df.to_csv("data/master.csv", index=False)

# Combine with kode_wilayah
kode_wilayah = pd.read_csv("kode_wilayah/kode_wilayah.csv")

# Rename column `Kabupaten/ Kota` to `name`
big_df.rename({"Kabupaten/ Kota": "name"}, inplace=True, axis=1)

# Merge column big_df with kode_wilayah
big_df_with_id = pd.merge(big_df, kode_wilayah, on="name", how="left")

# Change Order Column
big_df_with_id = big_df_with_id[big_df_with_id.columns[[
    2, 1, 12, 0, 11, 3, 4, 5, 6, 7, 8, 9, 10]]]

# Save master_with_id.csv
big_df_with_id.to_csv("data/master_with_id.csv", index=False)
