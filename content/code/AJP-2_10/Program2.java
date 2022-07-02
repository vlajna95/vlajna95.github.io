import java.util.*;
import java.util.stream.*;
import java.util.function.*;

public class Program2 {
  public static void main(String[] args) {
      
    List <Integer> numbers = Arrays.asList(1, -2, 0, 22, 98, -434, -89, -66, 123);
    Stream <Integer> numbersStream = numbers.stream();

    numbersStream.filter(value -> (value > 0)).forEach(System.out::println);
  }
}
