import pandas as pd

data = pd.ExcelFile("iqbal/SITUASI COVID19 KABUPATEN_KOTA - TESTING.xlsx")

test_columns_name = pd.read_excel(
    "data/periode/xlsx/01-07-2022.xlsx").columns.to_list()
test_columns_type = pd.read_excel(
    "data/periode/xlsx/01-07-2022.xlsx").dtypes.to_list()

for sheet in data.sheet_names:
    df = pd.read_excel(data, sheet_name=sheet)

    if df.iloc[1, 1] != True:
        df["Spesimen diperiksa/minggu (7 hari terakhir)"] = df["Spesimen diperiksa/minggu (7 hari terakhir)"].fillna(
            0).astype(int)

        df.rename(columns={'provinsi': 'provinsi (plot_tk_kab)',
                           'Provinsi': 'provinsi (plot_tk_kab)'}, inplace=True)

        print("Test columns", df.columns.to_list() == test_columns_name)
        print("Test format", df.dtypes.to_list() == test_columns_type)

        periode = df.iloc[1, 2].replace("/", "-")
        df.to_csv(f"iqbal/data/{periode}.csv", index=False)
        df.to_excel(f"iqbal/data/xlsx/{periode}.xlsx", index=False)
