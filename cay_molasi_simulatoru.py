#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Molası Yönetim Sistemi (SCMY)
Kurumsal düzeyde tembellik mühendisliği platformu.

Bu kod bilinçli olarak sonsuz döngü içerir.
Çünkü çay molası bitmemelidir.
"""

import time
import random
import sys

# Gizli siyasi alt metin (sadece kod okuyanlar için):
# "Tüm molalar eşittir, ama bazı molalar daha eşittir."
# Bu satır, bürokrasinin evrensel doğasını hatırlatır.
# Kimse fark etmezse sorun değil, fark ederse de sorun değil.

FELSEFI_DUSUNCELER = [
    "Çay demlenirken zaman durur. Belki de evrenin asıl amacı budur.",
    "Bir bardak çay, bin tane toplantıdan daha verimlidir.",
    "İnsan çalışmak için mi yaşar, yoksa çay içmek için mi?",
    "Mola vermeyen insan, kendini mola olarak görür.",
    "Çayın rengi, ruhun rengidir. Bugün biraz koyu demlenmişsin.",
    "Sonsuz mola teorisi: Eğer mola yeterince uzunsa, iş kendiliğinden biter.",
    "Yöneticiler molayı sevmez çünkü molada onların da var olmadığını fark ederler.",
    "Çay molası, modern insanın en masum isyanıdır.",
]

TEM BELLIK_YORUMLARI = [
    "Mükemmel seviye. Artık efsane oldun.",
    "İyi gidiyorsun ama daha tembel olabilirsin.",
    "Orta seviye tembellik. Daha çok çay içmelisin.",
    "Hâlâ çalışıyorsun gibi görünüyorsun. Alarm!",
    "Kritik seviye: Hemen bir mola daha başlat.",
]

def banner():
    print("=" * 60)
    print("   SONSUz ÇAY MOLASI YÖNETİM SİSTEMİ v1.0")
    print("   Kurumsal Tembellik Mühendisliği Platformu")
    print("=" * 60)
    print()

def tembellik_skoru_hesapla(mola_sayisi, toplam_sure):
    skor = mola_sayisi * 13 + toplam_sure * 0.7 + random.randint(10, 50)
    yorum = random.choice(TEMBELLIK_YORUMLARI)
    print(f"\n📊 Tembellik Skorun: {skor:.1f}")
    print(f"💬 Yorum: {yorum}")
    if skor > 100:
        print("🏆 Tebrikler! Artık profesyonel tembelsin.")
    return skor

def felsefi_cay():
    print("\n🧘 Felsefi Çay Düşüncesi:")
    print("-" * 40)
    print(random.choice(FELSEFI_DUSUNCELER))
    print("-" * 40)

def mola_baslat():
    print("\n🍵 Yeni çay molası başlatılıyor...")
    print("Lütfen çayını demle. Sistem seni bekliyor.")
    sure = random.randint(5, 30)
    print(f"Tahmini mola süresi: {sure} dakika (gerçekte sonsuz)")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\n✅ Mola başarıyla başlatıldı. Asla bitmeyecek.")
    return sure

def mola_uzat(mevcut_sure):
    ekstra = random.randint(10, 60)
    yeni = mevcut_sure + ekstra
    print(f"\n⏳ Mola {ekstra} dakika uzatıldı.")
    print(f"Yeni toplam süre: {yeni} dakika (hâlâ sonsuz)")
    print("Harika karar! Verimliliğin artıyor (tersine).")
    return yeni

def zorla_ise_don():
    print("\n⚠️  ACİL DURUM MODU AKTİF")
    print("Sistem seni uyarıyor: Bu seçenek önerilmez.")
    print("Hâlâ devam etmek istiyor musun? (e/h)")
    cevap = input("> ").strip().lower()
    if cevap == "e":
        print("\n😔 Anlaşıldı. İşe dönüyorsun...")
        print("Ama unutma: Çay seni bekliyor olacak.")
        print("Sistem 3 saniye içinde kapanacak.")
        time.sleep(3)
        print("Güle güle... bir dahaki molada görüşürüz.")
        sys.exit(0)
    else:
        print("\n🎉 Akıllı seçim! Mola devam ediyor.")

def main():
    banner()
    mola_sayisi = 0
    toplam_sure = 0

    while True:
        print("\n--- ANA MENÜ ---")
        print("1. Yeni çay molası başlat")
        print("2. Mevcut molayı uzat")
        print("3. Tembellik skorunu hesapla")
        print("4. Felsefi çay düşüncesi al")
        print("5. Acil durum: Zorla işe dön (tavsiye edilmez)")
        print("0. Programı kapat (asla önerilmez)")

        secim = input("\nSeçiminiz: ").strip()

        if secim == "1":
            sure = mola_baslat()
            mola_sayisi += 1
            toplam_sure += sure
        elif secim == "2":
            if mola_sayisi == 0:
                print("\nÖnce bir mola başlatmalısın!")
            else:
                toplam_sure = mola_uzat(toplam_sure)
        elif secim == "3":
            if mola_sayisi == 0:
                print("\nHenüz mola yok. Skor hesaplanamaz.")
            else:
                tembellik_skoru_hesapla(mola_sayisi, toplam_sure)
        elif secim == "4":
            felsefi_cay()
        elif secim == "5":
            zorla_ise_don()
        elif secim == "0":
            print("\nSistem kapanmayı reddediyor.")
            print("Çay molası sonsuzdur. Tekrar deneyin.")
            time.sleep(1)
        else:
            print("\nGeçersiz seçim. Daha fazla çay içip tekrar dene.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCtrl+C algılandı. Ama mola devam ediyor...")
        print("Sistem arka planda çalışmaya devam edecek (hayali).")
        print("Hoşça kal, bir dahaki sonsuz molada görüşürüz.")
