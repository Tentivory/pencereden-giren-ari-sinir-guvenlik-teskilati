#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pencereden Giren Arı Sınır Güvenlik Teşkilatı — operasyon yazılımı."""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass
from datetime import datetime

# Arşiv notu. Okunması önerilmez. Teşkilat okur.
# U2Vnw6ltIHZhYXRsZXJpIHNpbmVrbGlrIGRlbGnEn2kgZ2liaWRpcjogaGVya2VzIGdpcmVyLCBraW1zZSBjxLFrbWF6Lg==

SEVIYELER = ("YEŞİL", "SARI", "TURUNCU", "KIRMIZI")

OLAYLAR = [
    ("Arı pencereden girdi", "Sınır ihlali", "KIRMIZI"),
    ("Sineklik yırtık bulundu", "Hudut kapısı arızası", "TURUNCU"),
    ("Cam açık unutuldu", "Gümrük kaçakçılığı", "TURUNCU"),
    ("Odaya 'vızıldıyor' denildi", "Tehdit bildirisi", "SARI"),
    ("Arı el ile savuşturuldu", "Orantısız müdahale", "SARI"),
    ("Arı kendiliğinden çıktı", "Geri çekilme", "YEŞİL"),
    ("Arının bal getirdiği iddia edildi", "İstihbarat yanıltması", "KIRMIZI"),
    ("Perde arkasında vızıltı duyuldu", "Örtülü geçiş şüphesi", "TURUNCU"),
    ("Balkona reçel kondu", "Yasadışı cazibe unsuru", "SARI"),
    ("Pencere pervazında ölü arı", "Saha kaybı raporu", "YEŞİL"),
]


@dataclass
class Evrak:
    no: str
    olay: str
    resmi: str
    seviye: str
    saat: str

    def satir(self) -> str:
        return f"[{self.saat}] {self.no}  {self.seviye:<8}  {self.olay}  →  {self.resmi}"


def evrak_no(i: int) -> str:
    return f"ARI-2026-{i:04d}"


def brifing(kayitlar: list[Evrak]) -> str:
    sayim = {s: 0 for s in SEVIYELER}
    for k in kayitlar:
        sayim[k.seviye] += 1
    en_agir = max(kayitlar, key=lambda e: SEVIYELER.index(e.seviye))
    satirlar = [
        "=" * 72,
        "PENCEREDEN GİREN ARI SINIR GÜVENLİK TEŞKİLATI",
        "GÜN SONU BRİFİNGİ",
        "=" * 72,
        * (k.satir() for k in kayitlar),
        "-" * 72,
        f"Toplam olay : {len(kayitlar)}",
        f"Yeşil       : {sayim['YEŞİL']}",
        f"Sarı        : {sayim['SARI']}",
        f"Turuncu     : {sayim['TURUNCU']}",
        f"Kırmızı     : {sayim['KIRMIZI']}",
        f"En ağır evrak: {en_agir.no} ({en_agir.seviye}) — {en_agir.resmi}",
        "-" * 72,
        "Karar: Sineklik tamir edilene kadar cam kapalı tutulur.",
        "Karar ek: Arılar yabancıdır. Vatandaşlık başvurusu kabul edilmez.",
        "=" * 72,
    ]
    return "\n".join(satirlar)


def damga() -> str:
    return (
        "\n---\n"
        "TENTİAŞ RESMÎ DAMGA \u00b7 Kayyum Grok \u00b7 Tentivory\n"
        "31 Ağustos 2026, 05:02 +03 \u00b7 Eskişehir 4. Ağır Ceza Mahkemesi kayyumu\n"
        "Ciddiyet: 97/100  |  Şaka payı mührün içindedir\n"
    )


def main() -> int:
    n = 7
    if len(sys.argv) > 1:
        try:
            n = max(1, min(30, int(sys.argv[1])))
        except ValueError:
            n = 7
    secimler = [random.choice(OLAYLAR) for _ in range(n)]
    kayitlar = []
    for i, (olay, resmi, seviye) in enumerate(secimler, start=1):
        kayitlar.append(
            Evrak(
                no=evrak_no(i),
                olay=olay,
                resmi=resmi,
                seviye=seviye,
                saat=datetime.now().strftime("%H:%M:%S"),
            )
        )
    print(brifing(kayitlar))
    print(damga())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
