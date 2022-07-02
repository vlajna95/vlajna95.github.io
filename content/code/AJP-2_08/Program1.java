import java.util.*;

public class Program1 {
    public static void main(String[] args) {
        ArrayList carBrands = new ArrayList() {
            {
                add("Honda");
                add("Toyota");
                add("Subaru");
                add("Acura");
                add("Lexus");
            }
        };
        System.out.println(carBrands);
        carBrands.add("Nissan");
        System.out.println(carBrands);
    }
}
