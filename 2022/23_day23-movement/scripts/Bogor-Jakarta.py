import pandas as pd
import geopandas as gpd

spasial_jakarta_bogor = gpd.read_file("C:/Users/Ahmad Zaenun Faiz/Desktop/30DaysOfMapChallenge/Day 23 - Movement/data.gpkg", layer='line_bogor_jakarta').set_index('section')
df = pd.read_csv("C:/Users/Ahmad Zaenun Faiz/Desktop/30DaysOfMapChallenge/Day 23 - Movement/data_jadwal/Bogor-Kota.csv")

def variabel(section, sta_awal, sta_akhir):
    nama = df[['NO. KA', sta_awal, sta_akhir]]
    nama['section'] = section
    
    return nama.rename(columns={'NO. KA': 'no', sta_awal: 'berangkat', sta_akhir: 'tiba'})

NC4 = variabel('NC4', 'NMO', 'CBN')
MC20 = variabel('MC20', 'CBN', 'CTA')
BC7 = variabel('BC7', 'BOO', 'CLT')
BC6 = variabel('BC6', 'CLT', 'BJD')
BC8 = variabel('BC8', 'BJD', 'CTA')
MC19 = variabel('MC19', 'CTA', 'DP')
MC9 = variabel('MC9', 'DP', 'DPB')
MC15 = variabel('MC15', 'DPB', 'POC')
MC17 = variabel('MC17', 'POC', 'UI')
MC13 = variabel('MC13', 'UI', 'UP')
MC10 = variabel('MC10', 'UP', 'LNA')
MC12 = variabel('MC12', 'LNA', 'TNT')
MC11 = variabel('MC11', 'TNT', 'PSM')
MC14 = variabel('MC14', 'PSM', 'PSMB')
MC21 = variabel('MC21', 'PSMB', 'DRN')
MC18 = variabel('MC18', 'DRN', 'CW')
MC16 = variabel('MC16', 'CW', 'TEB')
MC9 = variabel('MC9', 'TEB', 'MRI')
MK63 = variabel('MK63', 'MRI', 'CKI')
MK57 = variabel('MK57', 'CKI', 'GDD')
MK62 = variabel('MK62', 'GDD', 'JUA')
MK60 = variabel('MK60', 'JUA', 'SW')
MK59 = variabel('MK59', 'SW', 'MGB')
MK58 = variabel('MK58', 'MGB', 'JAY')
MK57 = variabel('MK57', 'JAY', 'JAKK')
    
bogor_jakarta = pd.concat(
    [NC4,
    MC20,
    BC7,
    BC6,
    BC8,
    MC19,
    MC9,
    MC15,
    MC17,
    MC13,
    MC10,
    MC12,
    MC11,
    MC14,
    MC21,
    MC18,
    MC16,
    MC9,
    MK63,
    MK57,
    MK62,
    MK60,
    MK59,
    MK58,
    MK57]).set_index('section')
    
line_bogor_jakarta = bogor_jakarta.join(spasial_jakarta_bogor, how='left')
clean = line_bogor_jakarta[(line_bogor_jakarta['berangkat'].notna()) & (line_bogor_jakarta['tiba'].notna())]

clean.to_csv("C:/Users/Ahmad Zaenun Faiz/Desktop/30DaysOfMapChallenge/Day 23 - Movement/bogor_jakarta.csv")