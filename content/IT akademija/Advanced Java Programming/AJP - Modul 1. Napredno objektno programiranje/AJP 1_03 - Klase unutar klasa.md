title: AJP 1.3. Klase unutar klasa
date: 2022-04-22 18:46
tags: Java, OOP, programiranje, klase, anonimne klase, anonimni objekti, lambda, referenciranje
summary: Klase unutar klasa u programskom jeziku Java
description: {summary}
series: Advanced Java Programming
series_index: 3
lang: sr


[TOC]

-----

{% import "macros.html" as macros %}


Klase se u Javi smeštaju unutar zasebnih fajlova čiji naziv mora biti identičan nazivu klase. Tako su sve klase koje smo do sada kreirali bile smeštane unutar zasebnih fajlova. Pored toga, unutar klasa, kao njihovi članovi, mogu se naći svojstva i metode. U ovoj lekciji ćete videti da klase, pored svojstava i metoda, mogu da sadrže i druge klase, što omogućava kreiranje klasa unutar klasa, odnosno postojanje većeg broja klasa unutar jednog fajla. Takođe, u ovoj lekciji ćete imati prilike da vidite da je klase moguće definisati i unutar metoda, a na kraju i to da Java omogućava i kreiranje klasa bez imena. Za početak, biće ilustrovan pojam klasa unutar klasa.


## Klase unutar klasa 

U programskom jeziku Java moguće je napraviti klasu koja se nalazi u okviru neke druge klase. Klase unutar klasa se drugačije nazivaju ugnežđene klase (_nested classes_ ili _inner classes_). Evo kako može izgledati jedan primer takve klase: 

```java
class OuterClass {
	...
	class NestedClass {
		...
	}
}
```

Prikazani primer ilustruje dve klase. Klasa OuterClass je glavna, odnosno spoljašnja klasa, unutar koje se kao član nalazi još jedna klasa – NestedClass. OuterClass se drugačije naziva klasa najvišeg nivoa (_top level class_), a NestedClass se drugačije naziva unutrašnja, odnosno ugnežđena klasa. 

### Zbog čega su nam potrebne klase unutar klasa? 

Postoje brojni scenariji u kojima je korisno koristiti ovakav pristup, koji omogućava smeštanje jedne klase unutar neke druge. Tri najjača aduta postojanja klasa unutar klasa su: 

**Grupisanje** 
: Smeštanje većeg broja klasa unutar jedne top-level klase naročito je korisno kada je potrebno obaviti logičko grupisanje klasa koje će biti korišćene samo na jednom mestu. Drugim rečima, ukoliko znamo da će određena klasa biti korišćena samo u okviru jedne klase, logično je nju ugraditi u takvu klasu, čime spoljašnja i unutrašnja klasa postaju jedna celina.

**Enkapsulacija** 
: Definisanje jedne klase kao člana neke druge klase može poboljšati enkapsuliranost koda. Naime, s obzirom na to da je ugnežđena klasa član klase u kojoj se nalazi, nad njom je moguće definisati različite modifikatore pristupa, a sve u zavisnosti od cilja koji je potrebno postići.

**Čitljivost** 
: Na kraju, klase unutar klasa mogu pozitivno da utiču na čitljivost koda, pošto se one nalaze blizu mesta u kodu na kome će biti korišćene. 


## Vrste ugnežđenih klasa 

Za početak će biti reči o dve vrste klasa koje mogu biti direktni klasni ili objektni članovi. U zavisnosti od toga da li je ugnežđena klasa objektni ili klasni član, razlikuju se dve vrste takvih klasa: 
	- nestatičke ugnežđene klase 
	- statičke ugnežđene klase 

Pored ove dve vrste ugnežđenih klasa, koje su direktni objektni ili klasni članovi, postoje i klase koje se mogu definisati unutar blokova koda, najčešće unutar metoda. Takve klase će biti predmet drugog dela ove lekcije. 

### Nestatičke ugnežđene klase 

Prva vrsta unutrašnjih klasa sa kojima ćemo se upoznati jesu klase koje su unutar svoje roditeljske klase još jedan objektni član. Reč je o klasama koje nisu statičke (već znamo da statički elementi pripadaju klasama, a oni koji nisu statički isključivo objektima koji se kreiraju korišćenjem takve klase). Takva je bila i unutrašnja klasa iz uvodnog primera u ovoj lekciji. 

Nestatičke ugnežđene klase predstavljaju nestatički član klase u kojoj se nalaze, baš kao bilo koje drugo polje ili metoda koji nisu označeni ključnom rečju `static`: 

```java
class OuterClass {
	private int i;
	
	private void m() {
		System.out.println(i);
	}
	
	class InnerClass {
		void accessOuterClass() {
			i = 1;
			m();
		}
	}
}
```

U prikazanom primeru definisana je jedna top-level klasa sa nazivom `OuterClass`, koja sadrži dva privatna člana: 
	- jedno polje sa nazivom `i` 
	- jednu metodu sa nazivom `m` 

Zatim je kreirana nestatička ugnežđena klasa sa nazivom `InnerClass` i u okviru nje metoda sa nazivom `accessOuterClass`. Svrha ove metode je demonstracija mogućnosti unutrašnjih klasa da pristupe članovima klase u kojoj se nalaze, pa čak i ako su oni označeni kao privatni. 

Ugnežđene nestatičke klase moguće je instancirati samo pomoću objekata klase u kojoj se nalaze. To praktično znači da se `InnerClass` može instancirati isključivo ukoliko se prethodno kreira objekat klase `OuterClass`: 

??? "OuterClass.java"
	```{.java title="// OuterClass.java"}
	class OuterClass {
		private int i;
		
		private void m() {
			System.out.println(i);
		}
		
		class InnerClass {
			void accessOuterClass() {
				i = 1;
				m();
			}
		}
	}
	```

??? "Program.java"
	```{.java title="// Program.java"}
	public class Program {
		public static void main(String[] args) {
			OuterClass outerObject = new OuterClass();
			OuterClass.InnerClass innerObject = outerObject.new InnerClass();
			innerObject.accessOuterClass();
		}
	}
	```

Instanciranje nestatičkih ugnežđenih klasa se vrlo retko obavlja na ovaj način, odnosno izvan matične klase unutar koje su takve klase definisane. Jednostavno, nestatičke ugnežđene klase su gotovo uvek namenjene za korišćenje unutar samih klasa u kojima su i kreirane. 

### Statičke ugnežđene klase 

Ugnežđene klase mogu biti i klasni članovi, odnosno, one se mogu deklarisati i kao statički elementi matične klase, tj. klase u kojoj se nalaze. U takvoj situaciji govorimo o statičkim ugnežđenim klasama: 

```java
class OuterClass {
	public int outerClassField;
	static class StaticNestedClass {
		...
	}
}
```

Jedina razlika u odnosu na prethodni primer jeste korišćenje ključne reči `static` prilikom deklarisanja klase. Stoga za ovakvu ugnežđenu klasu važi sve što i za ostale statičke elemente - oni postoje samo u domenu klase i moguće im je pristupiti korišćenjem imena matične klase, bez njenog prethodnog instanciranja: 

```java
OuterClass.StaticNestedClass obj = new OuterClass.StaticNestedClass();
```

Sada možete videti da se, za razliku od prethodnog primera, ugnežđene statičke klase mogu instancirati bez prethodnog instanciranja matične klase. 

**Iz statičkih ugnežđenih klasa ne može se pristupiti objektnim članovima matične klase.** 
Statičke ugnežđene klase nemaju pristup članovima objekata svoje matične klase. Upravo zbog toga unutar kreirane klase (`OuterClass`) i postoji jedno objektno polje. Ukoliko bismo njemu pokušali da pristupimo iz ugnežđene statičke klase, dobili bismo grešku kao na slici 3.1. 

{{ macros.image("/images/AdvancedJavaProgramming/1_03_01.png", "Slika 3.1. Primer nemogućnosti pristupa objektnom članu iz statičke ugnežđene klase") }}

Ponašanje koje vidite na slici 3.1. nije nikakvo iznenađenje. Naime, iz bilo kog statičkog konteksta nije moguće pristupiti nijednom objektnom elementu. Jednostavno, statički elementi se kreiraju prilikom pokretanja aplikacije, a objektni tek prilikom instanciranja određene klase, za svaki objekat zasebno. S obzirom na to da je reč o dva potpuno različita konteksta, statičkim elementima nije omogućen pristup objektnim. Po identičnom principu, ni unutar `main()` metode, koja je takođe statička, nije moguće pristupiti objektnim poljima i metodama glavne klase Java programa. 

**Samo unutrašnje klase mogu biti statičke** 
Jedina situacija u kojoj jedna klasa može biti statička jeste ukoliko je ona deo neke druge klase, odnosno ukoliko je reč o ugnežđenoj klasi. Drugim rečima, top-level klase ne mogu biti statičke, zato što statički mogu biti samo elementi klasa. 

**Kada koristiti statičke, a kada nestatičke unutrašnje klase?** 
Do sada su prikazane dve vrste ugnežđenih klasa: one koje pripadaju direktno klasi (statičke) i one koje pripadaju instancama klase u kojoj se nalaze. Nestatičke ugnežđene klase je bolje koristiti kada je iz ugnežđene klase potrebno pristupati objektnim poljima i metodama. Kada tako nešto nije neophodno, ugnežđena klasa može biti statička. 

::: question correct="statičke" answers="statičke|ugnežđene nestatičke|instancne|privatne" unique_name="klase_bez_pristupa_clanovima"
	Koji tip ugnežđenih klasa ne može pristupiti članovima klasa u okviru koje je ugnežđena klasa definisana? 

### Lokalne klase 

Ugnežđene klase mogu se javiti i unutar blokova. Opet je analogiju potrebno napraviti sa klasičnim promenljivama koje se deklarišu unutar blokova. Promenljiva unutar bloka naziva se lokalna promenljiva, pa se onda po identičnom principu i klase unutar bloka nazivaju lokalne klase. 
Najčešće se lokalne klase mogu sresti unutar metoda: 

```java
class OuterClass {
	void testMethod(int x) {
		int y = x * 2;
		
		class LocalClass {
			int a;
			int b;
			
			public LocalClass() {
				a = x;
				b = y;
			}
		}
		
		LocalClass lc = new LocalClass();
		System.out.println(lc.a);
		System.out.println(lc.b);
	}
}
```

Prikazani kod ilustruje primer lokalne klase. U okviru klase `OuterClass` postoji metoda sa nazivom `testMethod`. Ova metoda prihvata jedan ulazni parametar imenovan nazivom `x`. Unutar metode se formira vrednost lokalne promenljive `y`, a zatim se obavlja i kreiranje jedne lokalne klase sa nazivom `LocalClass`. 
`LocalClass` poseduje dva svojstva, a unutar konstruktora se postavljaju njihove vrednosti korišćenjem lokalnih promenljivih `x` i `y`. Nakon ovoga, unutar `testMethod()` metode instancira se lokalna klasa i ispisuju se vrednosti objektnih svojstava `a` i `b`. 

Kako bi se primer testirao, dovoljno je instancirati klasu `OuterClass` i pozvati metodu `testMethod()`: 

??? "OuterClass.java"
	```{.java title="// OuterClass.java"}
	class OuterClass {
		void testMethod(int x) {
			int y = x * 2;
			
			class LocalClass {
				int a;
				int b;
				
				public LocalClass() {
					a = x;
					b = y;
				}
			}
			
			LocalClass lc = new LocalClass();
			System.out.println(lc.a);
			System.out.println(lc.b);
		}
	}
	```

??? "Program.java"
	```{.java title="// Program.java"}
	public class Main {
		public static void main(String[] args) {
			OuterClass obj = new OuterClass();
			obj.testMethod(10);
		}
	}
	```

### Anonimne klase 

Svakako najznačajnija vrsta ugnežđenih klasa o kojima će biti reči u ovoj lekciji jesu klase koje se nazivaju anonimne. Reč je o klasama koje omogućavaju da se klasa deklariše i instancira odjednom i sve to u formi izraza. Tako nešto može zvučati zbunjujuće, stoga ćemo se sa pojmom anonimnih klasa upoznati na jednom realnom primeru: 

```java
import java.util.Timer;
import java.util.TimerTask;

public class JavaProgram {
	public static void main(String[] args) {
		System.out.println("Program started...");
		
		class MyTimerTask extends TimerTask {
			@Override
			public void run() {
				System.out.println("Hello World");
				System.exit(0);
			}
		}
		
		MyTimerTask myTimerTask = new MyTimerTask();
		Timer timer = new Timer("Timer");
		long delay = 5000L;
		timer.schedule(myTimerTask, delay);
	}
}
```

Ovo je primer Java programa koji na izlazu odmah nakon pokretanja ispisuje poruku `Program started...`, a nakon pet sekundi i poruku `Hello World`. Tako nešto je postignuto korišćenjem jedne ugrađene klase `Timer` i njene metode `schedule()`. Ova metoda prihvata dva parametra: 
	- objekat klase `TimerTask` 
	- numeričku vrednost koja diktira nakon koliko milisekundi je potrebno izvršiti određeni kod 

Prvi parametar metode `schedule()` posebno je interesantan za nas u ovom trenutku. Naime, on treba da bude objekat koji predstavlja instancu klase `TimerTask`. Ipak, ovu klasu nije moguće direktno instancirati, zato što je reč o apstraktnoj klasi, odnosno klasi koja je predviđena samo kao osnova za kreiranje konkretnih klasa. Pored toga, klasa `TimerTask` poseduje i jednu apstraktnu metodu koja se zove `run()`. Pošto je reč o apstraktnoj metodi, ona se mora implementirati prilikom nasleđivanja klase `TimerTask`. Upravo zbog toga je u prikazanom primeru obavljeno kreiranje konkretne klase `MyTimerTask`. Ona je nasledila klasu `TimerTask` i obezbedila implementaciju metode `run()`. Inače, metoda `run()` je upravo ona metoda koja će se aktivirati nakon definisanog vremena, posredstvom metode `schedule()` klase `Timer`. 

Nije teško uvideti da smo mi u primeru morali da obavimo dosta toga kako bismo uposlili metodu `schedule()`. Njeno pozivanje nas je nateralo da kreiramo sopstvenu klasu, da je zatim instanciramo i da tako dobijeni objekat na kraju prosledimo metodi `schedule()`. Sve to smo obavili korišćenjem pojma lokalnih klasa, o kojima je bilo reči u prethodnom segmentu. S obzirom na to da smo klasu `MyTimerTask` definisali unutar `main()` metode, reč je o lokalnoj klasi. Ipak, sve ovo se mnogo jednostavnije i elegantnije može obaviti korišćenjem anonimnih klasa: 

```java
import java.util.Timer;
import java.util.TimerTask;

public class JavaProgram {
	public static void main(String[] args) {
		System.out.println("Program started...");
		TimerTask myTimerTask = new TimerTask() {
			public void run() {
				System.out.println("Hello World");
				System.exit(0);
			}
		};
		Timer timer = new Timer("Timer");
		long delay = 5000L;
		timer.schedule(myTimerTask, delay);
	}
}
```

Sada je bitno da primetite da u primeru više nema klase `MyTimerTask` koja je postojala u prethodnom primeru. Njena deklaracija je zamenjena jednim izrazom u kome je iskorišćen koncept anonimnih klasa. Reč je o izrazu kojim promenljiva `myTimerTask` dobija referencu na objekat tipa `TimerTask`. Možete da vidite da se u takvom izrazu pojavljuje nešto sa čim se do sada nismo susretali. Reč je o instanciranju klase, koje nakon uobičajene logike za instanciranje sadrži i telo unutar vitičastih zagrada. U pitanju je upravo sintaksa za kreiranje anonimnih klasa: 

```java
new interface-or-class-name() { class-body }
```

Ovakva sintaksa nam omogućava da u jednoj naredbi obavimo nekoliko operacija: 
    - da kreiramo novu klasu bez imena, zbog čega se ona i zove anonimna klasa 
    - da takva anonimna klasa nasledi neku drugu klasu ili implementira određeni interfejs 
    - da se obavi instanciranje upravo kreirane anonimne klase 
    - da se referenca na dobijeni objekat anonimne klase spakuje unutar promenljive koja se nalazi na levoj strani izraza 

Kao što možete da vidite, procesom kreiranja anonimnih klasa u potpunosti se zaobilazi korak ručnog kreiranja konkretne klase. Pošto je reč o klasama koje nemaju ime, njih je moguće upotrebiti samo jednokratno, odnosno isključivo unutar izraza u kome promenljiva dobija vrednost. Izvan takvog izraza, anonimna klasa iz ovog primera ne postoji. Stoga su anonimne klase odlična jezička mogućnost u situacijama kao u prikazanom primeru, odnosno onda kada nema potrebe da eksplicitno kreiramo klasu samo kako bismo implementirali jednu metodu. 

**Anonimni objekti** 
Upravo prikazani primer je moguće i dodatno optimizovati. Naime, u priču je moguće uključiti i pojam anonimnih objekata, pa kod može postati još kompaktniji: 

```java
import java.util.Timer;
import java.util.TimerTask;

public class JavaProgram {
	public static void main(String[] args) {
		System.out.println("Program started...");
		Timer timer = new Timer("Timer");
		timer.schedule(new TimerTask() {
			public void run() {
				System.out.println("Hello World");
				System.exit(0);
			}
		}, 5000L);
	}
}
```

Sada je bitno da primetite da više nema naredbe u kojoj je obavljano dodeljivanje vrednosti promenljivoj `myTimerTask`. Štaviše, takve promenljive u kodu, praktično, više uopšte nema. Ipak, ukoliko želimo da budemo u potpunosti precizni, ona postoji, ali sada nije imenovana, zato što se objekat kreira baš na onom mestu na kome se i koristi - prilikom pozivanja metode `schedule()`. 


## Lambda izrazi 

Kada govorimo o anonimnim klasama u Java jeziku, nije moguće zaobići ni pojam lambda izraza. Reč je o jednoj lestvici iznad na skali apstraktnih rešenja koja postoje unutar jezika. To praktično znači da je za razumevanje lambda izraza prvo neophodno razumeti pojam anonimnih klasa. Stoga ćemo se i mi u nastavku sa lambda izrazima upoznati na jednom primeru koji će ilustrovati transformiranje jednog izraza sa anonimnom klasom u lambda izraz. Primer će ilustrovati filtriranje jednog niza celobrojnih vrednosti, korišćenjem ugrađenog skupa funkcionalnosti. Početni niz će izgledati ovako: 
```java
int[] numbers = {13, 8, -9, 15, -1, -78, 5, 69};
```

Želimo da u nastavku obavimo filtriranje ovog niza tako da dobijemo novi niz koji sadrži samo pozitivne vrednosti koje postoje unutar početnog niza. To ćemo obaviti korišćenjem funkcionalnosti koje postoje unutar Java platforme. Reč je o metodi `filter()` koja poseduje sledeći potpis: 
```java
IntStream filter(IntPredicate predicate);
```

`filter()` metoda postoji unutar `Stream` skupa funkcionalnosti, a kao svoj ulazni parametar prihvata podatak tipa `IntPredicate`. Reč je zapravo o interfejsu koji klasa mora implementirati kako bi njeni objekti mogli da se proslede metodi `filter()`. Stoga, osnovni oblik primera filtriranja može da izgleda ovako: 

```java
import java.util.Arrays;
import java.util.function.IntPredicate;

public class JavaProgram {
	public static void main(String[] args) {
		int[] numbers = {13, 8, -9, 15, -1, -78, 5, 69};
		
		class MyPredicate implements IntPredicate {
			@Override
			public boolean test(int value) {
				return (value > 0);
			}
		}
		
		MyPredicate myPredicate = new MyPredicate();
		numbers = Arrays.stream(numbers).filter(myPredicate).toArray();
		System.out.println(Arrays.toString(numbers));
	}
}
```

Ovo je primer koji je realizovan korišćenjem najbazičnijeg pristupa, koji ne podrazumeva upotrebu ni anonimnih klasa ni lambda izraza. Obavljeno je kreiranje nove lokalne klase sa nazivom `MyPredicate`. Ona je implementirala interfejs `IntPredicate`, a zbog toga i metodu `test()` koja je unutar takvog interfejsa definisana. 

**Metoda `test()` `IntPredicate` interfejsa** 
Metoda `test()` je inače metoda koja se u procesu filtriranja poziva nad svakim članom jednog niza. U zavisnosti od povratne vrednosti utvrđuje se da li će vrednost biti prisutna unutar finalnog niza ili ne. Metoda `test()` kao ulazni parametar dobija svaku od vrednosti niza pojedinačno. Ukoliko `test()` metoda kao svoju povratnu vrednosti vrati `true`, član će biti uvršćen u finalni niz. Ukoliko povratna vrednost bude `false`, to je signal da vrednost neće biti član finalnog niza. 

U prikazanom primeru logika metode `test()` je formulisana tako da proverava da li je prosleđena vrednost veća od nule. Ukoliko jeste, povratna vrednost metode će biti `true` i obrnuto. Na taj način će bilo koja pozitivna ulazna vrednost da proizvede `true` vrednost na izlazu, čime se postiže filtriranje niza o kojem smo govorili nešto ranije. 

**Funkcionalni interfejsi** 
Svaki interfejs koji u Java jeziku poseduje samo jednu apstraktnu metodu naziva se funkcionalni interfejs. Upravo takav je i interfejs `IntPredicate` koji je naša klasa implementirala u prikazanom primeru. 

Nakon kreiranja klase `MyPredicate` koja implementira potrebni interfejs obavljeno je njeno instanciranje. Dobijeni objekat je prosleđen metodi `filter()`. U primeru je bitno da primetite da se metoda `filter()` ne poziva direktno nad nizom, već da se on prvo pretvara u tok korišćenjem klase `Arrays` i njene metode `stream()`. Tokovi će biti detaljno obrađeni u jednoj od narednih lekcija ovog kursa. 

Na kraju, kada se ovakav primer pokrene, na izlazu se dobija: 
`[13, 8, 15, 5, 69]` 
Na osnovu izlaza možemo da zaključimo da je filtriranje uspešno obavljeno, jer na izlazu dobijamo samo pozitivne članove originalnog niza. 

Kao što je već rečeno, prikazani primer je postignut bez upotrebe anonimnih klasa i lambda izraza. Stoga će naš sledeći korak biti optimizacija prikazanog primera uključivanjem anonimnih klasa o kojima je bilo reči u prethodnom segmentu. Naime, vrlo je nepraktično kreirati potpuno novu klasu samo kako bi se implementirao jedan interfejs. Stoga se sve takve operacije mogu grupisati u izraz kojim se dobija jedan objekat anonimne klase: 

```java
import java.util.Arrays;
import java.util.function.IntPredicate;

public class JavaProgram {
	public static void main(String[] args) {
		int[] numbers = {13, 8, -9, 15, -1, -78, 5, 69};
		IntPredicate myPredicate = new IntPredicate() {
			@Override
			public boolean test(int value) {
				return (value > 0);
			}
		};
		numbers = Arrays.stream(numbers).filter(myPredicate).toArray();
		System.out.println(Arrays.toString(numbers));
	}
}
```

Tek nakon ove modifikacije, dolazimo i do pojma lambda izraza. Naime, prikazani primer je moguće još jednom optimizovati, upotrebom lambda izraza, koji omogućavaju da se prikazani kod drastično uprosti. Tako nešto signalizira i samo razvojno okruženje (slika 3.2). 

{{ macros.image("/images/AdvancedJavaProgramming/1_03_02.png", "Slika 3.2. Savet razvojnog okruženja da se anonimna klasa zameni lambda izrazom") }}

Ukoliko poslušamo razvojno okruženje i odaberemo opciju _Replace with lambda_, koju možete videti unutar prozora sa porukom, dobijamo kod koji izgleda ovako: 

```java
import java.util.Arrays;

public class JavaProgram {
	public static void main(String[] args) {
		int[] numbers = {13, 8, -9, 15, -1, -78, 5, 69};
		numbers = Arrays.stream(numbers).filter(value -> (value > 0)).toArray();
		System.out.println(Arrays.toString(numbers));
	}
}
```

Možete videti da se kod kompletnog primera sveo na tri osnovne naredbe unutar `main()` metode. Ona koja nas posebno interesuje jeste ono što se nalazi na mestu parametra metode `filter()`: 
```java
value -> (value > 0)
```

Isečak naredbe koji upravo vidite jeste lambda izraz. Lambda izrazi predstavljaju najkompaktniju sintaksu za kreiranje i instanciranje anonimnih klasa koje treba da implementiraju funkcionalni interfejs. To praktično znači da je lambda izraze moguće koristiti uvek kada je potrebno dobiti objekat koji nastaje instanciranjem anonimne klase koja implementira interfejs sa jednom apstraktnom metodom. Drugim rečima, lambda izrazom se u pozadini obavlja sledeće: 
    - kreira se anonimna klasa koja implementira funkcionalni interfejs 
    - obavlja se instanciranje kreirane anonimne klase 
Sve ovo se obavlja korišćenjem forme koja podseća na neku vrstu metode. 

Lambda izrazi se sastoje iz tri dela: 
    - **liste argumenata**, odnosno ulaznih parametara 
    - **tokena** (`->`), odnosno skupa karaktera koji se koriste za razdvajanje parametara i tela 
    - **tela**, odnosno logike koja predstavlja telo apstraktne metode koja se implementira 

Lako je zaključiti da je prilikom formiranja lambda izraza jedino bitno kako izgleda apstraktna metoda koju anonimna klasa implementira. Stoga je kod maksimalno uprošćen, odnosno, oslobođeni smo potrebe za definisanjem bilo koje propratne sintakse. Nije čak potrebno definisati ni tip interfejsa koji se implementira, pošto će on biti automatski detektovan u zavisnosti od ulaznog parametra metode. 

Sve ovo na kraju znači da lambda izraz koji smo kreirali u ovom primeru ima sledeće značenje: 
    - `value` - Naziv ulaznog parametra metode `test()` koja se implementira 
    - `->` - Token koji govori da je reč o lambda izrazu 
    - `(value > 0)` - Logika koja se nalazi unutar tela `test()` metode koja se implementira 

### Reference na metode 

U prethodnim redovima ste mogli da pročitate da se lambda izrazi mogu koristiti uvek kada je potrebno dobiti objekat koji nastaje instanciranjem anonimne klase koja implementira interfejs sa jednom apstraktnom metodom. Drugim rečima, lambda izraze je moguće koristiti u kombinaciji sa funkcionalnim interfejsima, odnosno interfejsima koji poseduju samo jednu apstraktnu metodu. Ipak, ponekad se lambda izrazi koriste samo kako bi se obavio poziv neke druge metode koja treba da obavi neku logiku. Kako biste bolje razumeli na šta se misli, pogledajte sledeći primer: 

```java
import java.util.Arrays;
import java.util.function.IntConsumer;

public class JavaProgram {
	public static void main(String[] args) {
		int[] numbers = {13, 8, -9, 15, -1, -78, 5, 69};
		Arrays.stream(numbers).forEach(new IntConsumer() {
			@Override
			public void accept(int value) {
				System.out.println(value);
			}
		});
	}
}
```

Primer podrazumeva korišćenje niza koji je već viđen u prethodnim primerima. Opet se pribegava pretvaranju niza u tok podataka, kako bismo nad takvim podacima mogli da pozovemo metodu `forEach()`. Reč je o metodi koja omogućava da se određena logika obavi nad svakim elementom toka. Mi smo u primeru ovu metodu iskoristili kako bismo ispisali vrednost svakog elementa, pa je tako primer analogan prolasku kroz niz korišćenjem neke petlje. 

Za realizaciju prikazanog primera iskorišćena je anonimna klasa, kako bi se dobio objekat tipa `IntConsumer` koji se mora proslediti metodi `forEach()`. Poznajući pojam lambda izraza, primer sada možemo modifikovati na sledeći način: 

```java
int[] numbers = {13, 8, -9, 15, -1, -78, 5, 69};
Arrays.stream(numbers).forEach(value -> System.out.println(value));
```

Tako može da izgleda identičan primer, ovoga puta realizovan korišćenjem lambda izraza. Anonimna klasa je zamenjena lambda izrazom i kod je postao znatno kompaktniji. 

Bitno je da primetite da se unutar tela lambda izraza nalazi samo poziv jedne metode. Reč je o metodi kojom se na izlazu ispisuje vrednost elementa. U ovakvoj situaciji, kada se telo lambda izraza sastoji samo iz poziva neke druge metode, lambda izraz je moguće pretvoriti u referencu na metodu. 

Referenca na metodu je najkompaktniji način za implementaciju funkcionalnog interfejsa kada se implementacija sastoji iz poziva neke druge metode. Evo kako se već prikazani primer može optimizovati još jednom, ovoga puta upotrebom reference na metodu: 
```java
Arrays.stream(numbers).forEach(System.out::println);
```

Metodi `forEach()` sada se prosleđuje referenca na metodu. Referenca na metodu se dobija navođenjem tipa unutar koga se metoda nalazi, nakon koga se koristi specijalna konstrukcija koja se sastoji iz dva karaktera dve tačke. Nakon dvostruke dve tačke, navodi se naziv metode čija se referenca prilaže. 

Bitno je primetiti još jednu osobinu referenci na metode, a ona se odnosi na odsustvo parametara. Jednostavno, prilikom definisanja reference na metodu ne prilažu se parametri, već prosleđivanje za nas obavlja sam kompajler. On u ovom slučaju ulazni parametar metode `accept()` automatski prosleđuje metodi `println()`. 
