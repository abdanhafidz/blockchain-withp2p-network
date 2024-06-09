class Mesin:
    def __init__(self,cc:int,tipe:str):
        self.cc = cc
        self.tipe = tipe
class Mobil:
    def __init__(self,namaMobil:str, tahun:int, tipeMesin:Mesin):
        self.Merk = namaMobil
        self.Tahun = tahun
        self.Mesin = "off"
        self.TipeMesin = tipeMesin
        
    def nyalakan_mesin(self):
        self.Mesin = "on"
    def matikan_mesin(self):
        self.Mesin = "off"
TipeMesin = Mesin(2000,"2gd")
MobilKevin = Mobil("Kijang",2005,TipeMesin)
print("Status : ", MobilKevin.Mesin)
MobilKevin.nyalakan_mesin()
print("Status : ", MobilKevin.Mesin)
print("TipeMesin-CC : ", MobilKevin.TipeMesin.cc)
print("TipeMesin-Jenis : ", MobilKevin.TipeMesin.tipe)