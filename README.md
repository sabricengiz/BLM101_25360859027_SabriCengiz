# BLM101_25360859027_SabriCengiz
Öğrenci Bilgileri : Muhammed Sabri Cengiz   

NO. : 25360859027

Proje Başlığı : Veri Manipülasyonu ve Mantık Kapıları

YouTube linki :


Proje Açıklaması: Kodun ne yaptığı, nasıl çalıştırılacağı (kurulum gerekip gerekmediği) ve kodun 
çalışma mantığının detaylı açıklaması (Markdown formatında). 

# Sanal Mantık Kapısı Simülatörü (Logic Gate Simulator)
Bu proje, Bilgisayar Mimarisi ve Sayısal Tasarım konuları kapsamında, temel mantık kapılarının (AND, OR, XOR, NOT) çalışma prensiplerini simüle etmek amacıyla Python dili kullanılarak geliştirilmiştir.

Program, kullanıcıdan iki adet ikilik (binary) giriş değeri alır, seçilen mantık kapısına göre işlemi gerçekleştirir ve doğruluk tablosuna uygun sonucu ekrana yansıtır.

# Proje Özellikleri
Temel Mantık Kapıları: AND, OR, XOR ve NOT kapılarını destekler.

Giriş Doğrulama (Input Validation): Kullanıcının sadece 0 veya 1 girmesini zorunlu kılar. Harf veya geçersiz sayı girildiğinde program çökmez, uyarı verir.

Sürekli Çalışma Döngüsü: Kullanıcı çıkmak isteyene kadar program sonsuz döngüde çalışır.

Güvenli Çıkış Mekanizması: Herhangi bir adımda çıkış yazılarak program sonlandırılabilir.

Modern Python Yapısı: Python 3.10 ile gelen match-case yapısı kullanılarak kod okunabilirliği artırılmıştır.

# Kodun Çalışma Mantığı
Kod temel olarak üç ana bölümden oluşmaktadır:

1. Giriş Kontrol Modülü (input_al_kontrol_et)
Bu fonksiyon, kullanıcıdan alınan verinin geçerliliğini denetler. Savunmacı Programlama (Defensive Programming) prensibiyle yazılmıştır.

try-except bloğu kullanılarak kullanıcının sayı yerine harf girmesi (ValueError) engellenmiştir.

Girilen sayının sadece [0, 1] listesinde olup olmadığı kontrol edilir.

Kullanıcı çıkış yazdığında özel bir sinyal (CIKIS_SINYALI) döndürerek ana döngünün kırılmasını sağlar.


2. Hesaplama Modülü (mantik_kapisi_hesapla)
Seçilen kapı türüne göre bitsel (bitwise) işlemleri gerçekleştirir. C dilindeki switch-case yapısının Python karşılığı olan match-case kullanılmıştır.

AND (&): Her iki giriş de 1 ise sonuç 1 olur.

OR (|): Girişlerden en az biri 1 ise sonuç 1 olur.

XOR (^): Girişler birbirinden farklıysa sonuç 1 olur.

NOT: Tek girişli bir kapı olduğu için, girilen her iki değerin de tersini (inversion) alarak ekrana yazdırır.

3. Ana Program Döngüsü (Main Loop)
Program while True döngüsü içinde çalışır. Her adımda (1. Giriş, 2. Giriş ve Kapı Seçimi) kullanıcının çıkış yapıp yapmadığı kontrol edilir. Eğer çıkış sinyali gelirse break komutu ile program sonlandırılır.

# Nasıl Çalıştırılır?
Bu projeyi çalıştırmak için bilgisayarınızda Python 3.10 veya daha yeni bir sürümün yüklü olması gerekmektedir ( match-case yapısı gereği).

Repoyu klonlayın veya .py dosyasını indirin.

Terminal veya Komut İstemi'ni açın.

Aşağıdaki komutu çalıştırın:

Bash

python logic_simulator.py
# Örnek Çıktı


Programdan çikmak için herhangi bir adimda 'çıkış' yazabilirsiniz.

------------------------------
1. Girişi (0 veya 1) girin: 1
2. Girişi (0 veya 1) girin: 0
Kapi türünü girin (AND, OR, XOR, NOT): OR
 1 OR 0 = 1
Sonucunuz: 1
------------------------------
1. Girişi (0 veya 1) girin: 5
Lütfen sadece 0 veya 1 giriniz!
1. Girişi (0 veya 1) girin: çıkış
Programdan çikiliyor...

# Geliştirici Notu
Bu proje, bilgisayar mühendisliği eğitimim sürecinde algoritmik düşünme yeteneğimi geliştirmek ve Bitsel Operatörlerin (Bitwise Operators) pratikteki kullanımını kavramak amacıyla hazırlanmıştır.







# Doğruluk Tablosu Simülasyonu (Truth Table Generator)
Bu modül, mantık devreleri dersi kapsamında, 3 değişkenli karmaşık bir mantıksal ifadenin (A AND (B OR C)) davranışını analiz etmek için geliştirilmiştir.Kullanıcıdan veri girişi beklemek yerine, algoritma tüm olası durumları ($2^3 = 8$ ihtimal) otomatik olarak tarar ve sonuçları düzenli bir tablo halinde listeler.

# Modül Özellikleri
Otomatik İterasyon: 3 farklı değişkenin (A, B, C) alabileceği tüm 0 ve 1 kombinasyonlarını iç içe döngülerle üretir.İşlem Önceliği: Mantıksal ifadelerdeki parantez önceliğine (B OR C) dikkat edilerek hesaplama yapılır.Görsel Hizalama: Python'un f-string formatlama yetenekleri kullanılarak, tablonun terminalde kaymadan, nizami bir şekilde görünmesi sağlanmıştır.

# Algoritma Mantığı
Kodun çalışma prensibi şu adımlardan oluşur:
Kombinasyon Üretimi: 3 adet iç içe for döngüsü kullanılarak 000'dan 111'e kadar olan tüm durumlar (Cartesian Product mantığıyla) gezilir.
Parçalı Hesaplama: Karmaşık ifade parçalara bölünür:Önce parantez içi: parantez_ici = B | C (OR İşlemi)Sonra genel sonuç: sonuc = A & parantez_ici (AND İşlemi)
Formatlı Çıktı: Sonuçlar print(f"{degisken:^3}") yapısı ile ortalanarak tabloya yazdırılır.

# Örnek Çıktı

Program çalıştırıldığında terminalde aşağıdaki gibi bir tablo oluşturur:
=============================================
DOĞRULUK TABLOSU SİMÜLASYONU
   İfade: A AND (B OR C)
=============================================
 A  |  B  |  C  | (B OR C) | SONUÇ
---------------------------------------------
 0  |  0  |  0  |    0     |   0  
 0  |  0  |  1  |    1     |   0  
 0  |  1  |  0  |    1     |   0  
 0  |  1  |  1  |    1     |   0  
 1  |  0  |  0  |    0     |   0  
 1  |  0  |  1  |    1     |   1  
 1  |  1  |  0  |    1     |   1  
 1  |  1  |  1  |    1     |   1  
---------------------------------------------
 Tüm olasiliklarla Tablo başariyla oluşturuldu.
# Geliştirici Notu & Kazanımlar
Bu projeyi geliştirirken;İç İçe Döngüler (Nested Loops): Çok değişkenli sistemlerin tüm olasılıklarını tarama mantığını pekiştirdim.String Formatting: Python'da metin hizalama için kullanılan ^ (merkezleme) operatörünü yeni öğrendim ve bu projede uygulayarak terminal çıktılarının daha profesyonel görünmesini sağladım.Bitsel Operatörler: | (OR) ve & (AND) operatörlerinin işlem önceliğiyle kullanımını pratik ettim.


Her türlü geri bildirime ve katkıya açıktır.
