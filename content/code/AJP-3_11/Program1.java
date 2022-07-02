import java.util.stream.*;

public class Program1 {
  public static void main(String[] args) {
      
    String str = "first line \nsecond line \nthird line \nfourth line";
    Stream lines = str.lines();
    lines.forEach(System.out::println);
  }
}
