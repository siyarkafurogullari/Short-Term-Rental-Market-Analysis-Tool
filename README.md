# Kısa Dönem Kiralama Analiz Aracı — Hızlı Başlangıç

## Kurulum
```bash
pip install -r requirements.txt
streamlit run app.py
```
Tarayıcıda otomatik açılır (genelde http://localhost:8501).

## Kullanım
1. İstediğin şehrin Inside Airbnb verisini indir: http://insideairbnb.com/get-the-data/
   - `listings.csv.gz`
   - `calendar.csv.gz`
2. Uygulamada bu iki dosyayı yükle (gz olarak da yükleyebilirsin, kod otomatik açar — CSV'ye çıkarman gerekmiyorsa doğrudan dene, sorun olursa `gunzip` ile aç).
3. Sol menüden oda tipi ve minimum ilan sayısı filtrelerini ayarla.

## Bu aracı satışa nasıl çevirirsin
1. Bir şehri seç, dashboard'u çalıştır, ekran görüntüsü/kısa ekran kaydı al.
2. O şehirdeki host Facebook gruplarına veya Instagram'daki kısa kiralama yönetim
   hesaplarına şu mesajı gönder:

   > "[Şehir]'deki host'ların fiyat/doluluk trendine baktım, mahallenize özel
   > ücretsiz bir analiz hazırladım. Kaçırdığınız gelir potansiyelini gösteren
   > bir rapor — ister misiniz?"

3. İlgilenen host'a demo'yu göster, "kayıp gelir" rakamını vurgula.
4. Fiyatlandırma:
   - Tek seferlik analiz raporu: $150-250 (ilk müşteriler için)
   - Aylık fiyat optimizasyonu aboneliği: $50-100/ay (tekrarlayan gelir)

## Notlar
- `estimated_occupancy_l365d` ve `estimated_revenue_l365d` alanları Inside Airbnb'nin
  kendi tahmin modelinden gelir; %100 kesin değildir ama tutarlı bir kıyaslama sağlar.
- Calendar dosyasındaki "unavailable" oranı hem gerçek rezervasyonları hem de host'un
  manuel blokladığı günleri içerir — mevsimsellik için yaklaşık bir göstergedir,
  müşteriye sunarken bunu belirt.
