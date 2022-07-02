import java.lang.reflect.*;

public class Program2 {
	public static void main(String[] args) {
		Class productClass = Product.class;
		Field[] fields =  productClass.getDeclaredFields();
		for (Field field : fields) {
			System.out.println(field.getName());
		}
	}
}
