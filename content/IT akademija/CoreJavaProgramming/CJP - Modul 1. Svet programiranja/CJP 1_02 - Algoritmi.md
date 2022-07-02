title: CJP 1.2. Algoritmi
date: 2021-11-12
tags: programiranje, teorija, algoritmi
summary: Upoznavanje sa algoritmima
description: {summary}
series: Core Java Programming
series_index: 2
lang: sr


[TOC]

-----

{% import "macros.html" as macros %}


::: "Rezime"
    - Kompjuter je uređaj koji je sposoban da izvrši proizvoljan broj aritmetičkih i logičkih operacija. 
    - Program je skup instrukcija koje kompjuteru govore šta je potrebno da uradi. 
    - Proces stvaranja kompjuterskih programa naziva se programiranje. 
    - Kompjuterske programe kreiraju programeri, ljudi koji poseduju neophodna znanja kako bi bili u mogućnosti da kreiraju instrukcije koje diriguju kompjuteru. 
    - Prvim kompjuterskim programerom na svetu smatra se Ada Lovelace. 
    - Mašinski jezik je maternji jezik kompjutera, odnosno jedini jezik koji kompjuter razume. 
    - Asembler, odnosno asemblerski jezik, predstavlja programski jezik niskog nivoa, kod kojeg se osnovne programske naredbe pišu korišćenjem unapred utvrđenih reči, koje simbolizuju naredbu koju predstavljaju. 
    - Mašinski i asemblerski jezik u potpunosti su zavisni od fizičkih osobina procesora na kojima se izvršavaju, te od programera u velikoj meri zahtevaju poznavanje same fizičke arhitekture računara. 
    - Programski jezici višeg nivoa u znatno većoj meri koriste elemente prirodnih jezika, uglavnom reči i skraćenice preuzete iz engleskog jezika, te na taj način unapređuju čitljivost i olakšavaju kreiranje programskog koda.    - Kompajler i interpreter su kompjuterski programi čija je osnovna svrha generisanje drugih kompjuterskih programa. 


## Uvod 

Tokom obavljanja svakodnevnih aktivnosti, svako od nas suočen je sa procesom rešavanja raznih uobičajenih problema i donošenja odluka. Kojim putem ići do posla, šta doručkovati ili ručati, koji mobilni telefon kupiti, kada obaviti renoviranje stana... To su samo neke od situacija koje od nas zahtevaju određenu analizu i razmišljanje u cilju rešavanja konkretnog problema. Naravno, pojam problema je potrebno shvatiti uslovno, kao situaciju, obavezu, prepreku ili pitanje na koje je potrebno pronaći odgovor. Naša svakodnevica u potpunosti je ispunjena takvim situacijama. 

Posao pisanja kompjuterskih programa umnogome podseća na opisane svakodnevne situacije. Zbog toga se veoma često kaže da je programiranje posao koji je sastavljen od konstantnog rešavanja problema korišćenjem kompjutera. Drugim rečima, proizvod programerskog rada, odnosno program, nije ništa drugo do uputstvo računaru kako rešiti određeni problem. Ukoliko kompjuterski program posmatrate kroz prizmu iole složenijih aplikacija, programerski posao sastavljen je iz rešavanja niza takvih pojedinačnih, manjih problema, čije prevazilaženje dovodi do finalnog proizvoda – potpuno funkcionalnog kompjuterskog programa. 

Bez obzira na to da li je reč o situacijama iz svakodnevnog života ili problemima prilikom pisanja kompjuterskih programa, njihovo rešavanje zahteva sprovođenje serije koraka, koji se objedinjeno mogu nazvati algoritam. 


## Šta je algoritam? 

Postoje velike šanse da ste reč algoritam do sada čuli mnogo puta u različitim situacijama. Algoritam se definiše kao ispravno opisana procedura za rešavanje nekog problema, najčešće problema u matematici ili kompjuterskom programiranju. 

**Istorija algoritama** 
Algoritmi nisu nikakva novost, s obzirom na to da su, 3500 godina pre nove ere, drevni Vavilonci posedovali algoritme za računanje kvadratnog korena. Reč algoritam (engl. algorithm) nastala je kao posledica latinizacije imena persijskog naučnika i matematičara Al-Khwarizmija, koji je 825. godine objavio knjigu koja se bavila računanjem korišćenjem hindu brojeva. 

Algoritmi nikako nisu ograničeni isključivo na kompjutere, već se mogu primeniti na svaku situaciju koja iziskuje određenu analizu u cilju iznalaženja rešenja. Na primer, sve one uobičajene situacije iz realnog života navedene na početku ove lekcije mogu biti kandidati za kreiranje algoritama. Tako svi mi, potpuno nesvesno, kreiramo različite algoritme koji nam omogućavaju da razrešimo svakodnevne situacije u kojima se nalazimo. Evo samo nekih takvih situacija. 

Da li poneti kišobran napolje? 
: Pogledati vremensku prognozu; ukoliko je najavljena kiša, poneti kišobran; ukoliko kiša nije prognozirana, ne nositi kišobran. 

Kako napraviti palačinke? 
: Pomešati 300 g brašna, 3 jajeta, 100 ml kisele vode i 400 ml mleka; sjediniti smešu; zagrejati tiganj, sipati i ravnomerno rasporediti smešu; peći oko 2-3 minuta sa obe strane; dodati fil po želji. 

Kako skuvati čaj? 
: Sipati 2 dl vode u lonče i staviti na ringlu; uključiti i sačekati da provri; skloniti lonče sa ringle i dodati čaj. 

Ovo su bile samo neke od situacija čije razrešavanje od nas zahteva kreiranje internih algoritama. Koraci od kojih su sačinjena prikazana uputstva objedinjeni čine proceduru ili, drugim rečima, algoritam, koji opisuje kako konkretnu situaciju razrešiti. Na identičan način funkcionišu i kompjuterski algoritmi. 

**Zbog čega obrađujemo algoritme?** 
Do sada ste se verovatno zapitali koji je razlog obrađivanja algoritama unutar ovog uvodnog izlaganja o osnovama programiranja. Razlog je veoma jednostavan. Pisanje kompjuterskog koda samo je jedan od koraka u kreiranju programa. Pre nego što uistinu i započnu pisanje izvornog koda, programeri obavljaju niz pripremnih radnji, čiji je cilj što preciznije utvrđivanje koraka koji će biti sprovedeni kako bi se napisao kvalitetan i funkcionalan program. Proizvod takvih koraka upravo je algoritam ili više algoritama, koji se zatim koriste kao osnova ili, bolje rečeno, uputstvo za pisanje izvornog koda. 

Svaki dobar programer reći će vam da je posao pisanja algoritama značajniji ili, u najmanju ruku, podjednako značajan kao i posao konkretnog pisanja izvornog koda nekog programa. Upravo zbog toga postoje osobe koje se bave kompjuterskim naukama, čiji je posao isključivo sastavljen od pisanja algoritama. 


## Algoritmi u kompjuterskom svetu 

U ovom trenutku verovatno ne možete ni da naslutite u kojoj meri su algoritmi značajni za funkcionisanje kompjutera i digitalnih tehnologija uopšte. Na primer, čitanje ovoga teksta uopšte ne bi bilo moguće bez postojanja nekoliko veoma moćnih algoritama čije implementacije čine osnovu digitalnog sveta. Logika takvih algoritama koristi se za pretvaranje signala vremenskog domena u frekventni i obrnuto, a na takvim algoritmima se zasniva funkcionisanje interneta, WiFi-ja, rutera, satelita, telefona, kompjutera itd. 

I kada se govori o kompjuterskom programiranju, primarnoj temi ovog programa, može se konstatovati da algoritmi predstavljaju osnovu takvog posla. S obzirom na to da je kompjuter mašina koja obavljanjem velikog broja kalkulacija razrešava probleme, algoritmi bi bili praktični koraci koje bi kompjuter morao izvršiti kako bi proizveo očekivani rezultat. Neke od situacija koje prilikom programiranja zahtevaju kreiranje dobrih algoritama mogle bi biti sledeće: 

- na koji način izračunati srednju vrednost skupa brojeva 
- kako obaviti sortiranje niza podataka 
- kako odrediti poziciju na displeju na kojoj će biti nacrtan neki grafički element 
- na koji način odrediti najkraću putanju između dve tačke na mapi 
- kako generisati slučajnu (engl. random) vrednost 

Ovo su bili samo neki od problema koji mogu nastati prilikom pisanja kompjuterskih programa. Čak i veoma jednostavne aplikacije visokog nivoa kreirane korišćenjem raznih grafičkih alata, koje na svom aplikativnom nivou možda ne zahtevaju kreiranje nijednog algoritma, oslanjaju se u pozadini na veliki broj već napisanih algoritama. Ukoliko se program kreira bilo kojim jezikom nižeg ili višeg nivoa, u procesu prevođenja izvornog koda takvog jezika u mašinski, kompajler, interpreter ili asembler intenzivno koriste različite algoritme. 

Algoritmi kompjuterskog programiranja u potpunosti su nezavisni od programskog jezika, odnosno tehnologije koja će biti korišćena za realizaciju takvih algoritama. Zbog toga je odmah na početku potrebno napraviti razliku između algoritma i izvornog koda nekog programa, koji nastaje kao konkretna realizacija takvog algoritma. Kako biste bolje mogli da vizuelizujete opisani odnos, data je slika 2.1. 

{{ macros.image("/images/CoreJavaProgramming/1_02_01.jpg", "Slika 2.1. Algoritam je uputstvo za kreiranje programa ili nekog njegovog dela") }}

Slika 2.1. pokušava da dočara odnos između algoritma, izvornog koda kojim je napisan program i kompjutera koji takav program izvršava. 


## Različiti načini za predstavljanje algoritama 

Algoritam je samo precizno utvrđeno uputstvo za rešavanje nekog problema, koje u svakoj situaciji, odnosno za bilo koji ulaz, proizvodi očekivani izlaz. Tako je algoritam samo zamisao koja se formira u glavi programera. Da bi se algoritam prezentovao, potrebno je iskoristiti neki od načina koji se u te svrhe koriste. Četiri najčešće korišćena načina za predstavljanje algoritama su: 

- predstavljanje rečima, govorom, engleskim ili nekim drugim jezikom 
- predstavljanje crtanjem dijagrama toka (engl. flowchart) 
- predstavljanje pseudokodom 
- predstavljanje kodom nekog programskog jezika 

Na početku ove lekcije već je definisano nekoliko algoritama, i to korišćenjem prve navedene metode, odnosno korišćenjem nekog od prirodnih jezika. Iako je ovakav vid definisanja i prezentovanja algoritama veoma dobar u situacijama koje iziskuju usmenu ili neobaveznu komunikaciju, kada je kompjutersko programiranje u pitanju, za predstavljanje algoritama najčešće se pribegava korišćenju 2, 3. ili 4. načina. S obzirom na to da ste vi u ovom trenutku na početku učenja programiranja i još uvek ne poznajete nijedan programski jezik, nastavak ovog uvodnog izlaganja biće posvećen predstavljanju algoritama korišćenjem dijagrama toka i pseudokoda. Ove dve metode za vizuelizaciju algoritama predstavljaju odličan alat za upoznavanje osnova programiranja, a početnicima omogućavaju da razviju programersku logiku i pre nego što napišu ijednu liniju koda konkretnog programskog jezika. 

::: question correct="da" answers="da|ne" unique_name="algoritam_u_kodu"
    Da li je moguće algoritam predstaviti korišćenjem programskog jezika C? 


## Dijagram toka 

Dijagram toka jeste jedan od načina na koji je grafički moguće predstaviti korake nekog procesa. Takva grafička predstava ilustruje kompletno rešenje nekog problema, što pomaže u razumevanju načina na koji je takav problem rešen. Dijagrami tokova nisu striktno vezani za kompjutere i programiranje, već poseduju znatno širu primenu. 

Prve dijagrame tokova kreirali su 1921. godine supružnici Frank i Lillian Gilbreth, članovi Američkog društva mehaničkih inženjera (engl. American Society of Mechanical Engineers, ASME). Tako su ovi dijagrami inicijalno korišćeni za opisivanje procesa industrijskog inženjeringa. Ipak, ubrzo su dijagrami tokova svoju primenu našli i u drugim granama nauke, pa je 1949. godine zabeležena njihova prva upotreba u svrhu opisivanja funkcionisanja kompjuterskih programa. Danas se dijagrami tokova prevashodno koriste u industrijskom inženjeringu, kontroli kvaliteta, ekonomiji i kompjuterskim naukama. 

Dijagrami tokova sačinjeni su iz niza grafičkih simbola, koji predstavljaju osnovne gradivne blokove ovakvih dijagrama. Međusobnim povezivanjem takvih simbola na veoma jednostavan način je moguće ilustrovati tok jednog procesa (slika 2.2). 

{{ macros.image("/images/CoreJavaProgramming/1_02_02.jpg", "Slika 2.2. Dijagram toka koji ilustruje proces jedne od svakodnevnih odluka") }}

Slika 2.2. ilustruje primer jednog veoma jednostavnog dijagrama toka, koji predstavlja proces donošenja jedne uobičajene, svakodnevne odluke, spomenute na početku ove lekcije. Možete primetiti da su prilikom formiranja dijagrama sa slike 2.2. korišćeni simboli različitih oblika, koji su međusobno povezani linijama. Naravno, korišćenje prikazanih simbola nije slučajno. Simbole koji se mogu koristiti prilikom kreiranja dijagrama tokova standardizovali su  Američki nacionalni institut za simbole (engl. American National Symbols Institute, ANSI) i Internacionalna organizacija za standardizaciju (engl. The International Organizations for Standardization, ISO). Najznačajniji simboli dijagrama tokova ilustrovani su tabelom 2.1. 

<figure>
<div markdown="1">
| Simbol | Naziv | Opis 
| --- | --- | --- |
| ![Terminal](/images/CoreJavaProgramming/1_02_a_terminal.jpg) | Terminal | Koristi se za predstavljanje početka ili kraja procesa ili nekog potprocesa; ovaj simbol najčešće sadrži tekst Start ili End u zavisnosti od toga da li predstavlja početak ili kraj nekog procesa. |
| ![Operacija](/images/CoreJavaProgramming/1_02_b_operacija.jpg) | Operacija | Predstavlja bilo kakvu operaciju koja kreira, menja, prenosi ili briše podatke, te na taj način utiče na unutrašnje stanje procesa. |
| ![Ulaz/izlaz](/images/CoreJavaProgramming/1_02_c_ulaz-izlaz.jpg) | Ulaz/Izlaz | Simbol kojim se predstavlja unos ili ispis podataka; koristi se u situacijama kada je potrebno modelovati korak koji od korisnika zahteva da unese neke podatke neophodne za funkcionisanje algoritma ili kada je potrebno prikazati izvesne podatke na nekom od izlaznih uređaja (displej, štampač itd.). |
| ![Grananje](/images/CoreJavaProgramming/1_02_d_grananje.jpg) | Grananje | Simbol koji poseduje jednu ulaznu i dve izlazne linije; prilikom jednog prolaska kroz ovaj element dijagrama uvek će biti korišćena samo jedna izlazna linija; osobine ovog elementa mogu se razumeti i analizom njegovog naziva – grananje; ovo je element koji omogućava da tok dijagrama krene jednom od dve ponuđene linije; na taj način se upravo postiže grananje definisano u nazivu ovog simbola. |
| ![Predefinisani proces](/images/CoreJavaProgramming/1_02_e_predefinisani_proces.jpg) | Predefinisani proces | Koristi se da označi neki proces, odnosno skup više koraka, koji se smatra jedinstvenom operacijom; takav proces je unapred definisan na nekom drugom mestu, te se zbog toga naziva predefinisanim; unutar ovog simbola navodi se naziv predefinisanog procesa. |
| ![Linija_toka](/images/CoreJavaProgramming/1_02_f_linija_toka.jpg) | Linija toka | Simbol za povezivanje sukcesivnih koraka dijagrama; podrazumevani tok dijagrama je odozgo nadole i sleva nadesno; ukoliko tok dijagrama odstupa od ovoga standarda, dodaju su strelice na linije toka. |
| ![Konektor](/images/CoreJavaProgramming/1_02_g_konektor.jpg) | Konektor | Simbol kojim se povezuju dve tačke unutar dijagrama kada tako nešto nije moguće postići linijama ili kada se može dobiti jednostavniji prikaz izbegavanjem zbunjujućih isprepletanih linija; s obzirom na to da povezuje dve tačke na dijagramu, ovaj simbol se uvek koristi u parovima sa identičnim oznakama. |
| ![Komentar](/images/CoreJavaProgramming/1_02_h_komentar.jpg) | Komentar | Ukoliko je u dijagram potrebno uključiti neke dodatne informacije, odnosno komentare, koristi se ovaj simbol. |
</div>
<figcaption>Tabela 2.1. Simboli koji se koriste prilikom kreiranja dijagrama tokova</figcaption>
</figure>

Sada kada poznajemo osnovne simbole dijagrama tokova, stečeno znanje možemo iskoristiti za reprezentovanje nekih osnovnih algoritama. Prvi algoritam koji ćemo predstaviti korišćenjem dijagrama toka biće algoritam za sabiranje dva broja. To je jedan od najjednostavnijih algoritama kompjuterskog programiranja. Prirodnim jezikom, odnosno jednostavnim rečima, takav algoritam bi mogao da se opiše na sledeći način: 
prikupi vrednosti prvog i drugog broja, obavi sabiranje takvih brojeva, dobijeni zbir prikaži korisniku ili prosledi na dalju obradu. 

Ovakav algoritam, formulisan prirodnim jezikom, korišćenjem dijagrama toka može se predstaviti kao na slici 2.3. 

{{ macros.image("/images/CoreJavaProgramming/1_02_03.jpg", "Slika 2.3. Algoritam za sabiranje dva broja predstavljen dijagramom toka") }}

Dijagram toka sa slike 2.3. započinje zaobljenim pravougaonikom ili takozvanim terminal simbolom, koji ilustruje početak dijagrama. Unutar njega postavljen je simboličan tekst (START), koji označava da je reč o početku dijagrama. 
Nakon terminal simbola naveden je simbol za ulaz/izlaz, koji se u ovoj situaciji koristi za unos vrednosti. Jednostavno, kako bi se sabiranje obavilo, neophodno je obezbediti sabirke. U ovom trenutku je potpuno nebitno odakle takve vrednosti dolaze, s obzirom na to da je algoritam samo apstrahovani pogled na konkretan problem. U stvarnosti, odnosno unutar nekog kompjuterskog programa, takve vrednosti će obično doći od korisnika ili interne logike same aplikacije. Dva broja koja će biti sabrana, odnosno dva sabirka, unutar dijagrama toka označena su slovima x i y. 
Nakon unosa podataka prelazi se na njihovu obradu, te se zbog toga koristi simbol dijagrama toka koji predstavlja operaciju. Sabiranje je svakako jedan od idealnih kandidata za obeležavanje simbolom operacije. Operacija se sastoji iz sabiranja vrednosti brojeva x i y. Zbir ova dva broja čuva se kao vrednost z. 
Nakon obavljene operacije sabiranja, još jednom se koristi simbol ulaz/izlaz, ali ovog puta u kontekstu izlaza. Kao izlaz, dijagram toka emituje vrednost z, odnosno zbir brojeva x i y. 
Dijagram toka se završava terminal simbolom sa tekstom END, čime se simbolizuje kraj dijagrama toka. 


## Epilog 

Upravo ste po prvi put mogli da vizuelizujete tok jednog jednostavnog algoritma. Za obavljanje takvog posla pomogli su nam dijagrami tokova. Kao što je rečeno, dijagrami tokova su samo jedan od načina na koji je moguće artikulisati algoritme. Stoga je veoma bitno da razumete da dijagrami tokova nisu algoritmi. Oni su samo jedan od načina za njihovo prezentovanje. U narednoj lekciji biće prikazan još jedan način za artikulaciju algoritama, koji predstavlja oblik najsličniji pisanju izvornog koda nekog programskog jezika. Reč je o pseudokodu.
