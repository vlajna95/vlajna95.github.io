import java.io.*;
import java.util.*;

public class Program2 {
    public static void main(String[] args) {
        System.out.print("Enter a number: ");
        Scanner scan = new Scanner(System.in);
        if (scan.hasNextInt()) {
            int number = scan.nextInt();
            System.out.println(number);
        } else
            System.out.println("You must enter a number!");
    }
}
