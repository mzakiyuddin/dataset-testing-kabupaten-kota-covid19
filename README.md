# Dataset Testing Covid-19 per Kabupaten/Kota di Indonesia

Repository ini memuat data testing covid-19 per kabupaten/kota di seluruh Indonesia.

Data diambil dari Dashboard Kemenkes (https://vaksin.kemkes.go.id/#/sckab -> Testing)

## Cara Kerja

1. Dashboard Kemenkes dibuat dengan Tableau, sehingga untuk menarik datanya perlu menggunakan library [Tableau Scraper](https://github.com/bertrandmartel/tableau-scraping).
2. Dengan script [data_periode.py](/script/data_periode.py), data dari Dashboard Kemenkes disimpan ke folder [periode](/data/periode/).
3. Script [data_periode.py](/script/data_periode.py) dijalankan setiap hari untuk mengupdate data. Script berjalan secara otomatis di atas [Github Action](/.github/workflows/update.yml)
4. Setelah data terkumpuk di folder [periode](/data/periode/), data kemudian disatukan menjadi satu file [master.csv](/data/master.csv) dengan menggunaakn script [data_master.py](/script/data_master.py)
