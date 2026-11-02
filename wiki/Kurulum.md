# Kurulum

## Gereksinimler

| Gereksinim | Not |
|---|---|
| **Python 3.12+** | [python.org](https://www.python.org/downloads/) üzerinden indirilebilir |
| **tkinter** | Windows ve macOS Python kurulumlarında varsayılan olarak gelir |
| Ek paket | **Yok** — `pip install` gerekmez |

> **Linux kullanıcıları:** Bazı dağıtımlarda `tkinter` ayrı bir paket olarak gelir. Örneğin Debian/Ubuntu için:
> ```
> sudo apt install python3-tk
> ```

## Projeyi indirme

```
git clone https://github.com/ibrahim-isikli/Phrasal-Verb-Widget.git
cd Phrasal-Verb-Widget
```

Alternatif olarak GitHub sayfasındaki **Code → Download ZIP** ile indirip bir klasöre çıkarabilirsiniz.

## Dosyalar

| Dosya | Açıklama |
|---|---|
| `phrasal_widget.py` | Uygulamanın tamamı (tek dosya) |
| `phrasal_verbs.json` | Gösterilen phrasal verb listesi (92 adet) |
| `phrasal_widget.ico` | Kısayollar için uygulama simgesi |

## Çalıştırma

### Normal kullanım (konsol penceresi olmadan — Windows)

```
pythonw phrasal_widget.py
```

`pythonw` (sonunda **w** ile) Windows'ta uygulamayı arkada bir konsol penceresi açmadan çalıştırır.

### Hata ayıklama

```
python phrasal_widget.py
```

Bu şekilde çalıştırdığınızda, örneğin kelime listesi yüklenemediğinde verilen `warning: ...` mesajları terminalde görünür.

### macOS / Linux

```
python3 phrasal_widget.py
```

Sonraki adım: [[Kullanım]]
