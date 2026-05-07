# EuroSAT Uydu Görüntüsü Sınıflandırma Projesi

**3522 Bulut Bilişim Dersi — Final Projesi**

## Proje Hakkında

Bu proje, EuroSAT uydu görüntü veri setini kullanarak arazi örtüsü sınıflandırması yapan bir makine öğrenmesi uygulamasıdır. Model, AWS SageMaker üzerinde eğitilmiş ve tahmin sonuçları AWS DynamoDB'ye kaydedilmiştir.

## Kullanılan Teknolojiler

- **Python** — TensorFlow/Keras, Scikit-learn, Pandas, NumPy
- **Model** — CNN + Transfer Learning (MobileNetV2)
- **Bulut** — AWS S3, AWS SageMaker, AWS DynamoDB
- **Veri Seti** — EuroSAT (27.000 uydu görüntüsü, 10 sınıf)

## Proje Mimarisi

```
EuroSAT Veri Seti
      ↓
AWS S3 (Veri Depolama)
      ↓
AWS SageMaker Notebook (Model Eğitimi)
      ↓
MobileNetV2 CNN Modeli (%73 doğruluk)
      ↓
AWS DynamoDB (Tahmin Sonuçları)
```

## Sınıflandırma Kategorileri

| Sınıf | Açıklama |
|-------|----------|
| AnnualCrop | Tek yıllık tarım arazisi |
| Forest | Orman |
| HerbaceousVegetation | Otlak, çayır |
| Highway | Otoyol, yol |
| Industrial | Sanayi bölgesi |
| Pasture | Mera |
| PermanentCrop | Çok yıllık tarım |
| Residential | Yerleşim alanı |
| River | Nehir |
| SeaLake | Deniz, göl |

## Dosya Yapısı

```
eurosat-proje/
├── veri_kesif.py        # Veri seti keşif ve görselleştirme
├── veri_hazirla.py      # Veri seti küçültme (1000 görüntü)
├── train.py             # CNN model eğitimi (lokal)
├── egitim_grafigi.png   # Model eğitim grafikleri
├── ornek_goruntuler.png # Her sınıftan örnek görüntüler
└── README.md
```

## Model Sonuçları

- **CNN Modeli:** %72.50 doğruluk
- **MobileNetV2 Transfer Learning:** %73 doğruluk
- **Tahmin güven skoru:** %89 - %100

## Kurulum

```bash
pip install tensorflow scikit-learn pandas numpy matplotlib pillow boto3 sagemaker
```

## Çalıştırma

```bash
# Veri keşfi
python veri_kesif.py

# Küçük veri seti oluştur
python veri_hazirla.py

# Model eğitimi
python train.py
```

## AWS Servisleri

- **S3 Bucket:** `eurosat-ml-proje`
- **SageMaker:** Notebook Instance + Model Eğitimi
- **DynamoDB:** `eurosat-tahminler` tablosu

## Veri Seti

EuroSAT veri seti Kaggle üzerinden temin edilmiştir:
https://www.kaggle.com/datasets/apollo2506/eurosat-dataset

## Geliştirici

Yağmur Kalyoncu — 2026
