# Yapılandırma

Widget ayarlarını kullanıcı klasörünüzdeki bir JSON dosyasında saklar:

| İşletim sistemi | Konum |
|---|---|
| Windows | `C:\Users\<kullanıcı>\.phrasal_widget\config.json` |
| macOS / Linux | `~/.phrasal_widget/config.json` |

Dosya, widget'ı ilk kez taşıdığınızda veya kapattığınızda otomatik olarak oluşturulur.

## Ayarlar

```json
{
  "x": 1640,
  "y": 40,
  "interval_seconds": 15,
  "paused": false
}
```

| Anahtar | Tür | Varsayılan | Açıklama |
|---|---|---|---|
| `interval_seconds` | tam sayı | `15` | Otomatik geçişler arası süre (saniye) |
| `x` | tam sayı | `-1` | Pencerenin sol kenarının ekran koordinatı. `-1` = varsayılan konum (sağ üst) |
| `y` | tam sayı | `-1` | Pencerenin üst kenarının ekran koordinatı. `-1` = varsayılan konum |
| `paused` | mantıksal | `false` | `true` ise widget duraklatılmış olarak açılır |

## Geçiş süresini değiştirme

1. Widget'ı kapatın (`Esc`).
2. `config.json` dosyasını bir metin editörüyle açın.
3. `"interval_seconds"` değerini istediğiniz saniyeye ayarlayın, örn. `30`.
4. Kaydedip widget'ı yeniden başlatın.

> ⚠️ Widget kapanırken ayarları dosyaya yazar. Dosyayı widget **açıkken** düzenlerseniz değişiklikleriniz kapanışta üzerine yazılabilir. Bu yüzden önce kapatın.

## Konumu sıfırlama

`x` ve `y` değerlerini `-1` yapın veya `config.json` dosyasını silin. Widget bir sonraki açılışta sağ üst köşede başlar.

## Hatalı dosya

Dosya bozuksa (geçersiz JSON) veya eksik anahtarlar içeriyorsa widget çökmez; eksik değerler için varsayılanları kullanır.
