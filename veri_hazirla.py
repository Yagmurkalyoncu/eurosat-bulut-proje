import os
import shutil
import random

KAYNAK = "EuroSAT"
HEDEF = "EuroSAT_kucuk"
SINIF_BASI = 100

siniflar = [s for s in os.listdir(KAYNAK)
            if os.path.isdir(os.path.join(KAYNAK, s))]

for sinif in siniflar:
    kaynak_yol = os.path.join(KAYNAK, sinif)
    hedef_yol = os.path.join(HEDEF, sinif)
    os.makedirs(hedef_yol, exist_ok=True)
    
    dosyalar = os.listdir(kaynak_yol)
    secilen = random.sample(dosyalar, SINIF_BASI)
    
    for dosya in secilen:
        shutil.copy(
            os.path.join(kaynak_yol, dosya),
            os.path.join(hedef_yol, dosya)
        )
    print(f"{sinif}: {SINIF_BASI} goruntu kopyalandi")

print("\nTamamlandi! EuroSAT_kucuk klasoru olusturuldu.")