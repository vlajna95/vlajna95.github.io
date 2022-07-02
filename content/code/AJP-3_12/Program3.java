import java.time.*;

public class Program3 {
    public static void main(String[] args) {

        LocalDate now = LocalDate.now();

        for (Month month : Month.values()) {
            System.out.println(month + " " + month.length(now.isLeapYear()));
        }
    }
}
