# Sorun Giderme

### Widget açılmıyor, hiçbir şey olmuyor
`pythonw` hataları gizler. Hatayı görmek için konsoldan çalıştırın:
```
python phrasal_widget.py
```

### `ModuleNotFoundError: No module named 'tkinter'`
Python kurulumunuzda Tk desteği yok.
- **Windows:** Python yükleyicisini yeniden çalıştırın → *Modify* → **tcl/tk and IDLE** seçeneğini işaretleyin.
- **Debian/Ubuntu:** `sudo apt install python3-tk`
- **Fedora:** `sudo dnf install python3-tkinter`
- **macOS (Homebrew):** `brew install python-tk`

### Kendi eklediğim kelimeler görünmüyor
- Widget'ı yeniden başlattınız mı? Liste yalnızca açılışta okunur.
- JSON geçerli mi? Eksik/fazla virgül en sık hatadır. `python phrasal_widget.py` ile çalıştırıp `warning:` mesajı olup olmadığına bakın.
- Her öğede hem `en` hem `tr` alanı var mı? Tek bir hatalı öğe tüm dosyanın reddedilip yedek listenin kullanılmasına neden olur.
- Dosyanın `phrasal_widget.py` ile **aynı klasörde** olduğundan emin olun.

### Türkçe karakterler bozuk görünüyor (`Ã§`, `ÅŸ` vb.)
`phrasal_verbs.json` dosyasını **UTF-8** olarak kaydedin.

### Widget ekranda görünmüyor / kayboldu
Kayıtlı konum ekran dışındaysa widget otomatik olarak sağ üst köşeye döner. Yine de bulamıyorsanız `~/.phrasal_widget/config.json` dosyasını silin veya `x`/`y` değerlerini `-1` yapın.

### Klavye kısayolları çalışmıyor
Widget odakta değildir. Widget'a bir kez tıklayın, ardından tuşları kullanın.

### `interval_seconds` değişikliğim kayboldu
Dosyayı widget açıkken düzenlediyseniz widget kapanırken eski ayarları üzerine yazmış olabilir. Önce widget'ı kapatın, sonra dosyayı düzenleyin. Ayrıca değer **tam sayı** olmalıdır (ondalık kısım yok sayılır).

### Yazı tipi farklı görünüyor (macOS / Linux)
Widget Windows yazı tipi **Segoe UI**'yi kullanır. Bu yazı tipi yoksa Tk varsayılan bir yazı tipine düşer; işlevsellik etkilenmez.

---

Sorununuz burada yoksa bir [issue açın](https://github.com/ibrahim-isikli/Phrasal-Verb-Widget/issues).
