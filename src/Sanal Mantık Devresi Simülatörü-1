def input_al_kontrol_et(mesaj):
    while True:
        giris = input(mesaj)
        
        # ÇIKIŞ KONTROLÜ: Kullanıcı 'çıkış' yazana kadar 1 ve 0 almaya devam edecek
        if giris.lower() == "çıkış":
            return "CIKIS_SINYALI"
            
        try:
            sayi = int(giris)
            if sayi in [0, 1]: 
                return sayi    # Doğru sayıyı yakalayınca geri döndürür. (0 veya 1 dışında bir şey olmasın diye)
            else:
                print("Lütfen sadece 0 veya 1 giriniz!")
        except ValueError:
            print("Hata: Lütfen sayisal bir değer giriniz (veya çikmak için 'çıkış' yazın)!")

def mantik_kapisi_hesapla(kapi_turu, giris1, giris2):
    match kapi_turu.upper(): # .upper() kullanımı   kullanıcı and girse bile AND program anlasın diye kullandım.
        case "AND":
            result = giris1 & giris2
            print(f" {giris1} AND {giris2} = {result}")
            return result
            
        case "OR":
            result = giris1 | giris2
            print(f" {giris1} OR {giris2} = {result}")
            return result
            
        case "XOR":   
            result = giris1 ^ giris2
            print(f" {giris1} XOR {giris2} = {result}")
            return result
            
        case "NOT":
            # NOT işleminde her iki girisin de tersini alıp ekrana yazıyoruz.
            result = 1 if giris1 == 0 else 0 
            result2 = 1 if giris2 == 0 else 0
            print(f" NOT {giris1} = {result}")
            print(f" NOT {giris2} = {result2}")  
            return None # NOT islemi sonuc degiskenine tek bir deger dondurmedigi icin None donuyoruz
            
        case _: # Default durumu (Hatalı gırıs)
            print(" Hata! Geçerli bir kapi giriniz!")
            return None

#ANA PROGRAM DONGUSU
print("Programdan çikmak için herhangi bir adimda 'çıkış' yazabilirsiniz.\n")

while True:
    print("-" * 30) # Görsellik ; ayırma
    
    # A Girisi Al
    A = input_al_kontrol_et("1. Girişi (0 veya 1) girin: ")
    if A == "CIKIS_SINYALI": # Eğer fonksiyon çıkış sinyali gönderdiyse döngüyü kır
        print("Programdan çikiliyor...")
        break

    # B Girisi Al
    B = input_al_kontrol_et("2. Girişi (0 veya 1) girin: ")
    if B == "CIKIS_SINYALI":
        print("Programdan çikiliyor...")
        break

    # Kapı Turunu Al
    gate = input("Kapi türünü girin (AND, OR, XOR, NOT): ")
    if gate.lower() == "çıkış":
        print("Programdan çikiliyor...")
        break

    # Hesapla : Fonksiyonu cagırdık.  Parametreleri girdik.
    sonuc = mantik_kapisi_hesapla(gate, A, B)
    
    if (sonuc != None):
        print("Sonucunuz:", sonuc)
