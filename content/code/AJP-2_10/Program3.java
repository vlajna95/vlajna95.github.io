import java.util.*;
import java.util.stream.*;
import java.util.function.*;

public class Program3 {
  public static void main(String[] args) {
      
        List<Integer> numbers = Arrays.asList(1, -2, 0, 22, 98, -434, -89, -66, 123);
        Stream<Integer> numbersStream = numbers.stream();
        
        ArrayList<Integer> numbersFiltrated = numbersStream.sorted(Comparator.reverseOrder()).collect(Collectors.toCollection(ArrayList::new));

        for (Integer num : numbers) {
            System.out.print(num + " ");
        }
        System.out.print("\n");
        for (Integer num : numbersFiltrated) {
            System.out.print(num + " ");
        }
    }
}

