# Syöttölukko #

* Tekijä: Jose Manuel Delicado
* Yhteensopivuus: NVDA 2023.3.4 ja uudemmat
* Lataa [vakaa versio][1]

## Johdanto

Onko kotonasi lapsia tai lemmikkieläimiä? Onko sinulla kissa, joka pitää
pöydällesi kiipeilystä ja näppäimistölläsi kävelystä? Tuletko vahingossa
siirtäneeksi hiirtä näytöllä satunnaisiin paikkoihin kannettavaa
käyttäessäsi? Ratkaisu näihin kaikkiin on Syöttölukko. Voit huoletta jättää
tietokoneesi käyntiin vartioimattomana.

Kun tämä lisäosa on asennettu, voit lukita näppäimistön, kosketusnäytön
(mikäli kannettavassasi sellainen on), kosketuslevyn, hiiren sekä
pistenäytön.

## Käyttö

Tämä lisäosa lisää NVDA:han kolme pikanäppäintä. Niihin ei ole määritetty
oletusarvoisesti näppäinkomentoja, joten ne on määritettävä
Näppäinkomennot-valintaikkunasta. Katso lisätietoja NVDA:n käyttöoppaasta.

Kun painat syöttölukon tilanvaihtokomentoa, NVDA sanoo "Syöttö
lukittu". Syöttölaitteiden käyttö estetään, kunnes painat uudelleen samaa
komentoa. Silloin NVDA sanoo "Syöttölukko avattu", ja kaikki toimii kuten
tavallisesti.

Kosketuslevyn lukitseminen voi estää sen vahinkokosketukset, erityisesti
sellaisilla käyttäjillä, jotka ovat tottuneet käyttämään kannettavan
tietokoneen näppäimistöä. Kun painat kosketuslevyn lukituksen
tilanvaihtokomentoa, NVDA sanoo "Kosketuslevy lukittu". Kosketuslevyn käyttö
estetään, kunnes painat samaa komentoa uudelleen. Silloin NVDA sanoo
"Kosketuslevyn lukitus avattu", ja kaikki toimii kuten tavallisesti.

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

## Rajoitukset ja tunnetut ongelmat

Syöttölukossa on seuraavia tunnettuja ongelmia:

* Ctrl+Alt+Del- ja Win+L-näppäinkomennot toimivat, vaikka näppäimistö on
  lukittu.
* Käytä kosketuslevyn lukitsevan pikanäppäimen määrittämiseen vain
  muutamasta näppäimestä koostuvaa näppäinkomentoa. Suositeltavaa on käyttää
  NVDA+kirjaimia tai numeroita, Ctrl+F-näppäimiä jne.

## Muutosloki

### Versio 1.13

* Vanhin tuettu versio on nyt 2023.3.4.
* Käännöksiä päivitetty. Versiosta 1.13 lähtien muutoslokia ei enää muokata,
  jos uusi versio sisältää vain käännöspäivityksiä.
* Lisätty pikanäppäin kosketuslevyn lukitsemiselle/lukituksen avaamiselle
  (oletusnäppäinkomentoa ei määritetty).

### Versio 1.12

* Yhteensopivuusliput päivitetty uusimmille NVDA-versioille.
* Käännöksiä päivitetty.

### Versio 1.11

* Yhteensopivuusliput päivitetty uusimmille NVDA-versioille.
* Käännöksiä päivitetty.
* Vanhin tuettu versio on nyt 2022.4.

### Versio 1.10

* Yhteensopivuusliput päivitetty uusimmille NVDA-versioille.
* Käännöksiä päivitetty.
* Dokumentaatiota päivitetty.
* Vanhin tuettu versio on nyt 2021.3.
* Syöte pysyy estettynä valmiustilasta heräämisen jälkeen. Kiitos Javi
  Dominguezille.

### Versio 1.9

* Yhteensopivuusliput päivitetty uusimmille NVDA-versioille.
* Käännöksiä päivitetty.
* Dokumentaatiota päivitetty.

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

* Lisäosan komentoihin ei ole määritelty oletusarvoisesti näppäinkomentoja.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
