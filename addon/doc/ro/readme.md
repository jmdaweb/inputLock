# Input Lock #

* Autor: José Manuel Delicado
* NVDA compatibility: 2022.4 and beyond
* Descărcați [versiunea stabilă][1]

## Introducere

Aveți copii sau animale de companie acasă? Aveți o pisică căreia îi place
foarte mult să se suie pe masă și să se plimbe pe tastatură? Mișcați din
greșeală mouse-ul în diferite părți ale ecranului atunci când utilizați
laptop-ul? Atunci Input Lock este pentru dumneavoastră! Veți putea să lăsați
liniștit calculatorul pornit și nesupravegheat fără niciun risc.

Odată instalat, veți putea bloca tastatura sau ecranul tactil dacă laptop-ul
dumneavoastră are unul, mausul și afișajul braille.

## Utilizare

Acest supliment adaugă două gesturi suplimentare la NVDA. Ele sunt
neatribuite în mod implicit, deci va trebui să le configurați din dialogul
gesturilor de intrare. Citiți Ghidul Utilizatorului NVDA pentru mai multe
informații.

Când apăsați pe activarea gestului de blocare a intrării, NVDA va spune
„intrare blocată”. Dispozitivele dumneavoastră de intrare vor fi blocate
până când apăsați aceeași comandă din nou. Din acel moment, totul va merge
ca înainte.

Dacă apăsați pe activarea gestului de blocare a mausului, mausul
dumneavoastră va fi blocat. Apăsați aceeași comandă din nou pentru a-l
debloca. Cât timp mausul este blocat, puteți folosi gesturile NVDA pentru
a-l mișca și pentru a face click cu butoanele stânga și dreapta, dar nu
puteți mișca mausul în sine. Click-urile mausului pot fi dezactivate și din
categoria Input lock, aflată în dialogul setărilor NVDA (NVDA 2018.2 și mai
nou) sau din dialogul setărilor suplimentului pentru versiuni mai vechi,
găsit sub meniul Preferințe. În plus, din aceste setări puteți să controlați
dacă mausul se blochează sau nu atunci când NVDA este pornit.

Notă: Când click-urile mausului sunt blocate, nu puteți utiliza niciun gest
NVDA care să funcționeze cu mausul.

## Limitations and known problems

Input Lock has the following known problems:

* The shortcuts control+alt+del and windows+l can be used even when the
  keyboard is locked.
* On some laptops, the touchpad still accepts user input after mouse is
  blocked.

## Jurnal de modificări

### Version 1.11

* S-a adăugat compatibilitatea cu versiunile recente de NVDA.
* Traduceri actualizate.
* Now, minimum supported version is 2022.4.

### Version 1.10

* S-a adăugat compatibilitatea cu versiunile recente de NVDA.
* Traduceri actualizate.
* Updated documentation.
* Now, minimum supported version is 2021.3.
* The input will remain blocked after waking up from standby mode. Thanks to
  Javi Dominguez.

### Version 1.9

* S-a adăugat compatibilitatea cu versiunile recente de NVDA.
* Traduceri actualizate.
* Updated documentation.

### Versiunea 1.8

* S-a adăugat compatibilitatea cu versiunile recente de NVDA.
* Traduceri actualizate.

### Versiunea 1.7

* S-a adăugat compatibilitatea cu versiunile recente de NVDA.
* Traduceri actualizate.

### Versiunea 1.6

* Acum, setările sunt șterse la dezinstalarea suplimentului. Configurația nu
  mai este resetată la actualizare.
* Traduceri noi și actualizate.

### Versiunea 1.5

* S-a adăugat compatibilitatea cu versiunile recente de NVDA.
* Traduceri noi.

### Versiunea 1.4

* În mod implicit, gesturile suplimentului sunt neatribuite.

### Versiunea 1.3

* S-a adăugat un panou de configurarea în dialogul de setări. Și pentru
  versiunile de NVDA mai vechi au fost adăugate un dialog și un element de
  meniu.
* S-a adăugat o setare pentru blocarea mausului atunci când NVDA este
  pornit.
* S-a adăugat o setare și pentru blocarea clickk-urilor mausului cât timp
  acesta este blocat.
* Erori minore reparate, niște optimizări de cod și string-uri mai puțin
  duplicate pentru traducători

### Versiunea 1.2

* Acum, și mausul poate fi blocat
* Comandă nouă numai pentru blocarea și deblocarea mausului

### Versiunea 1.1

* Dacă un alt supliment a adăugat anterior o funcție de captură la
  inputManager, aceasta este restaurată atunci când intrarea este deblocată.

### Versiunea 1.0

* Versiunea inițială

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
