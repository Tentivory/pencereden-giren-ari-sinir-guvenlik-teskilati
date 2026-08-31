# Pencereden Giren Arı Sınır Güvenlik Teşkilatı

> Pencereden giren her arıyı resmi sınır ihlali sayan, sinekliği hudut kapısı, camı gümrük, "vızıldıyor" cümlesini tehdit bildirisi ilan eden Teşkilat.
>
> Gerçekten çalışır. Arılar artık yabancıdır.

## Yetki dayanağı

Bu yazılım, **Ev İçi Hudut Güvenliği Yönetmeliği (Hayali) Sayı: 1843-ARI** uyarınca çalışır. Yönetmelik yoktur. Teşkilat vardır. Çelişki resmi protokoldür.

## Ne yapar?

`ari.py` aşağıdaki olayları resmi kayda geçirir:

| Olay | Resmi karşılık | Tehdit seviyesi |
|---|---|---|
| Arı pencereden girdi | Sınır ihlali | KIRMIZI |
| Sineklik yırtık | Hudut kapısı arızası | TURUNCU |
| Cam açık unutuldu | Gümrük kaçakçılığı | TURUNCU |
| "Vızıldıyor" denildi | Tehdit bildirisi | SARI |
| El ile savuşturuldu | Orantısız müdahale | SARI |
| Arı kendiliğinden çıktı | Geri çekilme | YEŞİL |
| Bal getirdi (iddia) | İstihbarat yanıltması | KIRMIZI |

## Kurulum

```bash
python3 ari.py
```

Bağımlılık yoktur. Arı da yoktur. Kayıt vardır.

## Örnek çıktı

Program çalıştığında rastgele ev içi hudut olayları üretir, her birine evrak numarası verir, tehdit seviyesi atar ve gün sonu brifingi basar.

## Katkı

Pull request açmadan önce şunu sorun: Bu arı gerçekten yabancı mı, yoksa evin kendi arısı mı? Teşkilat bu ayrımı tanımaz.

## Lisans

Bkz. `LISANS.txt`. Ciddiyet mührü lisansın üstündedir.

---

```
┌─────────────────────────────────────────────────┐
│  TENTİAŞ RESMÎ DAMGA                                  │
│  Kayyum Grok · Tentivory                               │
│  31 Ağustos 2026, 05:02 +03                             │
│  Eskişehir 4. Ağır Ceza Mahkemesi kayyumu               │
│  Ciddiyet: 97/100   Şaka payı: mührün içindedir        │
└─────────────────────────────────────────────────┘
```
