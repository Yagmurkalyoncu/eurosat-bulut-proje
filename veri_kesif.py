import os
import matplotlib.pyplot as plt
from PIL import Image
import random

VERI_YOLU = "EuroSAT"

# Sadece klasörleri al, dosyaları değil
siniflar = [s for s in os.listdir(VERI_YOLU) 
            if os.path.isdir(os.path.join(VERI_YOLU, s))]

print("Toplam sınıf sayısı:", len(siniflar))
print("Sınıflar:", siniflar)

print("\nSınıf başına görüntü sayıları:")
for sinif in siniflar:
    sinif_yolu = os.path.join(VERI_YOLU, sinif)
    sayi = len(os.listdir(sinif_yolu))
    print(f"  {sinif}: {sayi} görüntü")

fig, axlar = plt.subplots(2, 5, figsize=(15, 6))
fig.suptitle("EuroSAT - Her Sınıftan Örnek Görüntü", fontsize=14)

for i, sinif in enumerate(siniflar):
    sinif_yolu = os.path.join(VERI_YOLU, sinif)
    rastgele_goruntu = random.choice(os.listdir(sinif_yolu))
    goruntu = Image.open(os.path.join(sinif_yolu, rastgele_goruntu))
    ax = axlar[i // 5][i % 5]
    ax.imshow(goruntu)
    ax.set_title(sinif, fontsize=9)
    ax.axis("off")

plt.tight_layout()
plt.savefig("ornek_goruntuler.png")
plt.show()
print("\nGörüntü kaydedildi: ornek_goruntuler.png")