import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical

# Ayarlar
VERI_YOLU = "EuroSAT"
GORUNTU_BOYUTU = (64, 64)
BATCH_SIZE = 32
EPOCHS = 10

print("Veri yukleniyor...")

# Veriyi yükle
gorseller = []
etiketler = []

siniflar = [s for s in os.listdir(VERI_YOLU)
            if os.path.isdir(os.path.join(VERI_YOLU, s))]

for sinif in siniflar:
    sinif_yolu = os.path.join(VERI_YOLU, sinif)
    dosyalar = os.listdir(sinif_yolu)[:500]  # Her sınıftan 500 görüntü
    for dosya in dosyalar:
        try:
            goruntu = Image.open(os.path.join(sinif_yolu, dosya))
            goruntu = goruntu.resize(GORUNTU_BOYUTU)
            goruntu = goruntu.convert("RGB")
            gorseller.append(np.array(goruntu))
            etiketler.append(sinif)
        except:
            pass

print(f"Toplam goruntu: {len(gorseller)}")

# Numpy dizisine çevir
X = np.array(gorseller, dtype="float32") / 255.0
le = LabelEncoder()
y = le.fit_transform(etiketler)
y = to_categorical(y, num_classes=len(siniflar))

# Eğitim/test ayır
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Egitim: {X_train.shape}, Test: {X_test.shape}")

# CNN modeli
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(64,64,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(128, (3,3), activation="relu"),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dropout(0.4),
    layers.Dense(256, activation="relu"),
    layers.Dense(len(siniflar), activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# Eğit
print("\nModel egitiliyor...")
history = model.fit(
    X_train, y_train,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    validation_data=(X_test, y_test)
)

# Sonuçları kaydet
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"\nTest dogrulugu: %{test_acc*100:.2f}")

# Grafik çiz
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(history.history["accuracy"], label="Egitim")
plt.plot(history.history["val_accuracy"], label="Dogrulama")
plt.title("Model Dogrulugu")
plt.legend()

plt.subplot(1,2,2)
plt.plot(history.history["loss"], label="Egitim")
plt.plot(history.history["val_loss"], label="Dogrulama")
plt.title("Model Kaybi")
plt.legend()

plt.savefig("egitim_grafigi.png")
plt.show()

# Modeli kaydet
model.save("eurosat_model.h5")
print("Model kaydedildi: eurosat_model.h5")