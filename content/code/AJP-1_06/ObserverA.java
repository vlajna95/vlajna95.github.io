public class ObserverA implements Observer {
	String name;
	
	public ObserverA(String name){
		this.name = name;
	}
	
	@Override
	public void update(String msg) {
		System.out.println("Observer "+ name +". Message from observable: " + msg);
	}
}