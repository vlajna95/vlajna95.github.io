public class Program3 {
	public static void main(String[] args) {
		RectangleDecorator rd = new RectangleDecorator(new Rectangle(2, 3));
		System.out.println(rd.rectangle.area());
		System.out.println(rd.perimeter());
	}
}