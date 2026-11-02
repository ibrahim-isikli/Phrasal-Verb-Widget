# Kelime Listesi

Gösterilen phrasal verb'ler, uygulama ile aynı klasörde bulunan `phrasal_verbs.json` dosyasından okunur. Depo varsayılan olarak **92 phrasal verb** ile gelir.

## Format

Dosya, her biri `en` (İngilizce) ve `tr` (Türkçe) alanlarına sahip nesnelerden oluşan bir **JSON dizisidir**:

```json
[
  {"en": "make up", "tr": "uydurmak; oluşturmak"},
  {"en": "bring about", "tr": "sebep olmak"},
  {"en": "put up with", "tr": "katlanmak"}
]
```

| Alan | Zorunlu | Açıklama |
|---|---|---|
| `en` | ✅ | Ekranın üst satırında kalın gösterilen İngilizce ifade |
| `tr` | ✅ | Alt satırda gösterilen anlam |

Dosya **UTF-8** kodlamasıyla kaydedilmelidir (Türkçe karakterler için).

## Kendi kelimelerinizi ekleme

1. `phrasal_verbs.json` dosyasını açın.
2. Diziye yeni bir satır ekleyin (önceki satırın sonuna virgül koymayı unutmayın):
   ```json
   {"en": "look forward to", "tr": "dört gözle beklemek"}
   ```
3. Kaydedin ve widget'ı yeniden başlatın — değişiklikler **bir sonraki açılışta** yüklenir.

## İpuçları

- Birden fazla anlamı `;` ile ayırabilirsiniz: `"kurmak; düzenlemek"`.
- Alt satır pencereye göre otomatik kaydırılır, ancak pencere küçük olduğu için anlamları kısa tutmak en iyisidir (yaklaşık iki satır).
- Widget yalnızca phrasal verb'lerle sınırlı değildir; aynı formatla **herhangi bir kelime/ifade listesi** (deyimler, akademik kelimeler, başka diller) kullanabilirsiniz.

## Yedek (gömülü) liste

`phrasal_verbs.json` bulunamazsa, geçersiz JSON içeriyorsa veya bir öğede `en`/`tr` alanı eksikse, widget kodun içine gömülü olan yedek listeyi kullanır. `python phrasal_widget.py` ile çalıştırdığınızda terminalde şuna benzer bir uyarı görürsünüz:

```
warning: ...phrasal_verbs.json is not a valid verb list; using embedded
```

Dosya geçerli ama **boş bir dizi** (`[]`) ise widget `(no data) / (veri yok)` gösterir.
