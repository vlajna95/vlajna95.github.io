title: AJP 1.2. Apstraktne klase i interfejsi
date: 2022-01-10 19:31
tags: Java, OOP, programiranje, klase, interfejsi, apstrakcija
summary: Apstraktne klase i interfejsi u programskom jeziku Java
description: {summary}
series: Advanced Java Programming
series_index: 2
lang: sr


[TOC]

-----

{% import "macros.html" as macros %}


Prethodna lekcija donela je kratak osvrt na osnovne postulate objektno orijentisanog programiranja u Javi. Prikazano je kako se obavlja kreiranje klasa i objekata, te kako se postiže nasleđivanje, redefinisanje i preklapanje metoda. Sve su to pojmovi čije je razumevanje neophodno za ono što će biti izneto u nastavku ovog modula. 

Sada je vreme da se posvetimo naprednim osobinama objektno orijentisanog programiranja u Javi. Za početak, pozabavićemo se specifičnim oblicima u kojima mogu postojati Java klase, pa će tako u ovoj lekciji biti reči o apstraktnim klasama. Nakon apstraktnih klasa, u ovoj lekciji biće predstavljen još jedan veoma značajan pojam objektno orijentisanog programiranja - interfejsi. 


## Apstraktne klase 

Apstraktne klase omogućavaju da se kreira klasa koja se ne može instancirati. I sada se verovatno pitate – zbog čega bismo uopšte i kreirali klasu koja se ne može koristiti za kreiranje objekata? Naime, u nekim situacijama može se javiti potreba za kreiranjem klase koja bi se koristila samo kao obrazac za kreiranje nekih drugih klasa. Takva klasa bi služila kao osnova za sve klase koje bi iz nje bile izvedene. Tako su apstraktne klase one koje se ne mogu instancirati, već samo naslediti. 
Primer iz prethodne lekcije idealan je za razumevanje pojma apstraktnih klasa. Naime, `Product` klasa se može pretvoriti u apstraktnu klasu: 

```java
public abstract class Product {
...
}
```

Bitno je da primetite da smo prilikom definisanja klase `Product` iskoristili ključnu reč `abstract`. Ključna reč `abstract` je ono što jednu klasu čini apstraktnom. Ovu ključnu reč je potrebno postaviti nakon ključne reči koja predstavlja modifikator pristupa, a pre ključne reči `class` kojom se deklariše klasa. 

Nakon pretvaranja klase `Product` u apstraktnu, nećete moći da primetite nikakvu razliku u funkcionisanju koda iz prethodne lekcije. Naime, instanciranje objekata nasleđenih klasa funkcionisaće bez ikakvih problema. 

??? "Program.java"
	```{.java title="// Program.java"}
	public class Program {
		public static void main(String[] args) {
			Gamepad product1 = new Gamepad("Logitech", "F710", 129.99, true);
			Printer product2 = new Printer("HP", "Envy Photo 7155", 179.99, true);
			Monitor product3 = new Monitor("Dell", "U2419H", 219.99, 24);
			System.out.println(product1);
			System.out.println(product2);
			System.out.println(product3);
		}
	}
	```

??? "Product.java"
	```{.java title="// Product.java"}
	public abstract class Product {
		private String brand;
		private String model;
		private double price;
		// ...
		
		public Product(String brand, String model, double price) {
			this.brand = brand;
			this.model = model;
			this.price = price;
		}
		
		@Override
		public String toString() {
			return "Brand='" + brand + '\'' + ", Model='" + model + '\'' + ", Price=" + price;
		}
	}
	```

??? "Gamepad.java"
	```{.java title="// Gamepad.java"}
	public class Gamepad extends Product {
		boolean wireless;
		
		public Gamepad(String brand, String model, double price, boolean wireless) {
			super(brand, model, price);
			this.wireless = wireless;
		}
		
		@Override
		public String toString() {
			return super.toString() + ", " + "wireless=" + wireless;
		}
	}
	```

??? "Monitor.java"
	```{.java title="// Monitor.java"}
	public class Monitor extends Product {
		double diagonal;
		
		public Monitor(String brand, String model, double price, double diagonal) {
			super(brand, model, price);
			this.diagonal = diagonal;
		}
		
		@Override
		public String toString() {
			return super.toString() + ", " + "diagonal=" + diagonal;
		}
	}
	```

??? "Printer.java"
	```{.java title="// Printer.java"}
	public class Printer extends Product {
		boolean color;
		
		public Printer(String brand, String model, double price, boolean color) {
			super(brand, model, price);
			this.color = color;
		}
		
		@Override
		public String toString() {
			return super.toString() + ", " + "color=" + color;
		}
	}
	```

Ipak, ukoliko pokušate da instancirate klasu `Product`, koja je sada apstraktna, doći će do pojave greške (slika 2.1). 

{{ macros.image("/images/AdvancedJavaProgramming/1_02_01.png", "Slika 2.1. Pokušaj instanciranja apstraktne klase proizvodi grešku") }}

Na slici 2.1. se jasno može videti da razvojno okruženje ukazuje na grešku prilikom pokušaja instanciranja klase `Product` koja je apstraktna. 

Apstraktne i konkretne klase 
U prethodnim redovima ste mogli da pročitate da su apstraktne one klase koje se ne mogu instancirati. Sa druge strane, sve one klase koje se mogu instancirati nazivaju se konkretne. Tako se može reći da jedna klasa u Java jeziku može biti apstraktna ili konkretna. 


## Apstraktne metode 

Još jedna osobenost apstraktnih klasa jeste njihova mogućnost da sadrže apstraktne metode. Reč je o metodama koje ne poseduju implementaciju, odnosno logiku, već samo potpis: 

```java
public abstract class Product {
	...
	public abstract int checkStock();
}
```

Unutar klase `Product` sada je postavljena i jedna apstraktna metoda sa nazivom `checkStock()`. Da je reč o apstraktnoj metodi znamo na osnovu upotrebe ključne reči `abstract` prilikom njenog deklarisanja. Opet važi identično pravilo kao i prilikom kreiranja apstraktnih klasa: ključna reč `abstract` navodi se odmah nakon modifikatora pristupa, ali pre tipa povratne vrednosti. 

Apstraktne metode ne smeju imati telo, stoga je definisanje apstraktne metode sa telom sintaksna greška (slika 2.2). 

{{ macros.image("/images/AdvancedJavaProgramming/1_02_02.png", "Slika 2.2. Apstraktne metode ne mogu imati telo") }}

S obzirom na to da ne mogu imati telo i da se mogu pojaviti samo unutar klasa koje se ne mogu instancirati (čitaj: apstraktnih klasa), kao logično se nameće pitanje svrhe apstraktnih metoda. Apstraktne metode imaju jednu vrlo važnu ulogu u objektno orijentisanom programiranju. One se zapravo koriste da obavežu sve klase koje nasleđuju neku klasu da moraju obezbediti implementaciju svih metode koje su u roditeljskoj klasi označene kao apstraktne. Neispunjenje takve obaveze stvara grešku, pa stoga u ovom trenutku imamo tri greške u našem projektu (slika 2.3). 

{{ macros.image("/images/AdvancedJavaProgramming/1_02_03.png", "Slika 2.3. Obaveza klase da implementira apstraktne metode") }}

Slika 2.3. ilustruje poruku iz jedne od klasa koje nasleđuju klasu `Product` unutar našeg Java programa. I u ostalim klasama postoji identična greška - apstraktna metoda `checkStock()` iz roditeljske klase se mora implementirati u nasleđenoj klasi: 

??? "Program.java"
	```{.java title="// Program.java"}
	public class Program {
		public static void main(String[] args) {
			Monitor product3 = new Monitor("Dell", "U2419H", 219.99, 24);
			System.out.println(product3.checkStock());
		}
	}
	```

??? "Product.java"
	```{.java title="// Monitor.java"}
	public class Monitor extends Product {
		double diagonal;
		
		public Monitor(String brand, String model, double price, double diagonal) {
			super(brand, model, price);
			this.diagonal = diagonal;
		}
		
		@Override
		public String toString() {
			return super.toString() + ", " + "diagonal=" + diagonal;
		}
		
		@Override
		public int checkStock() {
			return (int) (Math.random() * 100);
		}
	}
	```

Na dnu klase `Monitor` sada možete da vidite metodu `checkStock()`, koja poseduje implementaciju, odnosno telo sa logikom koja utvrđuje stanje rezervi određenog proizvoda. Logika za utvrđivanje stanja zaliha služi samo radi ilustracije, pa metoda `checkStock()` kao svoju povratnu vrednost može da emituje broj u rasponu od 0 do 99. U realnim okolnostima, unutar metode `checkStock()` verovatno bi se nalazila logika koja bi podatke o stanju zaliha čitala iz nekog lokalnog ili udaljenog skladišta podataka. 
Metoda `checkStock()` obeležena je oznakom `@Override`, kako bi se naznačilo da istoimena metoda postoji i unutar roditeljske klase. I zaista, implementacija apstraktnih metoda je jedan od klasičnih primera redefinisanja metoda, odnosno polimorfizma. 

#### IntelliJ IDEA Tip: Implementiranje apstraktnih metoda 

Apstraktne metode iz roditeljskih klasa veoma lako se mogu implementirati korišćenjem razvojnog okruženja IntelliJ IDEA. Dovoljno je odabrati opciju **Implement methods_** koja postoji unutar panela koji se dobija kada se kursor miša postavi iznad podvučenog dela koda u situaciji kada postoje apstraktne metode koje nisu implementirane (slika 2.4). 

{{ macros.image("/images/AdvancedJavaProgramming/1_02_04.png", "Slika 2.4. Implementiranje apstraktnih metoda korišćenjem IntelliJ IDEA okruženja") }}

Klikom na opciju **Implement methods** otvara se prozor za odabir metoda koje će biti implementirane (slika 2.5). 

{{ macros.image("/images/AdvancedJavaProgramming/1_02_05.png", "Slika 2.5. Prozor za odabir metoda koje će biti implementirane") }}

U našem primeru postoji samo jedna metoda za implementiranje (`checkStock`), a pored odabira metoda za implementaciju, prozor sa slike 2.5. omogućava da odlučimo da li želimo da se JavaDoc komentari prekopiraju iz roditeljske klase i da li želimo da metoda bude obeležena `@Override` anotacijom, kako bi se lakše moglo uočiti da je reč o metodi koja je redefinisana. 
Klikom na dugme OK dobija se implementacija metode `checkStock()`, sa podrazumevanom logikom: 

```java
	@Override
	public int checkStock() {
		return 0;
	}
```

Jedini scenario u kome implementiranje apstraktnih metoda nije neophodno jeste onda kada i sama klasa koja nasleđuje nije konkretna. To praktično znači da se apstraktna metoda `checkStock()` ne bi morala implementirati onda kada bi i klasa `Monitor` bila apstraktna. Ipak, apstraktne metode iz svih roditeljskih klasa moraju se implementirati u prvoj konkretnoj klasi u lancu nasleđivanja. 

Apstraktne klase mogu posedovati i klasične metode 
Osobenost apstraktnih klasa jeste mogućnost postojanja apstraktnih metoda. Ipak, ništa ne sprečava apstraktne klase da pored apstraktnih metoda poseduju i klasične metode, odnosno metode koje imaju telo. Takođe, apstraktne klase mogu posedovati i sve ostale elemente koji se mogu naći unutar Java klasa - svojstva, konstruktore... 


## Interfejsi 

Esencijalni sastojak gotovo svakog objektno orijentisanog programskog jezika jesu i interfejsi. Odmah je potrebno razumeti da se pod pojmom interfejsa u objektno orijentisanom programiranju ne podrazumeva bilo kakvo korisničko okruženje (User Interface – UI), odnosno grafički interfejs, što je uglavnom prva pomisao koju početnici dobijaju prilikom spominjanja pojma interfejsa. Ovde je reč o pojmu sa potpuno drugačijim značenjem, odnosno o konceptu koji omogućava najviši stepen apstrakcije u objektno orijentisanim jezicima. 

Pre nego što se posvetimo praktičnom kreiranju interfejsa, neophodno je da razumemo odakle potiče takav naziv – interfejs. Naime, do sada ste već imali prilike da vidite da se objekti klasa ponašaju kao zaokružene celine, unutar kojih su procesom enkapsulacije objedinjena svojstva i ponašanja koja su karakteristična za tip konkretnog objekta. Sa spoljašnjim svetom, odnosno sa ostatkom programa, objekti komuniciraju primarno posredstvom metoda. Drugim rečima, nakon instanciranja neke klase i dobijanja objekta, imamo mogućnost da njima rukujemo pozivanjem njegovih metoda i obradom izlaznih podataka. Tako se može reći da su metode koje izlaže jedan objekat interfejs za vršenje interakcije sa takvim objektom. Analogija se može napraviti sa automobilom. Volan, ručica menjača, kontrole pored volana i kontakt-brava objedinjeno se mogu nazvati interfejsom koji nam je proizvođač automobila izložio kako bismo njime mogli da upravljamo. Mi ne moramo da znamo na koji način su sve nabrojane operacije realizovane ispod haube, već samo kako da koristimo interfejs koji nam je stavljen na raspolaganje. Po identičnom principu, i metode koje jedan objekat izlaže na korišćenje spoljnom svetu mogu se nazvati interfejsom za rukovanje takvim objektom. Java programski jezik omogućava da se takav interfejs artikuliše posebnim jezičkim elementom koji se kreira korišćenjem ključne reči `interface`. 

U svom osnovnom obliku, interfejsi u Javi mogu da poseduju proizvoljan broj apstraktnih metoda: 

```java
public interface Storable {
	public abstract void read();
	public abstract void write();
	public abstract void update();
	public abstract void delete();
}
```

Kao što možete da vidite, interfejsi se kreiraju slično klasama. Razlika je upotreba ključne reči `interface` umesto ključne reči `class`. Prikazanim kodom kreiran je jedan interfejs sa nazivom `Storable` i unutar njega se nalaze četiri apstraktne metode: `read()`, `write()`, `update()` i `delete()`. 

#### IntelliJ IDEA Tip: Kreiranje interfejsa 

Interfejsi se korišćenjem IntelliJ IDEA razvojnog okruženja kreiraju slično klasama. Potrebno je odabrati opciju **New->Java Class**, koja se nalazi u kontekstnom meniju koji se dobija desnim klikom na folder `src` (slika 2.6). 

{{ macros.image("/images/AdvancedJavaProgramming/1_02_06.png", "Slika 2.6. Opcija za kreiranje nove klase (interfejsa)") }}

U prozoru koji se zatim dobija, potrebno je uneti naziv interfejsa i odabrati opciju **Interface** (slika 2.7). 

{{ macros.image("/images/AdvancedJavaProgramming/1_02_07.png", "Slika 2.7. Prozor za unos naziva novog interfejsa") }}

Nakon potvrđivanja pritiskom na taster Enter ili duplim klikom na opciju **Interface**, IntelliJ IDEA kreira interfejs sa definisanim imenom, čije je telo prazno: 

```java
public interface Storable {
	
}
```

U upravo kreiranom interfejsu sa nazivom `Storable`, definisane su četiri apstraktne metode. S obzirom na to da je reč o apstraktnim metodama, one ne poseduju telo, već samo potpis. Osnovni razlog za kreiranje interfejsa jeste njihova implementacija od strane klasa. Na primer, ovako može da izgleda implementacija `Storable` interfejsa od strane klase `Gamepad`: 

```java
public class Gamepad extends Product implements Storable {
	...
}
```

Interfejs se implementira korišćenjem ključne reči `implements`, nakon koje se navodi naziv interfejsa. Kada jedna klasa implementira neki interfejs, ona se obavezuje da će implemetirati sve metode koje se nalaze unutar interfejsa. To praktično znači da se unutar klase `Gamepad` moraju implemetirati sve metode koje postoje unutar interfejsa `Storable` (slika 2.8). 

{{ macros.image("/images/AdvancedJavaProgramming/1_02_08.png", "Slika 2.8. Prilikom implementiranja interfejsa moraju se implementirati sve njegove apstraktne metode") }}

Kako bi klasa `Gamepad` ispunila obećanje dato implementiranjem interfejsa, neophodno je da unutar nje budu implementirane sve metode iz interfejsa: 

??? "Program.java"
	```{.java title="// Program.java"}
	public class Program {
		public static void main(String[] args) {
			Gamepad product1 = new Gamepad("Logitech", "F710", 129.99, true);
			product1.delete();
		}
	}
	```

??? "Product.java"
	```{.java title="// Product.java"}
	public abstract class Product {
		private String brand;
		private String model;
		private double price;
		//...
		
		public Product(String brand, String model, double price) {
			this.brand = brand;
			this.model = model;
			this.price = price;
		}
		
		@Override
		public String toString() {
			return "Brand='" + brand + '\'' + ", Model='" + model + '\'' + ", Price=" + price;
		}
	}
	```

??? "Gamepad.java"
	```{.java title="// Gamepad.java"}
	public class Gamepad extends Product implements Storable {
		boolean wireless;
		
		public Gamepad(String brand, String model, double price, boolean wireless) {
			super(brand, model, price);
			this.wireless = wireless;
		}
		
		@Override
		public String toString() {
			return super.toString() + ", " + "wireless=" + wireless;
		}
		
		@Override
		public void read() {
			// logic for reading
		}
		
		@Override
		public void write() {
			// logic for writing
		}
		
		@Override
		public void update() {
			// logic for updating
		}
		
		@Override
		public void delete() {
			// logic for deleting
		}
	}
	```

??? "Storable.java"
	```{.java title="// Storable.java"}
	public interface Storable {
		public abstract void read();
		public abstract void write();
		public abstract void update();
		public abstract void delete();
	}
	```

Možemo da zaključimo da se korišćenjem interfejsa `Storable` klasa `Gamepad` obavezala da će unutar sebe imati četiri metode koje su definisane unutar takvog interfejsa. 

Interfejs `Storable` 
Prilikom demonstracije upotrebe interfejsa, u ovoj lekciji smo se odlučili za jedan realan primer interfejsa. Naime, upravo kreirani interfejs `Storable` može se koristiti da naznači da neka klasa poseduje metode za obavljanje osnovnih operacija nad skladištem podataka. 
U realnim aplikacijama, podaci se čuvaju unutar različitih vrsta skladišta podataka. Na primer, podaci se mogu čuvati unutar običnih tekstualnih fajlova, ali i unutar specijalizovanih skladišta koja se nazivaju baze podataka. Podaci iz takvih skladišta se unutar Java programa predstavljaju kao objekti odgovarajućih klasa. U primeru iz ove lekcije, to bi značilo da se podaci o proizvodima nalaze u nekoj bazi podataka. Java program takvim podacima rukuje u objektnom obliku, pri čemu se metode `read()`, `write()`, `update()` i `delete()` koriste za obavljanje četiri osnovne operacije nad podacima - čitanje, pisanje, ažuriranje i brisanje, respektivno. Implementacija interfejsa `Storable` u primeru naše aplikacije jeste garancija da objekti neke klase poseduju četiri upravo spomenute metode za obavljanje osnovnih operacija nad skladištem podataka. 

Metode koje se definišu unutar interfejsa su podrazumevano javne apstraktne metode. Upravo zbog toga je ključne reči `public` i `abstract` moguće izostaviti i napisati sledeće: 

```java
public interface Storable {
	void read();
	void write();
	void update();
	void delete();
}
```

### Razlika između interfejsa i apstraktnih klasa 

U ovom trenutku se možete pitati zbog čega su nam potrebni interfejsi, kada smo identično mogli da postignemo i korišćenjem apstraktne klase i apstraktnih metoda unutar nje. Jednostavno smo mogli da apstraktne metode iz interfejsa definišemo unutar roditeljske `Product` klase i efekat bi bio identičan, odnosno i tada bismo klasu `Gamepad` obavezali da mora imati implementacije sve četiri metode iz interfejsa. Ipak, postoji nekoliko značajnih razlika između apstraktnih klasa i interfejsa. 

Apstraktne klase se nasleđuju, dok se interfejsi implementiraju 
Prva razlika je kozmetičke mprirode. Apstraktne klase se nasleđuju, dok se interfejsi implementiraju, a takve operacije su propraćene i upotrebom odgovarajućih ključnih reči - `extends` i `implements`, respektivno. 

Jedna klasa može da nasledi samo jednu apstraktnu klasu, ali zato može da implemetira proizvoljan broj interfejsa 
Prva značajna razlika između apstraktnih klasa i interfejsa odnosi se na mogućnost višestruke implementacije. Naime, jedna klasa može da implementira veći broj interfejsa, što nije slučaj prilikom nasleđivanja klasa. Stoga mi sada možemo napraviti još jedan interfejs, a onda njega implementirati od strane klase `Gamepad`. Evo kako izgleda novi interfejs: 

```java
public interface Searchable {
	void search();
}
```

Klasa `Gamepad`, pored već implementiranog interfejsa, sada može da implementira i `interfejs `Searchable`: 

```java
public class Gamepad extends Product implements Storable, Searchable {
	...
}
```

Klasa `Gamepad` sada implementira dva interfejsa. Jednostavno, nakon ključne reči `implements` moguće je navesti veći broj interfejsa, koji se razdvajaju karakterom zapeta. 

Sada u okviru radnog okruženja možete dodati novi fajl `Searchable.java u kome bi se nalazio istoimeni interfejs, i onda klasa `Gamepad` može da njegovom implementacijom nasledi `search()` metodu. 

Jedan interfejs može biti implementiran od strane proizvoljnog broja klasa, pa čak i kada one međusobno nemaju nikakvih dodirnih tačaka 
Svakako najznačajnija osobenost interfejsa, i ujedno ono što ih razlikuje od apstraktnih klasa, jeste mogućnost implementacije interfejsa od strane klasa koje nemaju nikakvih dodirnih tačaka. Naime, interfejsi nisu vezani za neki konkretan tip ili grupu tipova. Jedan interfejs se može implementirati od strane klasa koje nemaju nikakvih dodirnih tačaka, što je u potpunosti suprotno od onoga što važi za apstraktne klase. Naime, sve klase koje nasleđuju jednu klasu moraju biti srodne, s obzirom na to da dele osobine koje su definisane unutar roditeljske klase. Za razliku od apstraktnih klasa, jedan interfejs mogu implementirati klase potpuno različitih namena. 
Sve ovo u našem konkretnom primeru znači da interfejse `Storable` i `Searchable` mogu da implementiraju sve klase koje treba da imaju metode za čuvanje i pretragu: 

```java
public class Customer implements Storable {
	private String name;
	private String address;
	private String gender;
	
	public Customer() {
		
	}
	
	public Customer(String name, String address, String gender) {
		this.name = name;
		this.address = address;
		this.gender = gender;
	}
	
	@Override
	public void read() {
		// read logic
	}
	
	@Override
	public void write() {
		// write logic
	}
	
	@Override
	public void update() {
		// update logic
	}
	
	@Override
	public void delete() {
		// delete logic
	}
}
```

Ovo je primer još jedne klase koja može postojati u našem programu. Naime, velike su šanse da program koji rukuje proizvodima ima potrebu i za predstavljanjem kupaca, odnosno klijenata. Upravo to može biti namena prikazane klase `Customer`. `Customer` je klasa koja ne deli osobine ni sa jednom od klasa kojima se predstavljaju proizvodi. Ipak, to ne sprečava nijednu od takvih klasa da implementira interfejs `Storable`. Zbog toga i klasa `Customer` implementira interfejs `Storable` i sve metode koje se unutar njega nalaze. To je garancija da objekti ove klase poseduju metode za obavljanje osnovnih operacija nad podacima kupaca. 

Sada u okviru radnog okruženja možete dodati novi fajl `Customer.java` u kome bi se nalazila istoimena klasa. 

Interfejsi su referentni tipovi 
Kreiranjem novog interfejsa zapravo se dobija jedan novi referentni tip u programu koji kreiramo. To praktično znači da su `Storable` i `Searchable` tipovi podataka. Veoma se lako možemo uveriti da je to stvarno tako: 

```java
Storable product1 = new Gamepad("Logitech", "F710", 129.99, true);
```

Naredba ilustruje kod za kreiranje jednog objekta klase `Gamepad`. Ipak, bitno je da primetite da je referenca na takav objekat smeštena unutar promenljive tipa `Storable`. To je dokaz da je kreiranjem interfejsa `Storable` stvoren i jedan novi tip u našem Java programu. To takođe znači i da se objekti klase `Gamepad` sada mogu predstaviti korišćenjem nekoliko tipova: 

- korišćenjem tipa `Gamepad`, što je osnovni tip matične klase 
- korišćenjem tipa `Product`, zato što klasa `Gamepad` nasleđuje takvu klasu 
- korišćenjem tipa `Storable`, što je interfejs koji ova klasa implementira 

```java
Gamepad product1 = new Gamepad("Logitech", "F710", 129.99, true);
Product product1 = new Gamepad("Logitech", "F710", 129.99, true);
Storable product1 = new Gamepad("Logitech", "F710", 129.99, true);
```

Činjenica da su interfejsi tipovi veoma je korisna u situacijama kada je potrebno rukovati objektima čije konkretne tipove ne možemo znati unapred. Na primer, zamislite metodu koja može da prihvati neki objekat koji se može sačuvati u bazi i nad takvim objektom obavlja određene provere i na kraju pokreće operaciju čuvanja: 

```java
public void saveObject(Storable object) {
	// do validation, and if valid call write
	object.write();
}
```

Metoda `saveObject()` je klasičan primer metode koja zavisi od apstrakcije, a ne od konkretne implementacije. Šta to praktično znači? 
Ulazni parametar metode jeste tipa `Storable`. To je tip koji predstavlja interfejs, a interfejs ne predstavlja neki konkretan tip podatka, zato što može biti implementiran od strane bilo koje klase. Stoga smo na ovaj način omogućili metodi `saveObject()` da prihvati objekte koji mogu da budu različitih konkretnih tipova. Njoj možemo da prosledimo objekte tipa `Gamepad` ili objekte tipa `Customer`, odnosno objekte svih onih konkretnih tipova koji implementiraju interfejs `Storable`. Štaviše, metoda `saveObject()` uopšte ne mora ni znati koji će konkretan tip da dobije. Sve što ona zna jeste da će dobiti tip koji je implemetirao interfejs `Storable`, a to je garancija da će takav objekat sigurno imati metodu `write()` koja je definisana unutar interfejsa `Storable`. 

### Podrazumevane metode unutar interfejsa 

Do sada ste imali prilike da vidite interfejse koji su unutar sebe imali apstraktne, javne metode. Javne apstraktne metode dugo su bile jedini sadržaj koji se mogao naći unutar interfejsa. Ipak, u novijim verzijama Jave takva činjenica se promenila, pa su tokom vremena u jezik dodate mogućnosti da interfejsi sadrže i neke druge članove. Za početak, unutar interfejsa se mogu naći podrazumevane metode. 

Podrazumevane metode omogućavaju da se unutar interfejsa definišu konkretne metode, odnosno metode koje poseduju telo. Ali, zbog čega su nam potrebne konkretne metode unutar interfejsa? 

Već ste imali prilike da vidite da se interfejsi mogu implementirati od strane velikog broja različitih klasa. Pri tom, sve klase koje implemetiraju jedan interfejs moraju obezbediti implementaciju svih metoda definisanih unutar tog interfejsa. Sada se postavlja pitanje – šta ukoliko se pojavi potreba za naknadnim dodavanjem još neke metode unutar interfejsa? 

```java
public interface Storable {
	void read();
	void write();
	void update();
	void delete();
	boolean exists();
}
```

Sada je unutar interfejsa `Storable` dodata još jedna metoda - `exists()`. Reč je o metodi koja je namenjena za utvrđivanje postojanja nekog objekta unutar skladišta podataka. Kada učinimo nešto ovako, odnosno kada dodamo novu metodu unutar interfejsa, sve klase koje su implementirale takav interfejs postaju nevalidne. Drugim rečima, u ovakvoj situaciji metoda `exists()` se mora implementirati u svim klasama koje implementiraju interfejs `Storable` kako bi kod bio validan. U realnim okolnostima, odnosno unutar realnih Java programa, jedan interfejs može biti implementiran od strane velikog broja klasa. U takvoj situaciji, dodavanje nove metode unutar interfejsa bi podrazumevalo da se svaka od takvih klasa modifikuje, dodavanjem implementacije za metodu koja je dodata. Kako bi se prevazišao takav problem, u Java jezik je uvršćena mogućnost definisanja podrazumevanih (**default**) metoda unutar interfejsa: 

```java
public interface Storable {
	void read();
	void write();
	void update();
	void delete();
	
	default boolean exists() {
		return true;
	}
}
```

Do malopre apstraktna metoda `exists()` sada je pretvorena u podrazumevanu metodu, koja poseduje telo. To sve klase koje implementiraju interfejs `Storable` oslobađa potrebe za implementacijom takve metode. Naravno, klase koje implementiraju interfejs `Storable` imaju mogućnost da ovakvu podrazumevanu metodu redefinišu, ukoliko se za takvim nečim javi potreba: 

```java
public class Gamepad extends Product implements Storable, Searchable {
	...
	
	@Override
	public boolean exists() {
		// Gamepad specific logic for exists() method
		return false;
	}
}
```

Sada u okviru radnog okruženja možete interfejsu `Storable` i klasi `Gamepad` dodati **default** metodu `exists()`. 

### Privatne metode unutar interfejsa 

S obzirom na to da interfejsi u Javi imaju mogućnost da poseduju konkretne metode, nekada može biti vrlo korisno određenu logiku grupisati unutar metoda koje se mogu koristiti samo unutar interfejsa, a ne i izvan njega. Do takve situacije veoma često može doći kada više podrazumevanih metoda treba da deli određenu istovetnu logiku. Takva istovetna logika se može grupisati unutar privatnih metoda unutar interfejsa: 

??? "Program.java"
	```{.java title="// Program.Java"}
	public class Program {
		public static void main(String[] args) {
			Gamepad product1 = new Gamepad("Logitech", "F710", 129.99, true);
			System.out.println(product1.exists());

		}
	}
	```

??? "Product.java"
	```{.java title="// Product.java"}
	public abstract class Product {
		private String brand;
		private String model;
		private double price;
		// ...
		
		public Product(String brand, String model, double price) {
			this.brand = brand;
			this.model = model;
			this.price = price;
		}
		
		@Override
		public String toString() {
			return "Brand='" + brand + '\'' + ", Model='" + model + '\'' + ", Price=" + price;
		}
	}
	```

??? "Gamepad.java"
	```{.java title="// Gamepad.java"}
	public class Gamepad extends Product implements Storable, Searchable {
		boolean wireless;
		
		public Gamepad(String brand, String model, double price, boolean wireless) {
			super(brand, model, price);
			this.wireless = wireless;
		}
		
		@Override
		public String toString() {
			return super.toString() + ", " + "wireless=" + wireless;
		}
		
		@Override
		public boolean exists() {
			// Gamepad specific logic for exists() method
			return false;
		}
		
		@Override
		public void search() {
			// logic for searching
		}
		
		@Override
		public void read() {
			// logic for reading
		}
		
		@Override
		public void write() {
			// logic for writing
		}
		
		@Override
		public void update() {
			// logic for updating
		}
		
		@Override
		public void delete() {
			// logic for deleting
		}
	}
	```

??? "Storable.java"
	```{.java title="// Storable.java"}
	public interface Storable {
		void read();
		void write();
		void update();
		void delete();
		
		default boolean exists() {
			method1();
			method2();
			return true;
		}
		
		private void method1() {
			System.out.println("Hello from private method1");
		}
		
		private void method2() {
			System.out.println("Hello from private method2");
		}
	}
	```

??? "Searchable.java"
	```{.java title="// Searchable.java"}
	public interface Searchable {
		void search();
	}
	```

Unutar interfejsa `Storable` sada su dodate dve privatne metode - `method1()` i `method2()`, koje se koriste od strane podrazumevane metode. Bitno je razumeti nekoliko važnih činjenica o privatnim metodama unutar interfejsa: 

- privatne metode unutar interfejsa namenjene su lokalnoj upotrebi, odnosno, one se mogu koristiti samo unutar interfejsa u kome su definisane 
- privatne metode unutar interfejsa ne mogu biti apstraktne, te moraju posedovati telo sa logikom 
- privatne metode unutar interfejsa nisu namenjene za spoljašnju upotrebu, tako da se ne implementiraju niti ih je moguće redefinisati u konkretnim klasama 

### Konstante unutar interfejsa 

Na kraju, još jedan element koji može postojati unutar Java interfejsa jesu i **konstante**. Tako je, pored metoda, unutar interfejsa moguće definisati i javna, statička, finalna polja, koja moraju posedovati vrednost: 

```java
public interface Storable {
	public static final int SOME_CONSTANT = 13;
	...
}
```

Zapravo, svako polje koje se definiše unutar interfejsa mora biti javno, statičko i finalno, te je stoga upravo prikazani kod ekvivalentan ovom: 

```java
public interface Storable {
	int SOME_CONSTANT = 13;
	...
}
```

Razlog zbog koga su sva polja unutar interfejsa podrazumevano statička vrlo je jednostavan. Interfejsi se ne mogu instancirati, pa se tako polja koja se unutar njih definišu dele između svih klasa koje takav interfejs implementiraju. 

Konstante unutar interfejsa je moguće definisati ukoliko znamo da će za njihovim korišćenjem postojati potreba kod svih klasa koje će interfejs implementirati. U takvoj situaciji, umesto definisanja konstante u svakoj konkretnoj klasi pojedinačno, sve one će imati pristup zajedničkoj konstanti koja postoji unutar interfejsa. Ipak, potrebno je voditi računa da konstanta zaista bude čvrsto vezana za samu namenu interfejsa. U programerskim krugovima dugo se vodi debata o opravdanosti korišćenja konstanti unutar interfejsa, s obzirom na to da se konstante smatraju detaljem koji se bavi implementacijom, dok su interfejsi primarno namenjeni za postizanje apstrakcije. 

Imenovanje interfejsa 
Veoma česta praksa jeste imenovanje interfejsa korišćenjem engleskih prideva koji poseduju sufiks **-able** ili **-ible**. Reč je o pridevima koji nastaju od glagola: `Comparable`, `Iterable`, `Storable`, `Queryable`... Ovakvi nazivi koriste se da označe da je neka klasa sposobna za obavljanje određenih operacija, sadržanih u nazivu interfejsa. Na primer, `Comparable` je naziv koji oslikava da se objekti klasa koje implementiraju takav interfejs mogu porediti. 
Formiranje naziva interfejsa koji se završavaju sufiksima **-able** i **-ible** nije pravilo, već samo česta praksa. Stoga je interfejse moguće imenovati proizvoljnim nazivom, sve dok se pridržavamo pravila za formiranje identifikatora u Java jeziku. 


## Vežbe 

### Vežba 1 

Potrebno je napraviti aplikaciju za restoran brze hrane. Aplikacija će rukovati proizvodima restorana. Restoran brze hrane u ponudi poseduje pice i sendviče. Neophodno je napraviti odgovarajuće klase za modelovanje pica i sendviča i za njihovo predstavljanje u Java programu. Prilikom realizacije je potrebno upotrebiti apstraktne klase i apstraktne metode. 
Sendviči i pice treba da budu određeni sledećim svojstvima: 

- naziv, String podatak 
- cena, double podatak 
- maksimalno 10 začina (priloga), niz String vrednosti 

Nad proizvodima (picama i sendvičima) potrebno je omogućiti obavljanje nekoliko operacija, kroz sledeće metode: 

- metoda `addSpice()` koja unosi začin 
- metoda `allSpices()` koja vraća sve začine u tekstualnom obliku 
- apstraktna metoda `countPrice()` koja izračunava cenu na osnovu tipa proizvoda; porez na picu je 10%, dok je porez na sendviče 15% 
- metoda `toString()` koja prikazuje podatke o proizvodu u sledećoj formi: 
    Product: pizza, price: 25.45, spices: tomato, mustard, mayonnaise 

Potrebno je napraviti klase `Product`, `Pizza` i `Sandwich`. Klase `Pizza` i `Sandwich` naslediće apstraktnu klasu `Product`. Na kraju je potrebno kreirati po jednu instancu klasa `Pizza` i `Sandwich` u `main()` metodi. 

#### Rešenje 

??? "Product.java"
	```{.java title="// Product.java"}
	public abstract class Product {
		public int type;
		public String name;
		public double price;
		public String[] spices;
		public abstract double countPrice();
		
		public Product(String name, double price) {
			this.spices = new String[10];
			this.name = name;
			this.price = price;
		}
		
		@Override
		public String toString() {
			StringBuilder output = new StringBuilder();
			output.append("Product: ");
			output.append(this.name).append(", ");
			output.append("price: ").append(countPrice()).append(", ");
			output.append("spices: ").append(allSpices());
			return output.toString();
		}
		
		public String allSpices() {
			StringBuilder output = new StringBuilder();
			for (String addition : this.spices)
				if (addition != null) {
					output.append(addition).append(", ");
				}
			if (!output.toString().equals("")) {
				if (output.toString().trim().endsWith(",")) {
					output.replace(output.length() - 2, output.length(), "");
				}
				else {
					output.append("no spices");
				}
			}
			return output.toString();
		}
		
		public void addSpice(String spice) {
			for (int i = 0; i < this.spices.length; i++)
				if (this.spices[i] == null) {
					this.spices[i] = spice;
					break;
				}
		}
	}
	```

??? "Pizza.java:"
	```{.java title="// Pizza.java"}
	public class Pizza extends Product {
		public Pizza(String name, double price) {
			super(name, price);
		}
		
		@Override
		public double countPrice() {
			return this.price + this.price * 0.1;
		}
	}
	```

??? "Sandwich.java"
	```{.java title="// Sandwich.java"}
	public class Sandwich extends Product {
		public Sandwich(String name, double price) {
			super(name, price);
		}
		
		public double countPrice() {
			return this.price + this.price * 0.15;
		}
	}
	```

??? "Program.java"
	```{.java title="// Program.java"}
	public class Program {
		public static void main(String[] args) {
			Pizza p = new Pizza("Capricciosa",25);
			p.addSpice("tomato");
			p.addSpice("sour cream");
			Sandwich s = new Sandwich("Sandwich with ham", 35);
			s.addSpice("cucumber");
			s.addSpice("onion");
			s.addSpice("tomato");
			System.out.println(p);
			System.out.println(s);
		}
	}
	```

### Vežba 2 

U narednoj vežbi potrebno je obaviti sledeće: 

- napraviti apstraktnu klasu `Quad` koja sadrži tri polja (koordinate `x` i `y` i stranicu `a`) i jednu apstraktnu metodu `setValues()` za postavljanje svih vrednosti 
- napraviti interfejs `Geom` koji sadrži potpise metoda za izračunavanje površine i obima 
- napraviti klasu `Square` koja nasleđuje klasu `Quad` i implementira interfejs `Geom` 
- kreirati jednu instancu klase `Square` u glavnom programu 

#### Rešenje 

??? "Quad.java"
	```{.java title="// Quad.java"}
	public abstract class Quad {
		public int x, y, a;
		public abstract void setValues(int x, int y, int a);
	}
	```

??? "Geom.java"
	```{.java title="// Geom.java"}
	public interface Geom {
		int area();
		int perimeter();
	}
	```

??? "Square.java"
	```{.java title="// Square.java"}
	public class Square extends Quad implements Geom {
		public int area() {
			return a * a;
		}
		
		@Override
		public int perimeter() {
			return 4 * this.a;
		}
		
		@Override
		public void setValues(int x, int y, int a) {
			this.x = x;
			this.y = y;
			this.a = a;
		}
	}
	```

??? "Program.java"
	```{.java title="// Program.java"}
	public class Program {
		public static void main(String[] args) {
			Square s = new Square();
			s.setValues(100, 100, 5);
			System.out.println(s.area());
			System.out.println(s.perimeter());
		}
	}
	```

### Vežba 3 

U ovoj vežbi potrebno je kreirati dva interfejsa za aplikaciju kalkulator: 

- `Operations` 
- `Operands` 

`Operands` treba da sadrži potpis metode `setOperands()` koji postavlja operande na inicijalne vrednosti. Interfejs `Operations` treba da sadrži potpise metoda sa operacijama (dovoljne su samo dve). 

Nakon kreiranja interfejsa, potrebno je napraviti klasu `Calculator` koja će implementirati interfejse `Operations` i `Operands`. 
Na kraju je potrebno instancirati klasu `Calculator` i pozvati njene metode `add()` i `sub()` koje vrše sabiranje i oduzimanje dva realna broja. 

#### Rešenje 

??? "Operands.java"
	```{.java title="// Operants.java"}
	public interface Operands {
		void setOperands(double a, double b);
	}
	```

??? "Operations.java"
	```{.java title="// Operations.java"}
	public interface Operations {
		double add();
		double sub();
	}
	```

??? "Calculator.java"
	```{.java title="// Calculator.java"}
	public class Calculator implements Operations, Operands {
		public double a, b;
		
		public double add() {
			return a + b;
		}
		
		public double sub() {
			return a - b;
		}
		
		public void setOperands(double a, double b) {
			this.a = a;
			this.b = b;
		}
	}
	```

??? "Program.java"
	```{.java title="// Program.java"}
	public class Program {
		public static void main(String[] args) {
			Calculator c = new Calculator();
			c.setOperands(2, 3);
			System.out.println(c.add());
			System.out.println(c.sub());
		}
	}
	```
