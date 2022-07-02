public class RectangleDecorator {
	protected Rectangle rectangle;
	
	public RectangleDecorator(Rectangle rectangle) {
		this.rectangle = rectangle;
	}
	
	public int perimeter() {
		return 2 * (this.rectangle.a + this.rectangle.b);
	}
}