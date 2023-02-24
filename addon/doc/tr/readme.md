# Girdi Kilidi #

* Yazar: Jose Manuel Delicado
* NVDA compatibility: 2022.4 and beyond
* [kararlı sürüm][1]ü indir

## Giriş

Evinizde kocuklar veya evcil hayvanınız mı var? Masanıza tırmanmayı seven ve
klavyenizde dolaşmayı seven bir kediniz mi var? Dizüstü bilgisayarınızı
kullanırken yanlışlıkla fareyi ekranın rastgele bölümlerine mi
götürüyorsunuz? O zaman Girdi kilidi tam size göre! Artık Bilgisayarınızı
rahatça kendi haline bırakıp geldiğinizde en son bıraktığınız gibi
bulabileceksiniz.

Kurulduktan sonra, dizüstü bilgisayarınızda klavyenizi, dokunmatik
ekranınızı ve varsa braille ekran ve farenizi kilitleyebilirsiniz.

## Kullanım

Bu eklenti, NVDA'ya Varsayılan olarak atanmamış iki ilave hareket ekler. Bu
yüzden Girdi hareketleri iletişim kutusundan bu hareketleri yapılandırmanız
gerekir. Daha fazla bilgi için NVDA Kullanım Kılavuzunu okuyun.

Girdi kilidi aç/kapa hareketine bastığınızda, NVDA "Girdi kiliti etkin"
diyecektir. Aynı harekete tekrar basana kadar girdi cihazlarınız devre dışı
kalacaktır. Girdi kilitliyken aynı harekete bastığınızda NVDA "Girdi kilidi
devre dışı" diyecek ve cihazlarınız çalışmaya devame decektir.

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
* Bazı dizüstü bilgisayarlarda, fare kilitli olmasına rağmen dokunmatik
  yüzey yine de kullanıcı girişini kabul eder.

## Değişiklik Listesi

### Version 1.11

* En son NVDA sürümleri için uyumluluk güncellemesi.
* Çeviriler güncellendi.
* Now, minimum supported version is 2022.4.

### Sürüm 1.10

* En son NVDA sürümleri için uyumluluk güncellemesi.
* Çeviriler güncellendi.
* dokümantasyon güncellendi.
* Şimdi, desteklenen minimum sürüm 2021.3.
* Bekleme modundan uyandıktan sonra girişler engellenmeye devam
  edecektir. Javi Dominguez'e teşekkürler.

### Sürüm 1.9

* En son NVDA sürümleri için uyumluluk güncellemesi.
* Çeviriler güncellendi.
* dokümantasyon güncellendi.

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

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
