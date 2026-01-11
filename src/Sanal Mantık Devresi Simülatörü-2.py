def dogruluk_tablosu_olustur():
    
    print("\n" + "="*45)
    print("DOĞRULUK TABLOSU SİMÜLASYONU")
    print("   İfade: A AND (B OR C)")
    print("="*45) # Gorsellik; ayırım
    
    # ^ : python da terminalde karakteri ortalar ve o kadar yer kaplar, hizayı saglamak ve estetik icin yeni ögrendim ve uyguladım
    print(f"{'A':^3} | {'B':^3} | {'C':^3} | {'(B OR C)':^8} | {'SONUÇ':^5}")
    print("-" * 45)

    
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                
                # Oncelik Parantez icini hesapla (B OR C)
                parantez_ici = b | c
                
                # Sonra Sonucu hesapla (A AND Parantez)
                sonuc = a & parantez_ici
                
                #  Satırı yazdır 
                print(f"{a:^3} | {b:^3} | {c:^3} | {parantez_ici:^8} | {sonuc:^5}")
    
    print("-" * 45)
    print(" Tüm olasiliklarla Tablo başariyla oluşturuldu.\n")

#fonksiyonu cagıralım
dogruluk_tablosu_olustur()
