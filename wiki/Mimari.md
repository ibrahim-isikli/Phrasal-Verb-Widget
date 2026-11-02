# Mimari

Uygulamanın tamamı tek bir dosyadadır: `phrasal_widget.py` (~420 satır). Yalnızca Python standart kütüphanesini kullanır (`json`, `random`, `sys`, `tkinter`, `pathlib`).

## Genel akış

```
__main__
 ├─ load_verbs()     → phrasal_verbs.json (hata olursa EMBEDDED_VERBS)
 ├─ load_config()    → ~/.phrasal_widget/config.json (DEFAULT_CONFIG ile birleştirilir)
 ├─ tk.Tk()
 └─ PhrasalWidget(root, verbs, cfg)
      └─ ShuffleCycle(verbs)
```

## Bileşenler

### Sabitler
| Sabit | Değer | Açıklama |
|---|---|---|
| `WINDOW_W`, `WINDOW_H` | `260`, `70` | Pencere boyutu (piksel) |
| `DEFAULT_INTERVAL_SECONDS` | `15` | Varsayılan geçiş süresi |
| `BG_COLOR` | `#1e1e2e` | Arka plan |
| `EN_COLOR` / `TR_COLOR` | `#e0e0ff` / `#a0a0c0` | Metin renkleri |
| `CONTROL_COLOR` / `CONTROL_HOVER_COLOR` | `#6c7086` / `#cdd6f4` | Düğme renkleri |
| `POSITION_TOLERANCE` | `20` | Ekran görünürlük kontrolü toleransı (piksel) |

Renk paleti [Catppuccin Mocha](https://catppuccin.com/) temasından esinlenmiştir. Görünümü değiştirmek için bu sabitleri düzenlemeniz yeterlidir.

### `load_verbs(path)`
JSON dosyasını okur ve doğrular: kök bir liste olmalı, her öğe `en` ve `tr` anahtarlarına sahip bir sözlük olmalı. `OSError`, `JSONDecodeError` veya doğrulama hatasında `stderr`'e uyarı yazar ve `EMBEDDED_VERBS` döndürür.

### `ShuffleCycle`
Öğeler üzerinde karıştırılmış sırayla dolaşan yineleyici.

- `next()` — sıradaki öğeyi döndürür; tur bitince `_reshuffle()` çağırır.
- `prev()` — mevcut tur içinde bir geri gider; turun başında olduğu yerde kalır.
- `_reshuffle()` — listeyi karıştırır; yeni turun ilk öğesi son gösterilen öğeyle aynıysa onu rastgele başka bir konumla değiştirir (**sınır yumuşatma**).
- Test edilebilirlik için isteğe bağlı bir `random.Random` örneği (`rng`) alır.

### `load_config(path)` / `save_config(path, cfg)`
Ayarları okur/yazar. Okuma sırasında dosya yoksa, bozuksa veya sözlük değilse `DEFAULT_CONFIG` kopyası döner; eksik anahtarlar varsayılanlarla doldurulur. Yazma, gerekirse üst klasörü oluşturur.

### `is_position_visible(x, y, w, h, screen_w, screen_h)`
Kayıtlı pencere konumunun ekran sınırları içinde (±20 px tolerans) olup olmadığını kontrol eder. Değilse widget varsayılan konuma (sağ üst, `x = screen_w - 280`, `y = 40`) yerleşir.

### `PhrasalWidget`
Tkinter arayüzü ve olay işleme.

| Metot | Görev |
|---|---|
| `_setup_window` | Çerçevesiz (`overrideredirect`), her zaman üstte (`-topmost`) pencere; konum hesaplama |
| `_build_ui` | İki etiket (EN/TR), gizli kontrol çubuğu, fare ve klavye bağlamaları |
| `_show` | Etiket metinlerini günceller |
| `_schedule_next` / `_cancel_scheduled` | `root.after` ile otomatik geçiş zamanlayıcısı |
| `_auto_advance` | Sonraki fiili gösterir ve yeniden zamanlar |
| `_manual_next` / `_manual_prev` | Manuel gezinme (zamanlayıcıyı sıfırlamaz) |
| `_toggle_pause` | Duraklat/sürdür, düğme simgesini değiştirir |
| `_on_drag_start/motion/end` | Sürükleyerek taşıma; bırakınca konumu kaydeder |
| `_on_window_enter/leave` | Kontrol çubuğunu göster/gizle |
| `_close` | Konum ve durumu kaydeder, pencereyi kapatır |

> **Not:** Tkinter, fare bir alt bileşene girdiğinde de pencere için `<Leave>` olayı üretir. `_on_window_leave` bu yüzden imlecin gerçekten pencere dışında olup olmadığını koordinatlarla kontrol eder.

## Katkıda bulunma

1. Depoyu fork'layın ve bir dal oluşturun.
2. Değişikliklerinizi `python phrasal_widget.py` ile test edin.
3. Pull request açın.

Yeni phrasal verb eklemek için yalnızca `phrasal_verbs.json` dosyasını düzenlemeniz yeterlidir — bkz. [[Kelime Listesi|Kelime-Listesi]]. Gömülü yedek listeyi (`EMBEDDED_VERBS`) de güncel tutmak isteyebilirsiniz.
