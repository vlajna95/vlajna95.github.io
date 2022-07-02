import java.lang.reflect.*;

public class Program {
	public static void main(String[] args) throws ClassNotFoundException {
		Class stringClass = String.class;
		String className = stringClass.getName();
		String simpleClassName = stringClass.getSimpleName();
		int modifiers = stringClass.getModifiers();
		Package classPackage = stringClass.getPackage();
		Class superclass = stringClass.getSuperclass();
		System.out.println(className);
		System.out.println(simpleClassName);
		System.out.println("Is private: " + Modifier.isPrivate(modifiers));
		System.out.println("Is public: " + Modifier.isPublic(modifiers));
		System.out.println("Is final: " + Modifier.isFinal(modifiers));
		System.out.println(classPackage.getName());
		System.out.println(superclass.getName());
	}
}