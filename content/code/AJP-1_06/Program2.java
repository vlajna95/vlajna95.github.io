public class Program2 {
	public static void main(String[] args) {
		Subject subject = new Subject();
		Observer o1 = new ObserverA("Observer 1");
		Observer o2 = new ObserverA("Observer 2");
		Observer o3 = new ObserverA("Observer 3");
		subject.addObserver(o1);
		subject.addObserver(o2);
		subject.addObserver(o3);
		subject.notifyObservers("new update");
		subject.removeObserver(o2);
		subject.removeObserver(o1);
		subject.notifyObservers("new update1");
	}
}