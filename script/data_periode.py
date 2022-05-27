import os
from tableauscraper import TableauScraper as TS
import pandas as pd

url = "https://dashboard.kemkes.go.id/views/asesmenkabkotavaksinKTP2/Dtesting_kabkota"

ts = TS()
ts.loads(url)

workbook = ts.getWorkbook()

data_crosstab = workbook.getCrossTabData(sheetName='testing')

data = pd.DataFrame(data_crosstab)

periode = data["Tanggal"].unique()[0].replace("/", "-") + ".csv"

list_file = os.listdir("data/periode")

if periode not in list_file:
    data.to_csv(f"data/periode/{periode}", index=False)
