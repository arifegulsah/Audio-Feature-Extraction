# Audio-Feature-Extraction
Feature extraction of audio signals using librosa package of Python 

Makine öğrenmesi tekniklerinde, modellere verilen girdilerin model tarafından anlaşılabilir bir formata dönüştürülebilmesi için **öznitelik çıkarılması (feature extraction)** gerekmektedir. Bu işleme verilerin *anlamlandırıldığı* bir süreçtir de denilebilir.  

Bu yazımda ses verisi içeren dosyaların özniteliklerinin nasıl ve hangi yöntemler ile çıkarılabileceğini açıklamaya çalıştım.  

## SES SİNYALLERİ 

Ses, havanın titreşmesi ve bu titreşimin kulak içine teması sonrasında oluşan bir enerji türüdür. Titreşimler çok farklı frekanslarda ve genliklerde (yani şiddetlerde) olabilmektedir. Bu değerler her ses için farklı ve özeldir. 

Herhangi bir sesin iletilmek veya saklanmak için elektromanyetik enerjiye çevrilmiş haline ise ses sinyali denilmektedir. 

Yani bir ses verisini incelediğimiz zaman şunu görebilmekteyiz ki; bu veriler özünde koordinat düzleminde **“zaman, genlik ve frekansın”** temsil edildiği 3 boyutlu sinyallerden başka bir şey değildir. 

![This is an image](/images/representative.png)



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

