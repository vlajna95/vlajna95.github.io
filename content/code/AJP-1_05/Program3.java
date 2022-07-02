import java.lang.reflect.*;

public class Program3 {
	public static void main(String[] args) {
		Class productClass = Product.class;
		Method[] methods = productClass.getMethods();
		for (Method method : methods) {
			System.out.println(method.getName());
		}
	}
}
