from datetime import datetime, timedelta
import locale
import json
locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')

data = json.load() #insert database here
hari_ini = datetime.now()

def header():
    print("—"*50)
    print(f"""
    PROGRAM TITLE
    Hari/Tanggal: {hari_ini.strftime("%A, %d/%m/%Y")}
    Waktu       : {hari_ini.strftime("%H:%M:%S")}
    """)
    print("—"*50)

def KegiatanHariIni():
    list_kegiatan = []

