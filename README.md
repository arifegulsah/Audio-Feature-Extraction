# Audio-Feature-Extraction
Feature extraction of audio signals using librosa package of Python 

Makine öğrenmesi tekniklerinde, modellere verilen girdilerin model tarafından anlaşılabilir bir formata dönüştürülebilmesi için **öznitelik çıkarılması (feature extraction)** gerekmektedir. Bu işleme verilerin *anlamlandırıldığı* bir süreçtir de denilebilir.  

Bu yazımda ses verisi içeren dosyaların özniteliklerinin nasıl ve hangi yöntemler ile çıkarılabileceğini açıklamaya çalıştım.  

## SES SİNYALLERİ 

Ses, havanın titreşmesi ve bu titreşimin kulak içine teması sonrasında oluşan bir enerji türüdür. Titreşimler çok farklı frekanslarda ve genliklerde (yani şiddetlerde) olabilmektedir. Bu değerler her ses için farklı ve özeldir. 

Herhangi bir sesin iletilmek veya saklanmak için elektromanyetik enerjiye çevrilmiş haline ise ses sinyali denilmektedir. 

Yani bir ses verisini incelediğimiz zaman şunu görebilmekteyiz ki; bu veriler özünde koordinat düzleminde **“zaman, genlik ve frekansın”** temsil edildiği 3 boyutlu sinyallerden başka bir şey değildir. 

![representative_image](/images/representative.png)



## LIBROSA’YA GİRİŞ 

Bir ses sinyalinin özelliklerinin analizi ve üzerinde işlem yapılabilmesi için Python programlama dilinin sahip olduğu **Librosa** paketinden faydalanacağız.  
```import librosa 
audio_path = 'audio-path' 
x , sr = librosa.load(audio_path) 
print(type(x), type(sr))
```


load() fonksiyonu bir ses dosyasının yüklenmesinde ve dosyanın 1 boyutlu sayısal bir dizine çevrilmesinde kullanılır. “sr” ise sampling rate’in baş harfleridir yani örnekleme hızına tekabül eder. Varsayılan sampling rate 22kHz’tir. Bu değeri değiştirmek veya yok etmek için kodunuzu şu şekilde düzenleyebilirsiniz: 

```librosa.load(audio_path, sr=44100) 
librosa.load(audio_path, sr=none) 
```
Yüklediğiniz ses dosyasını çalıştırmak isterseniz IPython.display ‘den yararlanabilirsiniz. 
```
import IPython.display as ipd 
ipd.Audio(audio_path) 
```
## GÖRSELLEŞTİRME 

### Dalga Grafiği 
```
import matplotlib.pyplot as plt 
import librosa.display 
plt.figure(figsize=(14, 5)) 
librosa.display.waveshow(x, sr=sr) 
```

`librosa.display` ses dosyalarını dalga grafiği, spektrogram veya renk haritası gibi farklı formatlarda görüntüleyebilmemizi sağlar. Dalga grafikleri sesin zamana bağlı olan yüksekliğini resmeder. Spektrogramlar ise zamana bağlı değişen ses genliğini, frekanslarıyla birlikte resmetmektedir. Daha önce de dediğimiz gibi genlik ve frekans her ses için özeldir.  

`librosa.display.waveshow` ile ses dosyamdaki genliğin zamana bağlı değişimini yani dalga grafiğini resmedebildim. Aldığım çıktı şöyle olacaktır. 

![waveplot1_image](/images/waveplot1.png)

### Spektrogram
Spektrogram, zamana göre değiştiği için bir sinyalin frekans spektrumunun görsel bir gösterimidir. Ses sinyallerimiz için spektrogram çizmek istediğimizde; 
```
X = librosa.stft(x) 
Xdb = librosa.amplitude_to_db(abs(X)) 
plt.figure(figsize=(14, 5)) 
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')  
plt.colorbar() 
```

`librosa.stft` fonksiyonu veriyi **Short Term Fourier Transform (STFT)*** formülüne sokar ve düzenler. *STFT*, sinyalimizi, belirli bir zamanda verilen frekansın genliğini bilebileceğimiz yeni şekline dönüştürmeye yarar. Bu işlem ses sinyalleri için zorunlu bir işlemdir.  

`Librosa.display.specshow` ile de görselleştirme işlemini yaptık. Çıktım şu şekilde:  

![SFTF1_image](/images/SFTF1.png)

# ÖZNİTELİK ÇIKARIMI TEKNİKLERİ

## Zero Crossing Rate 
İlk öznitelik çıkarma yöntemimiz Zero Crossing Rate. Bu yöntem bir ses verisinin zman içerisinde yön değiştirme oranını hesaplamaktadır. Yani sinyalin pozitiften negatife geçip geçmediğini ölçer. Dalga grafiğini çizdiğim ses dosyamın tümünü değil 100 dizi ***** 

```
n0 = 9000 
n1 = 9100 
plt.figure(figsize=(14, 5)) 
plt.plot(x[n0:n1]) 
plt.grid() 
```
![ZCR1_image](/images/ZCR1.png)

Zero Crossing Rate’i ölçebilmek için adından da anlaşılabileceği gibi grafiğin sıfır noktalarını kestiği yerleri saymalıyız. Bu grafik için sonuç 16dır. 
Bu işlemi manuel yapmak istemiyorsak,  
```
zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False) 
print(sum(zero_crossings)) 
```
şeklinde sonucu otomatik elde  edebiliriz. 

## Spectral Centroid 

Bu yöntem bir sesin "kütle merkezinin" nerede olduğunu gösterir ve seste bulunan frekansların ağırlıklı ortalaması olarak hesaplanır. Verideki frekanslar baştan sona aynıysa, o zaman spektral ağırlık merkezi bir merkezin etrafında olur ve sesin sonunda yüksek frekanslar varsa, ağırlık merkezi sonuna doğru olur. **** 

```
import sklearn 
spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0] 
spectral_centroids.shape 

frames = range(len(spectral_centroids)) 
t = librosa.frames_to_time(frames) 

def normalize(x, axis=0): 
  return sklearn.preprocessing.minmax_scale(x, axis=axis) 


librosa.display.waveplot(x, sr=sr, alpha=0.4) 
plt.plot(t, normalize(spectral_centroids), color='r') 
```
![SC1_image](/images/SC1.png)

## MFCC — Mel-Frequency Cepstral Coefficients 

Bu özellik, bir ses sinyalinin bir özelliğini çıkarmak için en önemli yöntemlerden biridir ve büyük ölçüde ses sinyalleri üzerinde çalışırken kullanılır. Bir sinyalin mel frekansı cepstral katsayıları (MFCC'ler), bir spektral zarfın genel şeklini kısaca tanımlayan ve genellik 10 ila 20 arasında olan küçük bir özellikler dizisidir.

```
mfccs = librosa.feature.mfcc(x, sr=sr) 
print(mfccs.shape) 
librosa.display.specshow(mfccs, sr=sr, x_axis='time') 
```

librosa.feature.mfcc, bir sinyalin mfcc'lerini hesaplamak için kullanılır. mfccs'nin şeklini yazdırarak, kaç karede kaç mfcc'nin hesaplandığını elde edersiniz. İlk değer, hesaplanan mfcc sayısını temsil eder ve başka bir değer, mevcut çerçevelerin sayısını temsil eder. 

![MFCC1_image](/images/MFCC1.png)
