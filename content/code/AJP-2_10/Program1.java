import java.util.*;
import java.util.stream.*;

public class Program1 {
  public static void main(String[] args) {
      
        String[] cars = {"Honda", "Toyota", "Subaru"};
        Stream carsStream = Arrays.stream(cars);

        carsStream.forEach(System.out::println);
    }
}

