public class Program1 {
	public static void main(String[] args) {
		Logger logger = Logger.getInstance();
		Logger logger1 = Logger.getInstance();
		System.out.println(logger.equals(logger1));
	}
}