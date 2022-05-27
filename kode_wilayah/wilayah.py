import pandas as pd

dagri = pd.read_csv(
    "https://raw.githubusercontent.com/guzfirdaus/Wilayah-Administrasi-Indonesia/master/csv/regencies.csv", sep=";")

dagri["name"] = dagri["name"].str.replace("KAB. ", "")
dagri["name"] = dagri["name"].str.replace("KAB ", "")
dagri["name"] = dagri["name"].str.replace("KOTA ADM. JAKARTA", "KOTA JAKARTA")
dagri["name"] = dagri["name"].str.replace(
    "ADM. KEP. SERIBU", "KEPULAUAN SERIBU")
dagri["name"] = dagri["name"].str.replace(
    "PADANG SIDEMPUAN", "PADANGSIDIMPUAN")
dagri["name"] = dagri["name"].str.replace(
    "KEP. SIAU TAGULANDANG BIARO", "SITARO")

dagri.rename({'province_id': 'dagri_province_id'}, axis=1, inplace=True)
dagri.rename({'id': 'dagri_regency_id'}, axis=1, inplace=True)

data_master = pd.read_csv("data/master.csv")
data_master.rename({'Kabupaten/ Kota': 'name'}, axis=1, inplace=True)

join = pd.merge(data_master, dagri, how="left", on="name")

# join[join["dagri_province_id"].isnull()]

relasi_bps = pd.read_csv(
    "https://raw.githubusercontent.com/zakiego/Kode-Wilayah-Administrasi-Indonesia-Relasi-BPS-Kemendagri/main/csv/kabkota.csv")
relasi_bps.drop(["nama_bps", "nama_dagri"], axis=1, inplace=True)
relasi_bps.rename({'kode_dagri': 'dagri_regency_id',
                  'kode_bps': 'bps_regency_id'}, inplace=True, axis=1)

final = pd.merge(join, relasi_bps, how="left", on="dagri_regency_id")

final.isnull().any()
final.columns.tolist()

final_regencies = final[["name", "bps_regency_id"]]
final_regencies["bps_province_id"] = final_regencies["bps_regency_id"].astype(
    str).str[0:2]
final_regencies = final_regencies.drop_duplicates()
final_regencies.to_csv("kode_wilayah/kode_wilayah.csv", index=False)
