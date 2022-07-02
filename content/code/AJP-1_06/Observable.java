public interface Observable {
	void addObserver(Observer s);
	void removeObserver(Observer s);
	void notifyObservers(String msg);
}