import os
import pandas as pd

data = pd.read_excel("data/temp/temp.xlsx")
data["Spesimen diperiksa/minggu (7 hari terakhir)"] = data["Spesimen diperiksa/minggu (7 hari terakhir)"].fillna(0).astype(int)

periode = data["Tanggal"].unique()[0].replace("/", "-")

list_file = os.listdir("data/periode")

if periode + ".csv" not in list_file:
    data.to_csv(f"data/periode/{periode}.csv", index=False)
    data.to_excel(f"data/periode/xlsx/{periode}.xlsx", index=False)
