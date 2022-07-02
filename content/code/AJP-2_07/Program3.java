public class Program3 {
  public static void main(String[] args) {

    for (Size size : Size.values()) {
        System.out.println(size.ordinal() + ": " + size + ", " + size.code);
    }
  }
}
