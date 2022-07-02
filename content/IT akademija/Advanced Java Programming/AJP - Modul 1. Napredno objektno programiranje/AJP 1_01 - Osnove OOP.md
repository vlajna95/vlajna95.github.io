title: AJP 1.1. Objektno orijentisano programiranje u Javi
date: 2022-01-10 15:33
tags: Java, OOP, programiranje, objekti, klase, apstrakcija, enkapsulacija, nasleđivanje, polimorfizam
summary: Uvod u objektno orijentisano programiranje u Javi i najvažniji pojmovi
description: {summary}
series: Advanced Java Programming
series_index: 1
lang: sr


[TOC]

-----

{% import "macros.html" as macros %}


Kurs pred vama biće posvećen naprednim konceptima programiranja korišćenjem programskog jezika Java. Tako ćete imati prilike da proširite svoje znanje upoznavanjem različitih koncepata koji su neophodni za kreiranje kompleksnijih Java programa. Uvodni modul ovog kursa pomoći će vam da proširite razumevanje objektno orijentisanog programiranja u Javi. Za početak, uvodna lekcija ovog modula biće posvećena osnovnim postulatima OOP u Javi, što će vam pomoći da bolje razumete napredne koncepte koji će biti predstavljeni u lekcijama koje slede. Stoga će u ovoj lekciji biti objašnjeno šta su to objekti i klase, koji su njihovi članovi, ali i šta podrazumevaju pojmovi apstrakcije, enkapsulacije, nasleđivanja i polimorfizma, koji predstavljaju osnovne postulate objektno orijentisanog programiranja. 


## Pojam objektno orijentisanog programiranja 

Java je objektno orijentisan programski jezik, što praktično znači da su klase i objekti njegove centralne figure. Objekti su način da se unutar Java programa predstave podaci po uzoru na pojmove iz realnog sveta. U praksi to znači da se objektima mogu vrlo efikasno predstaviti podaci koji su potrebni našim Java programima. Na primer, ukoliko kreiramo program koji rukuje proizvodima koji predstavljaju tehničku robu, svaki takav artikal (proizvod) bio bi jedan objekat (slika 1.1). 

{{ macros.image("/images/AdvancedJavaProgramming/1_01_01.png", "Slika 1.1. Objekti") }}

Objekti se kreiraju na osnovu određenog šablona, odnosno modela. U objektno orijentisanom programiranju takvi šabloni se drugačije nazivaju klase (slika 1.2). 

{{ macros.image("/images/AdvancedJavaProgramming/1_01_02.png", "Slika 1.2. Objekti nastaju na osnovu klasa") }}


## Klase 

Preduslov za kreiranje objekata u Java jeziku jeste postojanje klase. Unutar klase definišu se sve one osobine, odnosno svojstva i ponašanja, koja će objekti koji se na osnovu takve klase kreiraju imati. 

Procesom kreiranja klasa obavlja se modelovanje specifičnih tipova podataka koji su potrebni za funkcionisanje programa koje stvaramo. Tako na primer, ukoliko će naš program rukovati nekim proizvodima, klasa za njihovo modelovanje bi mogla da izgleda ovako: 

```java
public class Product {
	private String brand;
	private String model;
	private double price;

	public String getBrand() {
		return brand;
	}

	public void setBrand(String brand) {
		this.brand = brand;
	}

	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public double getPrice() {
		return price;
	}

	public void setPrice(double price) {
		this.price = price;
	}

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

Prikazani kod ilustruje klasu `Product`, koja se u Java programu može koristiti za predstavljanje proizvoda. `Product` klasa poseduje nekoliko veoma važnih elemenata čiju svrhu je neophodno razumeti. 

### Privatna svojstva 

Svojstva definišu karakteristike koje će moći da imaju objekti koji se kreiraju korišćenjem klase. U prikazanoj klasi postoje sledeća svojstva: 

```java
private String brand;
private String model;
private double price;
```

Ovo praktično znači da će svi objekti koji budu kreirani korišćenjem klase `Product` moći da budu karakterisani korišćenjem informacija o brendu, modelu i ceni. 

Upravo prikazana svojstva su privatna, što znači da im je moguće pristupiti samo iz klase u kojoj su definisana. 

### Metode **get** i **set** 

Za pristup privatnim svojstvima izvan klase `Product` koriste se **get** i **set** metode. Reč je o javnim metodama koje omogućavaju čitanje i izmenu vrednosti privatnih svojstava: 

```java
public String getBrand() {
	return brand;
}

public void setBrand(String brand) {
	this.brand = brand;
}

public String getModel() {
	return model;
}

public void setModel(String model) {
	this.model = model;
}

public double getPrice() {
	return price;
}

public void setPrice(double price) {
	this.price = price;
}
```

Za svako svojstvo definisane su po dve metode. Metode sa prefiksom **set** koriste se za postavljanje vrednosti privatnih svojstava, a metode sa prefiksom **get** za čitanje njihovih vrednosti. 

### Konstruktor 

Unutar klase `Product` postoji jedan konstruktor, što je zapravo metoda koja se poziva prilikom kreiranja objekata: 

```java
public Product(String brand, String model, double price) {
	this.brand = brand;
	this.model = model;
	this.price = price;
}
```

Unutar konstruktora se obavlja inicijalizacija svojstava objekta vrednostima koje su prilikom kreiranja objekta prosleđene konstruktoru. 

### Metoda `toString()` 

Klasa `Product` poseduje i metodu `toString()`, unutar koje je definisana logika za generisanje tekstualne reprezentacije objekta: 

```java
@Override
public String toString() {
	return "Brand='" + brand + '\'' + ", Model='" + model + '\'' + ", Price=" + price;
}
```

Pozivanjem metode `toString()` obavlja se ispis informacija o objektu, što podrazumeva ispis vrednosti njegovih svojstava. 


## Objekti 

Na osnovu upravo kreirane klase ćemo prvo obaviti kreiranje nekoliko objekata, a zatim ćemo se detaljnije upoznati sa upravo prikazanim elementima koji čine jednu klasu. Jedan objekat na osnovu klase `Product` može se kreirati na sledeći način: 

```java
Product product1 = new Product("Logitech", "F710", 129.99);
```

Ovo je primer kreiranja objekta na osnovu klase `Product`. Objekat se kreira upotrebom ključne reči `new`, nakon koje sledi poziv konstruktora, kome se prosleđuju vrednosti koje će biti dodeljene svojstvima. 

Proces kreiranja objekata se drugačije naziva instanciranje, pa se tako može reći da prikazana naredba oslikava instanciranje klase `Product`. Instanciranjem je u našem programu predstavljen prvi od tri proizvoda sa uvodnih slika 1.1. i 1.2. Naravno, na osnovu jedne klase može se stvoriti proizvoljan broj objekata, pa je tako korišćenjem klase `Product` u našem programu sada moguće predstaviti sve proizvode sa slika 1.1 i 1.2. 

Nad kreiranim objektima moguće je pozivati metodu `toString()`, koja će za rezultat imati generisanje tekstualne reprezentacije objekata: 

??? "Program.java"
    ```{.java title="// Program.java"}
    public class Main {
    	public static void main(String[] args) {
    		Product product1 = new Product("Logitech", "F710", 129.99);
    		Product product2 = new Product("HP", "Envy Photo 7155", 179.99);
    		Product product3 = new Product("Dell", "U2419H", 219.99);
    		System.out.println(product1);
    		System.out.println(product2);
    		System.out.println(product3);
    	}
    }
    ```

??? "Product.java"
	```{.java title="// Product.java"}
	public class Product {
		private String brand;
		private String model;
		private double price;
		
		public String getBrand() {
			return brand;
		}
		
		public void setBrand(String brand) {
			this.brand = brand;
		}
		
		public String getModel() {
			return model;
		}
		
		public void setModel(String model) {
			this.model = model;
		}
		
		public double getPrice() {
			return price;
		}
		
		public void setPrice(double price) {
			this.price = price;
		}
		
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

Na ovaj način na izlazu se stvara sledeći ispis: 

```console
Brand='Logitech', Model='F710', Price=129.99
Brand='HP', Model='Envy Photo 7155', Price=179.99
Brand='Dell', Model='U2419H', Price=219.99
```

-----

Na početku ove lekcije spomenuti su i pojmovi osnovnih postulata objektno orijentisanog programiranja. Reč je o apstrakciji, enkapsulaciji, nasleđivanju i polimorfizmu. O njima će biti reči u nastavku ove lekcije. 


## Apstrakcija 

Apstrakcija je princip objektno orijentisanog programiranja koji omogućava da se složeni entiteti iz realnog sveta modeluju baš onako kako mi želimo - sa nivoom detalja koji odgovara potrebama našeg programa. To znači da je u ovoj lekciji već ilustrovan primer apstrakcije i to upravo prilikom kreiranja klase `Product`. Njenim kreiranjem obavljeno je modelovanje proizvoda, odnosno tipa podatka koji je našem programu potreban. 


## Enkapsulacija 

Objekat predstavlja zaokruženu celinu, zato što u potpunosti opisuje jedan pojam iz realnog sveta. Unutar objekata objedinjuju se informacije i funkcionalnosti koje se tiču entiteta koji se modeluje. Objedinjavanje takvih informacija i funkcionalnosti drugačije se naziva enkapsulacija. 

I enkapsulacija je princip objektno orijentisanog programiranja koji je već ilustrovan na prikazanom primeru klase `Product`. Naime, enkapsulacijom se svojstva i metode `Product` objekata prezentuju kao celina, kojom se rukuje korišćenjem naziva promenljive koja čuva referencu na takav objekat. 

Enkapsulacija je ilustrovana i na primeru privatnih objektnih svojstava, kojima se izvan klase pristupa korišćenjem specijalnih metoda koje se koriste za upis i čitanje vrednosti privatnih svojstava. Postojanje **get** i **set** metoda omogućava kontrolisanu interakciju sa privatnim poljima, pa one predstavljaju još jedan svojevrstan primer enkapsulacije. 


## Nasleđivanje 

Nasleđivanje je još jedan postulat objektno orijentisanog programiranja koji omogućava kreiranje klasa koje svoje osobine i ponašanja nasleđuju od neke druge klase. U upravo prikazanom primeru smo kreirali samo jednu klasu (`Product`), tako da samostalno nismo definisali bilo kakvo nasleđivanje. Ipak, to ne znači da u primeru iz ove lekcije ne postoji nasleđivanje. Naime, sve klase u programskom jeziku Java implicitno nasleđuju osnovnu klasu tog jezika - klasu `Object`. 

`Object` je korena klasa u jeziku Java. To praktično znači da sve druge klase nju indirektno nasleđuju (slika 1.3). 

{{ macros.image("/images/AdvancedJavaProgramming/1_01_03.png", "Slika 1.3. Object je osnovna klasa Java jezika") }}

Na slici 1.3. možete da vidite hijerarhiju nasleđivanja između klasa u Java jeziku. Na vrhu takve hijerarhije nalazi se klasa `Object`. Sve klase u Javi mogu biti nasleđene. Nasleđena klasa postaje roditeljska klasa za sve klase koje je nasleđuju. Takođe, sve klase u Javi imaju svoju roditeljsku klasu, osim klase `Object` koja se nalazi na vrhu klasne hijerarhije. 

S obzirom na to da sve klase nasleđuju klasu `Object`, to znači i da naša klasa `Product` iz ove lekcije to čini. Ipak, primer modelovanja proizvoda u jednom Java programu idealan je za uvođenje nekoliko dodatnih konkretnijih klasa, koje bi nasledile već kreiranu klasu `Product`. Naime, različite grupe proizvoda se mogu predstaviti sopstvenim klasama, pa tako u primer možemo da uvedemo i nekoliko dodatnih klasa: 

- `Gamepad`, za predstavljanje kontrolera za video-igre 
- `Monitor`, za predstavljanje kompjuterskih monitora 
- `Printer`, za predstavljanje štampača 

Svaka od upravo navedenih klasa predstavlja specifičnu vrstu proizvoda, koji poseduju osobine koje ih razlikuju od drugih vrsta proizvoda. To znači da će u Java programu svaka od ovih klasa imati neka specifična svojstva. 

??? "Program.java"
	```{.java title="// Program.java"}
	public class Main {
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
	public class Product {
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

U sve tri klase koje nasleđuju klasu `Product` postoji identična logika. Svaka od klasa definiše po jednu dodatnu osobinu specifične grupe proizvoda. Klasa `Gamepad` poseduje svojstvo `wireless`, kojim je moguće definisati da li je reč o bežičnom kontroleru ili ne. Klasa `Monitor` poseduje svojstvo `diagonal`, kojim je moguće definisati veličinu dijagonale displeja u inčima. Na kraju, klasa `Printer` poseduje svojstvo `color`, koje se može koristiti kako bi se naznačilo da li štampač ima mogućnost štampe u boji. 

Sve tri klase poseduju po jedan konstruktor. Unutar njih, prvo se obavlja pozivanje roditeljskog konstruktora, korišćenjem posebne ključne reči `super`. Kada se ključna reč `super` upotrebi u obliku metode, njom se postiže pozivanje konstruktora roditeljske klase. Tako se konstruktor roditeljske klase upošljava kako bi obavio inicijalizaciju svojstava koja su definisana unutar klase `Product`, dok se unutar konkretnih klasa obavlja inicijalizacija samo onih svojstava koja su karakteristična za konkretne klase. 

Na kraju, svaka od upravo prikazanih konkretnih klasa koje predstavljaju proizvode poseduje i sopstvenu varijantu metode `toString()`. O tome će više reči biti u narednom poglavlju o polimorfizmu. 

### Klasni članovi koji se nasleđuju 

Nasleđivanjem, klasa dobija sve metode i svojstva roditeljske klase koji nisu obeleženi kao privatni. Privatna svojstva i metode se ne nasleđuju, ali se njima može pristupiti indirektno, ukoliko ih roditeljska klasa izlaže korišćenjem nekih metoda koje nisu privatne. Primer takvih metoda su upravo **get** i **set** metode koje postoje unutar `Product` klase. 

### Nasleđivanje i konstruktori 

Konstruktori su još jedan klasni element koji se ne nasleđuje. Ipak, kada se govori o konstruktorima i nasleđivanju, bitno je znati još jednu vrlo važnu osobinu jezika. Naime, već je poznato da se prilikom kreiranja objekata, odnosno instanciranja neke klase, obavlja pozivanje odgovarajućeg konstruktora. Java garantuje da će se prilikom kreiranja objekata pozvati konstruktor, pa čak i kada on unutar klase nije eksplicitno kreiran. U takvim situacijama u klasi postoji podrazumevani konstruktor koji nema parametara. 

Pored garancije da će konstruktor biti pozvan, Java garantuje da će prilikom instanciranja neke klase biti pozvan i konstruktor koji se nalazi unutar njene roditeljske klase. Takvu garanciju Java postiže tako što na početak svakog konstruktora postavlja naredbu za poziv konstruktora iz roditeljske klase. Na primer, kada unutar `Product` klase ne bi postojao konstruktor koji smo samostalno kreirali, Java bi za nas obavila kreiranje konstruktora sledećeg oblika: 

```java
public Product() {
	super();
}
```

Ovako bi izgledao podrazumevani konstruktor klase `Product` koji bi kompajler samostalno kreirao u slučaju da ga nismo eksplicitno definisali. Bitno je da primetite da se na početku takvog konstruktora nalazi naredba u kojoj se poziva konstruktor roditeljske klase. 
S obzirom na to da Java garantuje da će se konstruktor roditeljske klase uvek pozvati, kompajler dodaje naredbu za poziv roditeljskog konstruktora i na početak konstruktora koje samostalno kreiramo, ukoliko tako nešto mi ne učinimo. Kako biste ovo bolje razumeli, pogledajte sledeći konstruktor: 

```java
public Gamepad() {
	System.out.println("Hello from Gamepad constructor.");
}
```

Ovako može izgledati konstruktor unutar klase `Gamepad`, koja nasleđuje klasu `Product`. Ipak, s obzirom na to da uvek garantuje pozivanje roditeljskog konstruktora, Java kompajler će ovakav konstruktor modifikovati na sledeći način: 

```java
public Gamepad() {
	super();
	System.out.println("Hello from Gamepad constructor.");
}
```

Naredba `super()` je ono što Java kompajler dodaje za nas kako bi osigurao pozivanje roditeljskog konstruktora. Bitno je da razumete da Java kompajler uvek dodaje naredbu za poziv konstruktora bez parametara. Stoga, ukoliko se roditeljski konstruktor poziva eksplicitno, neophodno je da unutar roditeljske klase postoji konstruktor bez parametara, bilo da je reč o podrazumevanom ili o onom koji vi samostalno kreirate. Pošto mi unutar klase `Product` nemamo konstruktor bez parametara, u nasleđenim klasama se ne možemo osloniti na automatsko dodavanje naredbe `super()` od strane kompajlera (slika 1.4). 

{{ macros.image("/images/AdvancedJavaProgramming/1_01_04.png", "Slika 1.4. Problem koji može nastati kada roditeljska klasa ne poseduje podrazumevani konstruktor") }}

Ovakav problem se može rešiti na dva načina. Prvi podrazumeva kreiranje konstruktora bez parametara unutar roditeljske `Product` klase. Drugi način za rešavanje ovakve situacije jeste samostalno pozivanje konstruktora roditeljske klase, pri čemu bismo, naravno, pozvali onaj konstruktor koji unutar roditeljske klase postoji. 

Naredba `super()` za poziv roditeljskog konstruktora mora biti prva naredba unutar tela konstruktorske metode. 


## Polimorfizam 

Prilikom realizovanja nasleđivanja u objektno orijentisanom programiranju, veoma često dolazi do potrebe za redefinisanjem nekih nasleđenih ponašanja. Tako roditeljski objekat može definisati neku funkcionalnost koja ne zadovoljava u potpunosti njegove naslednike. Tako naslednici imaju mogućnost da nasleđeno ponašanje prilagode, dopune ili u potpunosti izmene. Na taj način se stvaraju različite verzije jednog istog ponašanja, odnosno verzije koje odgovaraju svakom pojedinačnom tipu objekata. Takva osobina objektno orijentisanog programiranja drugačije se naziva polimorfizam, odnosno višestruko značenje jednog istog pojma. 

Upravo opisana situacija postoji i unutar prikazanog primera. Naime, svaka od klasa poseduje metodu `toString()`, pri čemu je logika takve metode unutar svake od klasa različita. Metoda `toString()` potiče iz korene klase Java jezika - klase `Object`. To je jedna od nekoliko metoda koje postoje unutar ove klase i koje stoga nasleđuju sve ostale Java klase, kako one koje su ugrađene tako i one koje samostalno kreiramo. Upravo zbog toga i sve naše klase poseduju takvu metodu, bez ikakve potrebe da njenu logiku samostalno definišu. Ipak, izvorna logika `toString()` metode ne odgovara u potpunosti klasama koje smo mi samostalno kreirali. Kako biste ovo bolje razumeli, evo kako metoda `toString()` izgleda u svom izvornom obliku, unutar klase `Object`: 

```java
public String toString() {
	return getClass().getName() + "@" + Integer.toHexString(hashCode());
}
```

Izvorna logika `toString()` metode je takva da se unutar nje formira tekst koji se sastoji iz naziva klase kome sledi jedinstveni kod koji objekti dobijaju od strane virtualne mašine prilikom njihovog kreiranja. Reč je o kodu koji se dobija korišćenjem još jedne metode koja postoji unutar Object klase - metode `hashCode()`. Izvorna logika metode `toString()`, kao što možete da pretpostavite, daje prilično uopštenu tekstualnu reprezentaciju objekata. Na primeru klase `Product`, tekstualna reprezentacija jednog objekta dobijena od ovakve izvorne logike bi izgledala ovako: 

```console
Product@378bf509
```

Pored naziva klase, ovakav tekst za krajnjeg korisnika ne poseduje bilo kakve značajne informacije. Upravo zbog toga se u svakoj klasi koju smo samostalno kreirali u ovoj lekciji pribegava redefinisanju metode `toString()`. Tako sve klase poseduju sopstvenu logiku ove metode, koja odgovara skupu svojstava koja se unutar njih nalaze. Ovo je svojevrstan primer polimorfizma, odnosno višestrukog značenja jednog istog pojma. 

Proces redefinisanja propraćen je i upotrebom jedne posebne oznake (anotacije) koja se postavlja pre potpisa metode koja se redefiniše. Kako bi se naznačilo da je reč o redefinisanoj metodi, odnosno kako bi se naglasilo da metoda sa istim nazivom postoji i unutar roditeljske klase, pre potpisa metode postavlja se anotacija `@Override`. Bitno je znati da postavljanje anotacije `@Override` nije obavezno, odnosno da neće stvoriti grešku prilikom kompajliranja ili izvršavanja. Ipak, njeno korišćenje jeste dobra praksa, zato što poboljšava preglednost, jasno signalizirajući da je određena metoda redefinisana. Redefinisanje metoda se drugačije naziva **overriding**. 

Još jedan primer polimorfizma u Java programskom jeziku jeste mogućnost postojanja više metoda sa identičnim nazivima unutar jedne klase. Takvu situaciju je najbolje videti na primeru konstruktora. Naime, unutar jedne Java klase može postojati nekoliko konstruktora. Naravno, svi oni imaju identičan naziv koji odgovara nazivu klase, ali je neophodno da poseduju različite ulazne parametre: 

```java
public Product() {
	
}

public Product(String brand, String model, double price) {
	this.brand = brand;
	this.model = model;
	this.price = price;
}
```

Kod prikazuje dva konstruktora unutar klase `Product`. Naravno, i regularne metode se mogu upotrebiti u ovom obliku, sve dok poseduju različite ulazne parametre: 

```java
public int sum(int a, int b) {
	return a + b;
}
public int sum(int a, int b, int c) {
	return a + b + c;
}
```

Ovo su sada dve metode za sabiranje, koje poseduju identične nazive - `sum()`. Ipak, prva prihvata dva parametra, a druga tri, pa je njihovo postojanje unutar iste klase potpuno legitimno. Ovakva situacija se u Javi naziva **overloading**, odnosno preklapanje metoda i još jedan je od svojevrsnih primera polimorfizma.
