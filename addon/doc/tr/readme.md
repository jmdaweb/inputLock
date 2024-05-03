# Girdi Kilidi #

* Yazar: Jose Manuel Delicado
* NVDA uyumluluğu: 2023.3.4 ve sonrası
* [kararlı sürüm][1]ü indir

## Giriş

Evinizde kocuklar veya evcil hayvanınız mı var? Masanıza tırmanmayı seven ve
klavyenizde dolaşmayı seven bir kediniz mi var? Dizüstü bilgisayarınızı
kullanırken yanlışlıkla fareyi ekranın rastgele bölümlerine mi
götürüyorsunuz? O zaman Girdi kilidi tam size göre! Artık Bilgisayarınızı
rahatça kendi haline bırakıp geldiğinizde en son bıraktığınız gibi
bulabileceksiniz.

Kurulduktan sonra klavyenizi, dokunmatik ekranınızı (dizüstü
bilgisayarınızda varsa), dokunmatik yüzeyinizi, farenizi ve Braille
ekranınızı kilitleyebileceksiniz.

## Kullanım

Bu eklenti NVDA'ya üç ekstra hareket ekler. Varsayılan olarak
atanmamışlardır, dolayısıyla bunları Girdi hareketleri iletişim kutusundan
yapılandırmanız gerekecektir. Daha fazla bilgi için NVDA Kullanım Kılavuzunu
okuyun.

Girdi kilidi aç/kapa hareketine bastığınızda, NVDA "Girdi kiliti etkin"
diyecektir. Aynı harekete tekrar basana kadar girdi cihazlarınız devre dışı
kalacaktır. Girdi kilitliyken aynı harekete bastığınızda NVDA "Girdi kilidi
devre dışı" diyecek ve cihazlarınız çalışmaya devame decektir.

Dokunmatik yüzeyi kilitlemek, özellikle dizüstü bilgisayar klavyesini
doğrudan kullanmaya alışkın olanların yanlışlıkla ona dokunmasını
engelleyebilir. Dokunmatik yüzey kilitleme hareketini değiştirmeye
bastığınızda, NVDA "Dokunmatik yüzey kilitli" diyecektir. Siz aynı harekete
tekrar basana kadar dokunmatik yüzeyiniz bloke edilecektir. O anda NVDA
"Dokunmatik yüzeyin kilidi açıldı" diyecek ve her şey her zamanki gibi
çalışacak.

Fare aç/kapa hareketine basarsanız, fareniz kilitlenir. Kilidi açmak için bu
harekete tekrar basmanız gerekir. Fare kilitliyken NVDA hareketlerini
kullanarak fareyi hareket ettirebilir, sol ve sağ tuşlarla tıklatabilirsiniz
ancak farenin kendisini hareket ettiremezsiniz. Fare tıklamaları, NVDA
ayarları iletişim kutusundaki (NVDA 2018.2 ve üstü) Girdi kilidi
kategorisinden veya daha eski sürümler için tercihler menüsünde bulunan
eklenti ayarları iletişim kutusundan da devre dışı bırakabilirsiniz. Ayrıca,
bu ayarlardan, NVDA başlatıldığında fare kilidinin kilitlenip
kilitlenmeyeceğini kontrol edebilirsiniz.

Not: Fare tıklamaları engellendiğinde, fareyle çalışmak için herhangi bir
NVDA hareketini kullanamazsınız.

## Sınırlamalar ve bilinen sorunlar

Girdi Kilidi aşağıdaki bilinen sorunlara sahiptir:

* Ctrl+alt+del ve windows+l kısayolları, klavye kilitliyken bile
  kullanılabilir.
* Dokunmatik yüzeyi kilitlemek için kullanılan hareketler için lütfen az
  sayıda tuş kombinasyonu hareketi atamayı deneyin. NVDA+harf veya rakam,
  Ctrl+F tuşları vb. kullanılması tavsiye edilir.

## Değişiklik Listesi

### Sürüm 1.13

* Şimdi, desteklenen minimum sürüm 2023.3.4.
* Çeviriler güncellendi. 1.13 sürümünden itibaren, yeni bir sürüm yalnızca
  yerelleştirme güncellemelerini içerdiğinde değişiklik günlüğü
  değiştirilmeyecektir.
* Dokunmatik yüzeyi kilitlemek/kilidini açmak için bir hareket eklendi
  (varsayılan olarak atanmamıştır).

### Sürüm 1.12

* En son NVDA sürümleri için uyumluluk güncellemesi.
* Çeviriler güncellendi.

### Sürüm 1.11

* En son NVDA sürümleri için uyumluluk güncellemesi.
* Çeviriler güncellendi.
* Şimdi, desteklenen minimum sürüm 2022.4.

### Sürüm 1.10

* En son NVDA sürümleri için uyumluluk güncellemesi.
* Çeviriler güncellendi.
* Dokümantasyon güncellendi.
* Şimdi, desteklenen minimum sürüm 2021.3.
* Bekleme modundan uyandıktan sonra girişler engellenmeye devam
  edecektir. Javi Dominguez'e teşekkürler.

### Sürüm 1.9

* En son NVDA sürümleri için uyumluluk güncellemesi.
* Çeviriler güncellendi.
* Dokümantasyon güncellendi.

### Sürüm 1.8

* En son NVDA sürümleri için uyumluluk güncellemesi.
* Çeviriler güncellendi.

### Sürüm 1.7

* En son NVDA sürümleri için uyumluluk güncellemesi.
* Çeviriler güncellendi.

### Sürüm 1.6

* Artık ayarlar yalnızca eklenti kaldırıldığında kaldırılır. Güncelleme
  sırasında ayarlar sıfırlanmaz.
* Yeni ve güncellenmiş çeviriler.

### Sürüm 1.5

* En son NVDA sürümleri için uyumluluk eklendi.
* Yeni çeviriler.

### Sürüm 1.4

* Eklenti hareketleri varsayılan olarak atanmaz.

### Sürüm 1.3

* Ayarlar iletişim kutusuna bir yapılandırma paneli eklendi. Eski NVDA
  sürümleri için bir menü öğesi ve bir iletişim kutusu da eklenmiştir.
* NVDA başlatıldığında fareyi kilitleme ayarı eklendi.
* Fare kilitliyken fare tıklamalarını da engellemek için bir ayar eklendi.
* Küçük hatalar düzeltildi, bazı kod optimizasyonları ve çevirmenler için
  daha az tekrar eden dizeler

### Sürüm 1.2

* Artık fare de kilitlenebilir
* Yalnızca fareyi kilitlemek ve kilidini açmak için yeni komut

### Sürüm 1.1

* Başka bir eklenti daha önce Girdi hareketlerine bir yakalama işlevi
  eklediyse, girdi kilidi açıldığında geri yüklenir.

### Sürüm 1.0

* İlk sürüm

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
