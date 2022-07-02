public class Viewer extends User {
	public Viewer(String username) {
		super(username);
		System.out.println("Viewer " + this.username + " created.");
	}
}