title: AJP 1.4. Događaji
date: 2022-04-22 19:24
tags: Java, OOP, programiranje, događaji
summary: Događaji u programskom jeziku Java
description: {summary}
series: Advanced Java Programming
series_index: 4
lang: sr


[TOC]

-----

{% import "macros.html" as macros %}


Do sada smo se susretali sa objektima koji unutar sebe poseduju svojstva i metode. Svojstva i metode su osnovni mehanizmi pomoću kojih se rukuje objektima. Pri tome, svojstvima se izlažu podaci, a metodama operacije. Ipak, veoma često se može javiti potreba da objekti budu u mogućnosti da spoljašnjem okruženju signaliziraju određena dešavanja do kojih može doći unutar njih. Tako dolazimo do pojma događaja, koji su veoma važan aspekt programiranja. Pojmu događaja biće posvećena lekcija pred vama. 


## Šta su događaji? 

Događaji omogućavaju da objekti spoljašnjem svetu pošalju neku vrstu signala, odnosno da obaveste sve zainteresovane subjekte o određenom dešavanju. Analogija se može napraviti sa različitim situacijama iz svakodnevnog života. Jedna takva situacija poznata je svim vozačima. Unutar rezervoara automobila nalazi se senzor koji prati nivo goriva. Onoga trenutka kada se nivo goriva spusti ispod određene vrednosti, na kontrolnoj tabli se aktivira indikator rezerve goriva. To je svojevrstan primer događaja. Kada takvog sistema izveštavanja ne bi bilo, mi bismo morali da samostalno vodimo računa o nivou napunjenosti rezervoara, što je svakako rešenje koje je daleko manje komforno. 
Događaji u programiranju funkcionišu po identičnom principu. Oni omogućavaju objektima da, baš kao i indikator rezerve goriva, spoljašnjem okruženju signaliziraju neke pojave koje su značajne za njihovo unutrašnje funkcionisanje. 

Programiranje koje podrazumeva praćenje i obradu događaja u toku izvršavanja aplikacije naziva se programiranje zasnovano na događajima (_event-based programming_). Događaji su posebno važan pojam u aplikacijama koje sadrže grafičko korisničko okruženje i različite kontrole koje korisnik upotrebljava kako bi upravljao programom (tastere, prozore, polja za unos vrednosti...). Ipak, to ne znači da je korišćenje događaja ograničeno na aplikacije sa grafičkim elementima. Događaji nisu striktno vezani za grafička okruženja, pa svoju primenu imaju i prilikom razvoja konzolnih aplikacija, što ćete imati prilike da vidite i u nastavku ove lekcije u kojoj će biti ilustrovan osnovni koncept rada sa događajima. 


## Kako funkcionišu događaji? 

Rukovanje događajima u programiranju podrazumeva postojanje nekoliko činilaca. Svi oni su ilustrovani slikom 4.1. 

{{ macros.image("/images/AdvancedJavaProgramming/1_04_01.png", "Slika 4.1. Različiti elementi koji učestvuju u životu jednog događaja") }}

Na slici 4.1. možete videti da rad sa događajima podrazumeva postojanje sledećih elemenata: 
	- **izvor događaja** (_event source_) - objekat ili klasa, odnosno generator koji proizvodi događaj 
	- **objekat događaja** (_event object_) - objekat koji reprezentuje događaj, odnosno objekat koji sadrži informacije o događaju do koga je došlo 
	- **slušalac**, odnosno **slušaoci događaja** (_event listener(s)_) - objekat, odnosno objekti koji će biti obavešteni kada do nekog događaja dođe; proces kojim neki objekat postaje slušalac često se naziva **pretplata na događaj**, a sami slušaoci **pretplatnici** (_subscribers_) 

U nastavku ove lekcije biće prikazano kako samostalno kreirati i emitovati jedan događaj. Takav događaj će zatim biti obrađen od strane nekoliko slušalaca događaja, što praktično znači da će oni dobiti dojavu o njegovom nastanku. 

Primer koji će biti prikazan u nastavku simuliraće alarm na budilniku. Stoga ćemo kreirati  klasu `Alarm`, čiji objekti će imati mogućnost da generišu jedan događaj. Događaj će se aktivirati nakon proticanja proizvoljne količine vremena, što je podatak koji će objekti klase `Alarm` moći da dobiju kao parametar. Na kraju, klasa `Alarm` će posedovati i logiku za registrovanje svih objekata koje je potrebno obavestiti o pojavi događaja. 


## Kreiranje klase događaja 

U prethodnim redovima ste mogli da pročitate da se događaji u programu predstavljaju korišćenjem objekata događaja. Objekat događaja je ono što generator događaja prosleđuje svim slušaocima. Kako bismo bili u mogućnosti da kreiramo objekat događaja, potrebna nam je klasa čijim instanciranjem će biti stvoren takav objekat. 
Osnovna klasa kojom se u Java programskom jeziku predstavljaju događaji jeste klasa `EventObject`: 

```java
import java.util.EventObject;

public class AlarmEvent extends EventObject {
	...
}
```

Na ovaj način kreirana je klasa `AlarmEvent` koja će u našem programu da predstavlja događaj aktiviranja alarma na budilniku. Ova klasa nasleđuje upravo spomenutu klasu `EventObject`. Reč je o konkretnoj klasi koja poseduje samo jedan konstruktor sa jednim parametrom. Parametar se odnosi na referencu na objekat koji je izazvao događaj. Sve to praktično znači da smo nasleđivanjem klase `EventObject` mi u obavezi da samostalno definišemo konstruktor koji će da pozove konstruktor roditeljske klase i da mu prosledi referencu na objekat koji je generator događaja. Naravno, kao i uvek prilikom nasleđivanja, imamo mogućnost da objekat događaja proširimo, odnosno da definišemo još neke osobine događaja. To ćemo i učiniti, uvođenjem još jednog svojstva, koje će predstavljati poruku događaja: 

```java
import java.util.EventObject;

public class AlarmEvent extends EventObject {
	String message;
	
	public AlarmEvent(Object source, String message) {
		super(source);
		this.message = message;
	}
}
```

::: question correct="EventObject" answers="EventObject|EventClass|EventAction|Event" unique_name="klasa_objekta_za_event"
	Objekat kojim se predstavlja događaj kreira se na osnovu klase: 


## Kreiranje interfejsa za predstavljanje slušalaca 

Sledeći korak u procesu kreiranja primera upotrebe događaja biće kreiranje interfejsa kojim će biti predstavljeni slušaoci. Naime, želimo da obezbedimo da naš događaj aktiviranja alarma može da dobije objekat bilo koje klase, odnosno želimo da omogućimo objektima svih tipova da budu slušaoci našeg događaja. Ipak, kao što ćete uskoro videti, klasa koja će generisati događaj mora na neki način rukovati svim pretplatnicima. Kako se ne bismo ograničavali na neki konkretan tip, za predstavljanje svih slušalaca ćemo iskoristiti apstrakciju, oličenu u jednom interfejsu: 

```java
public interface AlarmListener {
	void alarmRang(AlarmEvent event);
}
```

Ovo je interfejs koji će morati da implementiraju svi konkretni tipovi koji žele da dobijaju dojavu o aktiviranju alarma budilnika. Tako smo na ovaj način efikasno predstavili sve slušaoce korišćenjem apstraktnog tipa koji je predstavljen interfejsom. 

Bitno je da primetite i to da se unutar interfejsa nalazi i jedna metoda. Iz prethodnih lekcija znamo da je ovako definisana metoda javna i apstraktna, stoga će sve konkretne klase morati da je implementiraju. Reč je o metodi koja će se unutar slušalaca aktivirati kada dođe do pojave događaja. 


## Kreiranje generatora događaja 

Element koji nedostaje jeste klasa unutar koje će doći do emitovanja događaja. Nju smo spomenuli na početku ove lekcije - reč je o klasi sa nazivom `Alarm`. Klasa `Alarm` će omogućiti aktiviranje alarma na budilniku nakon isticanja određene količine vremena. 

Pored funkcionalnosti koja će omogućiti aktiviranje alarma, unutar klase `Alarm` je neophodno da postoji i logika koja će omogućiti rukovanje svim pretplatnicima. Stoga je kreiranje klase koja će generisati događaj korak u kome se objedinjuju svi elementi koje smo do sada kreirali. 

Klasa koja generiše događaj unutar sebe mora imati referencu na sve pretplatnike. Takođe, dobra je praksa da se unutar generatora događaja obezbedi i logika za ukidanje nekih objekata iz liste pretplatnika. Sve to praktično znači da unutar klase Alarm moramo da kreiramo i dve metode koje će se koristiti za dodavanje i uklanjanje slušalaca događaja. S obzirom na to da slušalaca može biti više, njihove reference moramo čuvati unutar niza: 

```java
import java.util.Timer;
import java.util.TimerTask;

public class Alarm {
	private AlarmListener[] listeners = {};
	
	public void addListener(AlarmListener alarmListener) {
		AlarmListener[] newListeners = new AlarmListener[listeners.length+1];
		System.arraycopy(listeners, 0, newListeners, 0, listeners.length);
		newListeners[listeners.length] = alarmListener;
		listeners = newListeners;
	}
	
	public void removeListener(AlarmListener alarmListener) {
		int indexOfElementToRemove = -1;
		for (int i = 0; i < listeners.length; i++){
			if (alarmListener.equals(listeners[i])) {
				indexOfElementToRemove = i;
			}
		}
		AlarmListener[] newListeners = new AlarmListener[listeners.length-1];
		System.arraycopy(listeners, 0, newListeners, 0, indexOfElementToRemove);
		System.arraycopy(listeners, indexOfElementToRemove+1, newListeners, indexOfElementToRemove, listeners.length-indexOfElementToRemove-1);
		listeners = newListeners;
	}
	
	public void setTimeFromNow(int millis) {
		Timer timer = new Timer("Timer");
		timer.schedule(new TimerTask() {
			public void run() {
				System.out.println("AlarmEvent triggered...");
				for (AlarmListener listener : listeners) {
					AlarmEvent eventObj = new AlarmEvent(this, "Time is up!");
					listener.alarmRang(eventObj);
				}
				System.exit(0);
			}
		}, millis);
	}
}
```

Kod predstavlja kompletnu logiku klase `Alarm`. Ona se zapravo sastoji iz jednog niza i tri metode: 
	- `AlarmListener[] listeners` - niz unutar koga će biti smeštani slušaoci 
	- `void addListener(AlarmListener alarmListener)` - metoda za registrovanje slušaoca 
	- `void removeListener(AlarmListener alarmListener)` - metoda za uklanjanje slušaoca 
	- `void setTimeFromNow(int millis)` - metoda za aktiviranje alarma 

S obzirom na to da nizovi u Javi moraju imati fiksnu, unapred utvrđenu dužinu, unutar metoda `addListener()` i `removeListener()` postavljena je logika koja prilikom svakog dodavanja ili uklanjanja slušaoca kreira novi niz koji na kraju dodeljuje objektnom svojstvu `listeners`. Tako ovo svojstvo na kraju uvek poseduje niz čija je dužina tačno onolika koliko ima i registrovanih slušalaca. Kada se dodaje novi slušalac, prvo se kreira novi niz sa jednim elementom više u odnosu na postojeći niz. Postojeći niz se kopira u novi niz, a zatim se na kraj dodaje još jedan, novi slušalac. 
Uklanjanje slušaoca se obavlja po sličnom principu. Prvo se kreira novi niz, čija je dužina za jedan element manja od dužine postojećeg niza. Zatim se utvrđuje na kom indeksu se nalazi element koji je potrebno ukloniti. Na kraju se u novi niz kopiraju svi elementi iz starog, osim elementa koji se uklanja. Kopiranje se obavlja iz dva dela, tako što se prvo kopiraju svi elementi pre elementa koji se uklanja, a zatim i svi elementi koji se nalaze nakon elementa koji se uklanja. 

Metoda `setTimeFromNow()` koristi se za aktiviranje logike klase `Alarm`. To je metoda koja će aktivirati alarm nakon vremena u milisekundama koje se ovoj metodi prosledi kao parametar. Kao pomoć za formiranje takve logike iskorišćene su klase `Timer` i `TimerTask`, o kojima je bilo reči u jednoj od prethodnih lekcija. Kada istekne vreme koje je metodi `setTimeFromNow()` prosleđeno kao ulazni parametar, aktivira se metoda `run()` i unutar nje logika kojom se obavlja emitovanje događaja. 

Emitovanje događaja se zapravo sastoji iz prolaska kroz niz svih slušalaca i pozivanje metode `alarmRang()`, čija implementacija se nalazi unutar njih. Metodi `alarmRang()` se prosleđuje objekat događaja, sa osnovnim informacija o događaju (sa referencom na objekat koji je proizveo događaj i porukom). Tako svi slušaoci bivaju obavešteni o pojavi događaja. 


## Pretplata na događaje 

U dosadašnjem toku ove lekcije realizovali smo sve elemente koji su neophodni za obradu događaja. Preostaje još da kreiramo slušaoce i da ih pretplatimo na dobijanje dojave o pojavi događaja. 

Događaj koji je predstavljen `AlarmEvent` klasom mogu da slušaju svi objekti čija klasa implementira interfejs `AlarmListener`. Možemo da napravimo i neku posebnu klasu, čiji će objekti biti slušaoci, ali isto tako, možemo da iskoristimo i glavnu klasu našeg Java programa kako bi primer ostao što jednostavniji: 

```java
public class Program implements AlarmListener {
	public static void main(String[] args) {
		// ...
	}
	
	@Override
	public void alarmRang(AlarmEvent e) {
		System.out.print(e.message);
		System.out.println(" Wake up!!!");
	}
}
```

Klasa `Program` je implementirala interfejs `AlarmListener` i tako je postala legitiman tip slušaoca događaja `AlarmEvent`. Implementiranje interfejsa `AlarmListener` obavezuje klasu da poseduje i metodu `alarmRang()`. To je metoda koja će se aktivirati kada dođe do pojave događaja. 

Preostaje još da unutar `main()` metode dodamo i finalni kod kojim će biti kreirano nekoliko objekata-slušalaca. Oni će biti pretplaćeni na slušanje `AlarmEvent` događaja. Na kraju će biti dodat i kod kojim će se aktivirati logika klase `Alarm`, koja će nakon nekog vremena da proizvede `AlarmEvent` događaj: 

??? "Alarm.java"
	```{.java title="// Alarm.java"}
	import java.util.Timer;
	import java.util.TimerTask;
	
	public class Alarm {
		private AlarmListener[] listeners = {};
		
		public void addListener(AlarmListener alarmListener) {
			AlarmListener[] newListeners = new AlarmListener[listeners.length+1];
			System.arraycopy(listeners, 0, newListeners, 0, listeners.length);
			newListeners[listeners.length] = alarmListener;
			listeners = newListeners;
		}
		
		public void removeListener(AlarmListener alarmListener) {
			int indexOfElementToRemove = -1;
			for (int i = 0; i < listeners.length; i++){
				if (alarmListener.equals(listeners[i])) {
					indexOfElementToRemove = i;
				}
			}
			AlarmListener[] newListeners = new AlarmListener[listeners.length - 1];
			System.arraycopy(listeners, 0, newListeners, 0, indexOfElementToRemove);
			System.arraycopy(listeners, indexOfElementToRemove + 1, newListeners, indexOfElementToRemove, listeners.length-indexOfElementToRemove-1);
			listeners = newListeners;
		}
		
		public void setTimeFromNow(int millis) {
			Timer timer = new Timer("Timer");
			timer.schedule(new TimerTask() {
				public void run() {
					System.out.println("AlarmEvent triggered...");
					for (AlarmListener listener : listeners) {
						AlarmEvent eventObj = new AlarmEvent(this, "Time is up!");
						listener.alarmRang(eventObj);
					}
					System.exit(0);
				}
			}, millis);
		}
	}
	```

??? "AlarmEvent.java"
	```{.java title="// AlarmEvent.java"}
	import java.util.EventObject;
	
	public class AlarmEvent extends EventObject {
		String message;
		
		public AlarmEvent(Object source, String message) {
			super(source);
			this.message = message;
		}
	}
	```

??? "AlarmListener.java"
	{.java title="// AlarmListener.java"}
	public interface AlarmListener {
		void alarmRang(AlarmEvent event);
	}
	```

??? "Program.java"
	{.java title="// Program.java"}
	public class Program implements AlarmListener {
		public static void main(String[] args) {
			Program program = new Program();
			Program program1 = new Program();
			Program program2 = new Program();
			Alarm alarm = new Alarm();
			alarm.addListener(program);
			alarm.addListener(program1);
			alarm.addListener(program2);
			alarm.setTimeFromNow(2000);
		}
		
		@Override
		public void alarmRang(AlarmEvent e) {
			System.out.print(e.message);
			System.out.println(" Wake up!!!");
		}
	}
	```

Unutar `main()` metode prvo je obavljeno kreiranje tri objekta klase `Program`. Zatim je kreiran objekat klase `Alarm`. Njemu su dodati slušaoci, prosleđivanjem kreiranih objekata metodi `addListener()`. Poslednjom naredbom, unutar `main()` metode aktiviran je alarm budilnika. S obzirom na to da je prosleđena vrednost 2000, alarm će se aktivirati nakon dve sekunde. Aktiviranje alarma značiće i emitovanje `AlarmEvent` događaja. Sve će to na kraju, nakon dve sekunde, unutar konzole da proizvede sledeći rezultat: 

```output
AlarmEvent triggered...
Time is up! Wake up!!!
Time is up! Wake up!!!
Time is up! Wake up!!!
```

Prva poruka potiče iz klase `Alarm` i metode `run()` koja se aktivira nakon isteka prosleđene količine vremena. Ona se aktivira jednom, a unutar nje, kao što ste nešto ranije mogli da vidite, obavlja se obaveštavanje svih slušalaca događaja. Njih je u primeru tri i upravo zbog toga se na izlazu dobijaju tri identične poruke `Time is up! Wake up!!!`. Ovo praktično znači da se metoda `alarmRang()` aktivirala tri puta, odnosno nad svakim od objekata-slušalaca po jednom. Pri tome je bitno da primetite da je tekst `Time is up!` došao zajedno sa samim objektom događaja, unutar njegovog svojstva `message`. Takvom tekstu je zatim unutar metode za obradu događaja dodat nastavak `Wake up!!!`. 
