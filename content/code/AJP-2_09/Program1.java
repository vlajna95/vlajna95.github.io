public class Program1 {
  public static void main(String[] args) {

    MyClass<Integer, String, Boolean> myClass1 = new MyClass<>(35, "My text", true);
    
    MyClass<Integer, Integer, Integer> myClass2 = new MyClass<>(35, 15, 22);

    System.out.println(myClass1.equals(myClass2));
  }
}

