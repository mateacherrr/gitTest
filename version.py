class cost:
    def __init__(self,araba,yol):
        self.araba=araba
        self.yol=yol
    def yolHesapla(yol,araba):
         print(f"{araba}  adlı taşıtın geçiş ücreti {yol*3,5} TL' dir.")




ogreci=cost("mercedes",30)

ogreci.yolHesapla



