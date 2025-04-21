# X (Twitter) Üzerinden Tweet Siyasi Görüş Tahmini 📊🗣️

## Tweet Verisi Çekerek Siyasi Görüşleri Analiz Etme

Bu proje, X (eski adıyla Twitter) platformundan belirli kriterlere göre tweet verilerini çekmeyi ve bu tweetlerin içerdiği siyasi görüşü veya eğilimi Makine Öğrenmesi tekniklerini kullanarak tahmin etmeyi amaçlayan bir çalışmadır. Kamuya açık sosyal medya verisi üzerinden siyasi söylemin ve eğilimlerin analizi bu projenin temelini oluşturur.

### Projenin Amacı

*   X API'sini kullanmadan ilgili tweet verisini toplamak.
*   Toplanan ham tweet verisi üzerinde kapsamlı bir veri ön işleme ve temizleme süreci uygulamak.
*   Metin verisinden anlamlı özellikler (features) çıkarmak (NLP teknikleri kullanarak).
*   Etiketlenmiş (veya etiketlenecek) veri seti kullanarak Siyasi Görüş Tahmini  için bir Makine Öğrenmesi modeli eğitmek.
*   Eğitilen modelin performansını değerlendirmek.
*   Modeli kullanarak yeni, etiketlenmemiş tweetlerin siyasi görüşlerini tahmin etmek.
*   Sosyal medyadaki siyasi söyleme dair içgörüler elde etmek.

### İçerik ve Kapsam

Bu depo, projenin farklı aşamalarına ait kodları, not defterlerini ve ilgili dosyaları barındırır. Kapsanan ana alanlar şunlardır:

1.  **Veri Çekme (Data Collection):** Belirli anahtar kelimeler, kullanıcılar veya zaman aralıklarına göre tweet toplama scriptleri. *(X API kısıtlamaları ve değişiklikleri dikkate alınmıştır.)*
2.  **Veri Ön İşleme (Data Preprocessing):**
    *   Tweet temizleme (URL'ler, etiketler, emojiler, özel karakterler vb.)
    *   Küçük harfe dönüştürme, noktalama işaretlerini kaldırma.
    *   Stop words (durak kelimeler) ve seyrek kelimelerin kaldırılması.
    *   Tokenizasyon, Stemming/Lemmatization (Gerekirse).
    *   Veri setinin etiketlenmesi (Siyasi görüş kategorileri: Sol, Sağ, Merkez, Nötr veya spesifik parti/aday eğilimleri). *Bu aşama projenin en kritik ve manuel çaba gerektiren kısımlarından biridir.*
3.  **Model Eğitimi (Model Training):**
    *   Farklı sınıflandırma algoritmalarının denenmesi (Örn: Lojistik Regresyon, Destek Vektör Makineleri (SVM), Naive Bayes, Karar Ağaçları, Random Forest, Gradient Boosting veya Basit Derin Öğrenme Modelleri).
    *   Modelin test/doğrulama setleri üzerinde eğitilmesi ve performans metriklerinin hesaplanması.
4.  **Model Değerlendirme (Model Evaluation):**
    *   Accuracy, Precision, Recall, F1-Score, Confusion Matrix gibi metriklerle modelin başarısını ölçme.
    *   Çapraz Doğrulama (Cross-Validation) teknikleri.
5.  **Tahmin ve Analiz (Prediction & Analysis):**
    *   Eğitilen model ile yeni tweetlerin siyasi görüşlerinin tahmin edilmesi.
    *   Tahmin sonuçlarına göre genel siyasi eğilimlere dair temel analizler yapılması.

Proje Sahibi
Süleyman Kürşat Demir

GitHub: https://github.com/demiresaa
LinkedIn: https://www.linkedin.com/in/suleyman-kursat-demir/
