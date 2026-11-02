# Windows'ta Otomatik Başlatma

Widget'ın her oturum açışınızda otomatik başlamasını istiyorsanız Windows Başlangıç klasörüne bir kısayol ekleyin.

## Adımlar

1. `Win + R` tuşlarına basın, `shell:startup` yazın ve Enter'a basın.
2. Açılan klasörde boş bir yere sağ tıklayıp **Yeni → Kısayol** seçin.
3. Öğenin konumu (hedef) olarak şunu girin:
   ```
   pythonw.exe "C:\tam\yol\phrasal_widget.py"
   ```
4. Kısayola bir ad verin (ör. *Phrasal Verb Widget*) ve kaydedin.

![Başlangıç kısayolu](https://github.com/user-attachments/assets/0f8be085-0ceb-414d-ba20-c60e0504bd23)

Artık widget her oturum açışınızda başlayacaktır.

## İsteğe bağlı: simge ekleme

Kısayola sağ tıklayın → **Özellikler → Simge Değiştir...** → depodaki `phrasal_widget.ico` dosyasını seçin.

## İpuçları

- `pythonw.exe` bulunamıyorsa tam yolunu yazın, örn. `C:\Users\<kullanıcı>\AppData\Local\Programs\Python\Python312\pythonw.exe`. Yolu bulmak için komut isteminde `where pythonw` çalıştırabilirsiniz.
- Otomatik başlatmayı kapatmak için kısayolu Başlangıç klasöründen silmeniz yeterlidir.
