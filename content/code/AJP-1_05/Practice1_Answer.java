import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Parameter;

public class Practice1_Answer {
	public static void main(String[] args) throws InvocationTargetException, IllegalAccessException, ClassNotFoundException {
		Class c = Class.forName("Practice1");
		Practice1 myClass = new Practice1();
		String stringArgument = "John";
		Method[] methods = c.getDeclaredMethods();
		for (Method method : methods) {
			System.out.println("Invoking of method: " + method.getName());
			if (method.getParameterCount() > 0) {
				Parameter[] param = method.getParameters();
				if (param.length == 1) {
					if (param[0].getType() == String.class) {
						method.invoke(myClass, stringArgument);
					}
				}
			}
			else {
				method.invoke(myClass);
			}
		}
	}
}
