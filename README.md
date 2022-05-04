# Audio-Feature-Extraction
Feature extraction of audio signals using librosa package of Python 

Makine öğrenmesi tekniklerinde, modellere verilen girdilerin model tarafından anlaşılabilir bir formata dönüştürülebilmesi için **öznitelik çıkarılması (feature extraction)** gerekmektedir. Bu işleme verilerin *anlamlandırıldığı* bir süreçtir de denilebilir.  

Bu yazımda ses verisi içeren dosyaların özniteliklerinin nasıl ve hangi yöntemler ile çıkarılabileceğini açıklamaya çalıştım.  

Yani bir ses verisini incelediğimiz zaman şunu görebilmekteyiz ki; bu veriler özünde koordinat düzleminde **“zaman, genlik ve frekansın”** temsil edildiği 3 boyutlu sinyallerden başka bir şey değildir. 

SES SİNYALLERİ 
