title: AJP 1.6. Dizajn šabloni
date: 2022-05-22 08:44
tags: Java, OOP, programiranje, dizajn šabloni, design patterns
summary: Primena dizajn šablona u programskom jeziku Java
description: {summary}
series: Advanced Java Programming
series_index: 6
lang: sr


[TOC]

-----

{% import "macros.html" as macros %}


Obrisi modernog programiranja datiraju od pre više od 30 godina. Tokom tog vremenskog perioda, programski jezici su korišćeni za rešavanje različitih problema. Ipak, veliki broj problema u programiranju iznova se i iznova ponavlja bez obzira na to o kojoj vrsti softverskog proizvoda je reč. Takvi česti problemi su tokom vremena detektovani i za njih su se ustalila određena rešenja, koja su se u praksi pokazala kao dobra. Reč je o rešenjima koja su artikulisana pojmom softverskih dizajn šablona. Njima će biti posvećena lekcija koja je pred vama. 


## Šta su softverski dizajn šabloni? 

Softverski dizajn šabloni (_software design patterns_) opisuju rešenja veoma čestih problema do kojih dolazi prilikom dizajniranja unutrašnje strukture nekog softverskog proizvoda. Reč je, zapravo, o dokazanim pristupima, odnosno praksama koje su se tokom vremena pokazale kao dobre. 

Bitno je razumeti da dizajn šabloni nisu gotova rešenja, već samo generalizovana, koncizna uputstva koja se mogu koristiti za konkretnu implementaciju rešenja. Stoga dizajn šabloni nisu vezani ni za jedan programski jezik, pa se njihova načela mogu primeniti prilikom kreiranja različitih tipova aplikacija, za različite platforme. 

Korišćenjem softverskih dizajn šablona ubrzava se proizvodnja, naročito ukoliko se ona odvija u timskom okruženju. Naime, realizacija softverskih dizajn šablona široko je poznata, pa programeri koji rade na istom projektu mnogo lakše mogu da se snađu u kodu koji je pisao neki drugi programer. 


## Koji dizajn šabloni postoje? 

Svi softverski dizajn šabloni se dele na tri grupe: 

- šabloni kreiranja (_creational patterns_) 
- strukturni šabloni (_structural patterns_) 
- šabloni ponašanja (_behavioral patterns_) 

Sve tri upravo navedene grupe poseduju ilustrativne nazive, koji oslikavaju intuitivno upotrebno okruženje šablona koji pripadaju konkretnoj grupi. Svaka od grupa poseduje veliki broj različitih šablona. U ovoj lekciji biće ilustrovana načela nekoliko najpoznatijih dizajn šablona i njihova realizacija u programskom jeziku Java: 

- **Singleton** 
- **Observer** 
- **Factory** 
- **Decorator** 


## **Singleton** 

**Singleton** je dizajn šablon koji propisuje postojanje samo jedne instance nekog tipa. Drugim rečima, **Singleton** nalaže rukovanje nekim tipom koje se uvek obavlja korišćenjem jedne iste instance. Tako uz poštovanje **Singleton** šablona nije moguće kreirati dva objekta jednog istog tipa. 

**Singleton** je jedan od najpopularnijih softverskih dizajn šablona, koji se primenjuje prilikom programiranja različitih aspekata aplikacija koje zahtevaju postojanje samo jednog objekta tokom čitavog životnog toka aplikacije. 

U dosadašnjem toku ovog kursa u više navrata ste imali prilike da vidite da se korišćenjem jedne klase može napraviti proizvoljan broj instanci, odnosno objekata: 

```java
Product product1 = new Product();
Product product2 = new Product();
System.out.println(product1.equals(product2));
```

Prikazani kod će proizvesti rezultat `false`, jer promenljive `product1` i `product2` čuvaju reference na dva potpuno nezavisna objekta klase `Product`. Ovo je ponašanje sa kojim smo se do sada susretali, a kao što je rečeno, podrazumeva da se na osnovu jedne klase može kreirati proizvoljan broj nezavisnih instanci (slika 6.1). 

{{ macros.image("/images/AdvancedJavaProgramming/1_06_01.png", "Slika 6.1. Na osnovu regularne klase moguće je kreirati proizvoljan broj objekata") }}

Ipak, u nekim situacijama može se javiti potreba da se definiše ponašanje po kojem se određena klasa može instancirati samo jednom. Upravo to osigurava **Singleton** dizajn šablon (slika 6.2). 

{{ macros.image("/images/AdvancedJavaProgramming/1_06_02.png", "Slika 6.2. Singleton klasa može imati samo jednu instancu") }}

Sa slike 6.2. se može videti da **Singleton** osigurava da se svakim instanciranjem jedne klase dobija identična instanca. 

U Java programskom jeziku, **Singleton** se realizuje vrlo jednostavno. Potrebno je obaviti nekoliko koraka koji su ilustrovani u nastavku. 

1. Onemogućavanje direktnog instanciranja klase 
	Pod direktnim instanciranjem klase podrazumeva se instanciranje upotrebom ključne reči `new` i pozivom konstruktora. Kako bi se tako nešto onemogućilo izvan klase, dovoljno je unutar klase definisati privatni konstruktor: 
	```java
	public class Logger {
		private Logger() {
		}
	}
	```

2. Kreiranje polja koje će čuvati referencu na instancu klase 
	S obzirom na to da se kod **Singleton** šablona klasa ne može instancirati na tradicionalni način, neophodno je unutar nje definisati mehanizam za predstavljanje instance. Tako se kod **Singleton** šablona instanca čuva unutar privatnog, statičkog polja klase: 
	```java
	public class Logger {
		private static Logger instance;
		
		private Logger() {
		}
	}
	```

3. Kreiranje mehanizma za pristup instanci **Singletona** 
	Kada imamo polje za čuvanje instance, preostaje da se definiše i javna metoda za pristup takvom polju: 
	```{.java title="Logger.java"}
	public class Logger {
		private static Logger instance;
		
		private Logger() {
			
		}
		
		public static Logger getInstance() {
			if (Logger.instance == null)
				instance = new Logger();
			return instance;
		}
	}
	```

Metoda za dobijanje instance imenovana je nazivom `getInstance()`. Unutar nje se obavlja vrlo jednostavna logika. Proverava se da li je instanca klase `Logger` već kreirana i samo ukoliko nije, obavlja se njeno kreiranje. Ukoliko instanca već postoji, kao povratna vrednost se isporučuje njena referenca, čime se osigurava da će svakim pozivanjem metode `getInstance()` biti isporučena referenca na istovetan objekat klase `Logger`. 

Ukoliko pokušamo da upravo kreiranu klasu instanciramo na tradicionalni način, doći će do greške, s obzirom na to da je konstruktor privatan. Kako bi se dobio objekat **Singleton** klase, koristi se sledeći pristup: 
```java
Logger logger = Logger.getInstance();
```

Vrlo je bitno razumeti da će svako pozivanje  `getInstance()` metode imati za efekat isporučivanje reference na identičan objekat, u šta se lako možemo uveriti: 

{java * AJP-1_06/Logger.java  Logger.java  0}

{java * AJP-1_06/Program1.java  Program1.java  0}

Za razliku od primera sa početka ove lekcije, prikazani kod sada proizvodi vrednost `true`, što jasno govori da je reč o dve promenljive koje čuvaju referencu na identičan objekat. 

**Klasa `Logger`** 
Naziv upravo kreirane **Singleton** klase nije izabran slučajno. Naime, jedna od realnih situacija za upotrebu **Singleton** šablona jesu situacije u kojima je potrebno napraviti klasu za logovanje informacija o unutrašnjem funkcionisanju programa. Veoma česta praksa u realnim aplikacijama jeste postojanje takve klase, koja unutar fajla ili posebnog skladišta podataka beleži sve informacije koje mogu biti značajne za programere koji su aplikaciju kreirali. Tokom izvršavanja aplikacije, potrebno je da postoji samo jedna instanca klase za logovanje. Drugim rečima, postojanje većeg broja instanci klase za logovanje nema smisla, pa je upravo zbog toga klasa `Logger` idealan kandidat za demonstraciju **Singleton** dizajn šablona. 

::: question correct="Singleton" answers="Singleton|Observer|Factory|MVC" unique_name="single_instance"
	Ukoliko je potrebno osigurati da određena klasa ima samo jednu instancu, koji šablon za dizajn softverskih komponenti se koristi? 


## **Observer** 

**Observer** je jedan od najpoznatijih šablona ponašanja. On omogućava razmenu obaveštenja između većeg broja objekata. Drugim rečima, **Observer** šablon omogućava da se stanje jednog objekta emituje različitim objektima koji taj objekat nadgledaju (slika 6.3). 

{{ macros.image("/images/AdvancedJavaProgramming/1_06_03.png", "Slika 6.3. Način funkcionisanja Observer dizajn šablona") }}

Na slici 6.3. možete da vidite najznačajnije elemente koji postoje unutar **Observer** šablona. Ovaj šablon poznaje dve vrste objekata: objekte tipa **Observer** i **Observable**. Kako bi se postigla što bolja apstrakcija i univerzalnost, ova dva tipa se predstavljaju intefejsima. **Observer** implementiraju svi konkretni tipovi koji žele da dobijaju obaveštenja, dok interfejs **Observable** implementiraju tipovi koji imaju potrebu da generišu i šalju obaveštenja. Konkretni tipovi koji generišu obaveštanje u **Observer** šablonu se nazivaju *Subject*. 

Nije teško zaključiti da se na **Observer** šablonu zasniva razmena događaja između objekata, što je pristup koji je obrađen u jednoj od prethodnih lekcija. Stoga smo se mi sa **Observer** šablonom već susretali, pa će u nastavku biti prikazan nešto jednostavniji primer, koji će se fokusirati isključivo na osnovne osobine ovog šablona. 

Kako bismo demonstrirali **Observer** šablon, prvo ćemo kreirati dva interfejsa, koji će predstavljati dva tipa objekata koji učestvuju u komunikaciji. Objekti koji mogu da budu obavešteni o nečemu zasnivaju se na ovakvom interfejsu: 

{java * AJP-1_06/Observer.java  Observer.java  0}

Objekti koji će moći da proizvedu obaveštenja zasnivaće se na ovakvom interfejsu: 

{java * AJP-1_06/Observable.java  Observable.java  0}

Nakon kreiranja interfejsa, oni se mogu iskoristiti za izgradnju konkretnih tipova. Evo prvo klase koja će poslužiti za kreiranje objekata koji će moći da primaju obaveštenja: 

{java * AJP-1_06/ObserverA.java  ObserverA.java  0}

Radi jednostavnosti primera, čim stigne poruka od objekta koji se nadzire, takva poruka će biti ispisana na izlazu. Pri tome svaki objekat tipa **Observer** poseduje i sopstveno ime koje se definiše prilikom instanciranja klase. 

Klasa koja će predstavljati objekte koji će moći da šalju obaveštenja nešto je kompleksnija, zato što se unutar nje moraju implementirati tri metode i jedno svojstvo koje će čuvati referencu na niz pretplatnika: 

{java * AJP-1_06/Subject.java  Subject.java  0}

Kako bismo se uverili da sve funkcioniše ispravno, unutar `main()` metode našeg Java programa postavićemo sledeći kod: 

{java * AJP-1_06/Program2.java  Program2.java  0}

Primer proizvodi sledeći rezultat: 
```shell
Observer Observer 1. Message from observable: new update
Observer Observer 2. Message from observable: new update
Observer Observer 3. Message from observable: new update
Observer Observer 3. Message from observable: new update1
```

S obzirom na to da su prilikom slanja prve poruke sva tri objekta u listi pretplatnika, aktiviraju se `update()` metode u tri objekta koji predstavljaju pretplatnike. Nakon uklanjanja pretplatnika `o2` i `o1` iz liste, sledeće ažuriranje podrazumeva slanje poruke samo jednom pretplatniku - `o3`. 


## **Factory** 

**Factory** je šablon kreiranja koji se koristi kada je potrebno kreirati posredničku klasu za kreiranje objekata određenog tipa. Drugim rečima, objekti određenog tipa se ne kreiraju na tradicionalni način, upotrebom konstruktora i ključne reči `new`, već posredstvom specijalne klase koja se naziva kao i sam šablon - `Factory`. Sve to izgleda kao na slici 6.4. 

{{ macros.image("/images/AdvancedJavaProgramming/1_06_04.png", "Slika 6.4. Factory klasa") }}

**Factory** šablon će u nastavku biti ilustrovan jednim primerom koji će modelovati nekoliko različitih vrsta korisnika. Naime, česta je praksa da se u aplikacijima koje rukuju korisnicima oni dele na nekoliko grupa, u zavisnosti od privilegaija koje imaju prilikom korišćenja aplikacije. Upravo jedan takav primer, u kome će postojati tri različite vrste korisnika, biće prikazan u nastavku. Tipovi korisnika će biti: 

- `Viewer` 
- `Admin` 
- `Superuser` 

Upravo prikazani tipovi korisnika u našem primeru ujedno će biti i konkretne klase koje će se koristiti za modelovanje odgovarajućeg tipa korisnika. S obzirom na to da su srodne, sve one mogu da naslede zajedničku apstraktnu klasu `User`, koja može poslužiti za definisanje nekih zajedničkih osobina svih korisnika: 

{java * AJP-1_06/User.java  User.java  0}

Klasa `User` je apstraktna i unutar sebe poseduje samo jedno svojstvo, kojim se definiše korisničko ime. Konstruktor prihvata jedan parametar i njime se inicijalizuje svojstvo `username`. Ovakvu klasu nasleđuju tri konkretne klase. 

{java * AJP-1_06/Viewer.java  Viewer.java  0}

{java * AJP-1_06/Admin.java  Admin.java  0}

{java * AJP-1_06/Superuser.java  Superuser.java  0}

Radi jednostavnosti, sve prikazane klase poseduju minimalnu logiku, odnosno samo konstruktor unutar koga se prvo poziva konstruktor roditeljske klase, a zatim se ispisuje poruka da je korisnik odgovarajućeg tipa i imena kreiran. 

Svaka od upravo kreiranih klasa može se instancirati na standardni način. Na primer: 

```java
Viewer viewer = new Viewer("John");
Admin admin = new Admin("Jack");
Superuser boss = new Superuser("Josh");
```

Na ovaj način se u programu kreira po jedan korisnik svakog tipa. Kreiranje objekata biće propraćeno ispisom sledećih poruka unutar konzole: 
```shell
Viewer John created.
Admin Jack created.
Superuser Josh created.
```

Veoma česta situacija u realnim aplikacijama prilikom rukovanja korisnicima jeste to da njihov tip nije unapred poznat, već se utvrđuje dinamički, tokom izvršavanja aplikacije. To praktično znači da većina aplikacija poseduje neku vrstu forme za prijavljivanje u koju je neophodno uneti korisničko ime i lozinku. Na osnovu unetih podataka, aplikacija utvrđuje o kojoj vrsti korisnika je reč, odnosno da li je korisnik tipa `Viewer`, `Admin` ili `Superuser`. Stoga se veoma često može dogoditi da na više mesta unutar svoje aplikacije posedujemo kod koji može da izgleda ovako: 

```java
User user = switch(userType) {
	case "viewer" -> new Viewer(username);
	case "admin" -> new Admin(username);
	case "superuser" -> new Superuser(username);
	default -> null;
};
```

Ovo je jedna uslovna konstrukcija u kojoj se u zavisnosti od vrednosti kontrolne promenljive (`userType`) obavlja instanciranje odgovarajuće klase koja predstavlja korisnika. S obzirom na to da su velike šanse da će ovakva provera biti potrebna na više mesta unutar aplikacije, idealno je nju enkapsulirati unutar jedne **Factory** klase: 

{java * AJP-1_06/UserFactory.java  UserFactory.java  0}

Ovo je klasičan primer **Factory** dizajn šablona na delu. Kreirana je nova `UserFactory` klasa, kao centralizovano mesto za instanciranje objekata koji predstavljaju korisnike. Sada se objekti korisnika mogu kreirati na sledeći način: 

```java
User user1 = UserFactory.newUser("admin", "Ron");
User user2 = UserFactory.newUser("viewer", "Ben");
User user3 = UserFactory.newUser("superuser", "Tom");
```

Na ovaj način su centralizovano kreirana tri objekta korisnika različitog tipa. Kod će na izlazu proizvesti sledeći ispis: 
```shell
Admin Ron created.
Viewer Ben created.
Superuser Tom created.
```


## **Decorator** 

**Decorator** je strukturni šablon koji omogućava dodavanje, odnosno proširivanje funkcionalnosti postojećih tipova. Implementira se kreiranjem posebne klase koja se naziva `Decorator`, unutar koje se objekti nekog tipa proširuju dodatnim osobinama ili funkcionalnostima. Tako **Decorator** šablon omogućava da se mogućnosti tipova prošire bez klasičnog nasleđivanja. Drugim rečima, `Decorator` klasa nije u direktnoj hijerarhijskoj vezi sa klasom koju dekoriše, već predstavlja neku vrstu njenog omotača (slika 6.5). 

{{ macros.image("/images/AdvancedJavaProgramming/1_06_05.png", "Slika 6.5. Decorator šablon") }}

**Decorator** šablon će biti ilustrovan na primeru jednog tipa kojim se u Java programu predstavljaju pravougaonici: 

{java * AJP-1_06/Rectangle.java  Rectangle.java  0}

Klasa `Rectangle` koristi se za modelovanje pravougaonika. Svojstva `a` i `b` se koriste za predstavljanje dužine stranica, čije vrednosti je moguće postaviti korišćenjem konstruktora koji prihvata dva parametra. Pored toga, klasa `Rectangle` poseduje i metodu za računanje površine sa nazivom `area()`. 

Korišćenjem **Decorator** šablona, objekti upravo kreirane klase se mogu proširiti na sledeći način: 

{java * AJP-1_06/RectangleDecorator.java  RectangleDecorator.java  0}

`RectangleDecorator` je klasičam primer implementacije **Decorator** šablona. Unutar ove klase obavlja se proširivanje funkcionalnosti `Rectangle` objekata jednom novom metodom koja je namenjena računanju obima. 

Konačno, evo kako može da izgleda upotreba `Decorator` klase: 

{java * AJP-1_06/Program3.java  Program3.java  0}

Prikazanim naredbama obavljeno je kreiranje objekta `RectangleDecorator` klase. Prilikom kreiranja takvog objekta, konstruktoru je prosleđen objekat `Rectangle` klase koji će `Decorator` da proširi. Nakon toga se obavlja računanje površine i obima i rezultati se prikazuju na izlazu. 


## **JavaBeans konvencija** 

Kada već govorimo o softverskim dizajn šablonima i različitim dobrim praksama za kreiranje unutrašnje objektne strukture Java programa, dobro je spomenuti još jedan pojam koji je značajan za Java jezik. Naime, u Java jeziku postoji jedna konvencija, odnosno standard koji se naziva **JavaBeans**. 

JavaBeans je konvencija koja definiše osobine tipova koji se nazivaju Java Bean. Java Bean je zapravo svaka klasa koja zadovoljava nekoliko jednostavnih pravila: 

- klasa mora imati javni konstruktor bez parametara 
- polja klase moraju biti privatna i moraju postojati odgovarajuće javne `get` i `set` metode za rukovanje njima izvan matične klase 
- klasa mora implementirati interfejs `Serializable` 

JavaBeans konvencija je primarno namenjena za kreiranje softverskih komponenti grafičkog korisničkog okruženja. O kreiranju grafičkog okruženja još nismo govorili, ali je bitno da znate da se pojedinačne komponente takvog okruženja predstavljaju objektima, odnosno instancama nekih klasa. Takođe, grafička okruženja se najčešće kreiraju pomoću određenih pomagala – grafičkih editora. Kako bi takvi editori mogli da funkcionišu adekvatno, oni se oslanjaju na upravo spomenutu konvenciju JavaBeans. Ipak, JavaBeans konvencija nije ograničena na komponente grafičkog korisničkog okruženja, pa se s njom možemo susresti i prilikom rada sa raznim drugim celinama Java platforme. 

Evo kako može izgledati jedna klasa koja zadovoljava JavaBeans konvenciju: 

{java * AJP-1_06/CarBean.java  CarBean.java  0}

Kod ilustruje klasu sa nazivom `CarBean`. Reč je o klasi koja u potpunosti zadovoljava **JavaBeans** konvenciju: 

- klasa implementira interfejs `Serializable` 
- klasa poseduje javni konstruktor, bez parametara 
- polja unutar klase su privatna i postoje `get` i `set` metode kako bi se njima rukovalo izvan klase
