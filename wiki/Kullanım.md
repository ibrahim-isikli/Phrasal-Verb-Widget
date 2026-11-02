# Kullanım

Widget açıldığında ekranın **sağ üst köşesine** yerleşir (ilk çalıştırmada) ve bir phrasal verb göstermeye başlar:

- **Üst satır:** İngilizce phrasal verb (kalın)
- **Alt satır:** Türkçe anlamı

![Widget](https://github.com/user-attachments/assets/07372513-bd0a-4c44-ba57-c323bf77a33d)

## Kontroller

| İşlem | Klavye | Fare |
|---|---|---|
| Pencereyi taşı | — | Pencerenin herhangi bir yerinden sürükleyin |
| Sonraki fiil | `→` | `▶` düğmesi |
| Önceki fiil | `←` | `◀` düğmesi |
| Otomatik ilerlemeyi duraklat / sürdür | `Space` | `⏸` / `▶` düğmesi |
| Kapat | `Esc` | `✕` düğmesi |

> 💡 Kontrol düğmeleri varsayılan olarak gizlidir; fareyi widget'ın üzerine getirdiğinizde sağ alt köşede belirir.

> ⌨️ Klavye kısayollarının çalışması için widget'ın odakta olması gerekir. Başka bir pencereye geçtiyseniz önce widget'a bir kez tıklayın.

## Davranış ayrıntıları

### Karıştırılmış sıra
Fiiller rastgele bir sırada gösterilir. Listedeki **tüm fiiller bir kez gösterilmeden** hiçbiri tekrar etmez. Liste bitince yeniden karıştırılır ve bir turun son fiilinin bir sonraki turun ilk fiili olmaması sağlanır (art arda aynı fiil görmezsiniz).

### Geri gitme
`←` ile yalnızca **mevcut karıştırma turu içinde** geri gidebilirsiniz. Turun başına ulaştığınızda geri tuşu ilk fiilde kalır.

### Manuel ilerleme ve zamanlayıcı
`→` / `◀` / `▶` ile manuel gezinme otomatik zamanlayıcıyı **sıfırlamaz**; bir sonraki otomatik geçiş kendi planlanan zamanında olur.

### Duraklatma
Duraklatıldığında `⏸` düğmesi `▶` olarak değişir. Duraklatma durumu, pencere kapatıldığında veya taşındığında kaydedilir ve bir sonraki açılışta korunur.

### Konum hafızası
Pencereyi bıraktığınız (sürüklemeyi bitirdiğiniz) anda ve kapatırken konum kaydedilir. Kayıtlı konum ekran dışında kalıyorsa (ör. monitör çıkarıldıysa) widget otomatik olarak sağ üst köşeye geri döner.

Ayar dosyası için bkz. [[Yapılandırma]].
