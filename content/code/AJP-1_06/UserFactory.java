public class UserFactory {
	public static User newUser(String userType, String username) {
		User user = switch(userType) {
			case "viewer" -> new Viewer(username);
			case "admin" -> new Admin(username);
			case "superuser" -> new Superuser(username);
			default -> null;
		};
		return user;
	}
}