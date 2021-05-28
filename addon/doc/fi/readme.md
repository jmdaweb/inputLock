# Syöttölukko #

* Tekijä: Jose Manuel Delicado
* NVDA compatibility: 2017.3 to 2021.1
* Lataa [vakaa versio][1]

## Johdanto

Onko kotonasi lapsia tai lemmikkieläimiä? Onko sinulla kissa, joka pitää
pöydällesi kiipeilystä ja näppäimistölläsi kävelystä? Tuletko vahingossa
siirtäneeksi hiirtä näytöllä satunnaisiin paikkoihin kannettavaa
käyttäessäsi? Ratkaisu näihin kaikkiin on Syöttölukko. Voit huoletta jättää
tietokoneesi käyntiin vartioimattomana.

Kun tämä lisäosa on asennettuna, voit lukita näppäimistön, kosketusnäytön
(mikäli kannettavassasi sellainen on), hiiren sekä pistenäytön.

## Käyttö

Tämä lisäosa lisää NVDA:han kaksi syötekomentoa. Niihin ei ole liitetty
oletusarvoisesti näppäinkomentoja, joten ne on määritettävä
Syötekomennot-valintaikkunasta. Katso lisätietoja NVDA:n käyttöoppaasta.

Kun painat syöttölukon tilanvaihtokomentoa, NVDA sanoo "Syöttö
lukittu". Syöttölaitteiden käyttö estetään, kunnes painat uudelleen samaa
komentoa. Silloin NVDA sanoo "Syöttölukko avattu", ja kaikki toimii kuten
tavallisesti.

Jos painat hiiren käytön estävää tilanvaihtokomentoa, hiiri lukitaan. Paina
samaa komentoa uudelleen avataksesi lukituksen. Kun hiiri on lukittuna, voit
käyttää NVDA-komentoja sen siirtämiseen sekä vasenta ja oikeaa painiketta
napsauttamiseen, mutta itse hiirtä ei voi siirtää. Myös hiiren napsautukset
voidaan poistaa käytöstä NVDA:n asetusvalintaikkunan
Syöttölukko-kategoriasta (NVDA 2018.2 ja uudemmat) tai vanhemmissa
versioissa lisäosan asetusikkunasta, johon pääsee
Asetukset-valikosta. Asetuksista voi lisäksi määrittää, lukitaanko hiiri
NVDA:n käynnistyessä vai ei.

Huom: Kun hiiren napsautukset on estetty, mitkään NVDA:n hiirikomennot eivät
toimi.

## Limitations and known problems

Input Lock has the following known problems:

* The shortcuts control+alt+del and windows+l can be used even when the
  keyboard is locked.
* NVDA unlocks the keyboard and other input methods when the computer wakes
  up from standby mode or the session is restored from the Windows lock
  screen.
* On some laptops, the touchpad still accepts user input after mouse is
  blocked.

## Muutosloki

### Version 1.9

* Yhteensopivuusliput päivitetty uusimmille NVDA-versioille.
* Käännöksiä päivitetty.
* Updated documentation.

### Versio 1.8

* Yhteensopivuusliput päivitetty uusimmille NVDA-versioille.
* Käännöksiä päivitetty.

### Versio 1.7

* Yhteensopivuusliput päivitetty uusimmille NVDA-versioille.
* Käännöksiä päivitetty.

### Versio 1.6

* Asetukset poistetaan nyt vain, kun lisäosa poistetaan. Asetusten
  oletusarvoja ei palauteta päivitettäessä.
* Uusia ja päivitettyjä käännöksiä.

### Versio 1.5

* Lisätty yhteensopivuus viimeisimpien NVDA-versioiden kanssa.
* Uusia käännöksiä.

### Versio 1.4

* Lisäosan syötekomentoihin ei ole määritelty oletusarvoisesti
  näppäinkomentoja.

### Versio 1.3

* Lisätty asetuspaneeli Asetukset-valintaikkunaan. Vanhoja NVDA-versioita
  varten on lisätty valintaikkuna ja sen avaava valikkokohde.
* Lisätty asetus hiiren lukitsemiseksi NVDA:n käynnistyessä.
* Lisätty asetus napsautusten estämiseksi hiiren ollessa lukittuna.
* Pieniä bugeja korjattu, koodia optimoitu ja vähemmän merkkijonojen
  kaksoiskappaleita kääntäjille.

### Versio 1.2

* Nyt myös hiiri voidaan lukita.
* Uusi komento pelkän hiiren lukitsemiseen ja lukituksen avaamiseen.

### Versio 1.1

* Jos toinen lisäosa on aiemmin lisännyt kaappaustoiminnon syötönhallintaan,
  se palautetaan, kun syötön lukitus avataan.

### Versio 1.0

* Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock
