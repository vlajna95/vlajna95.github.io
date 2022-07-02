import java.time.*;

public class Program1 {
    public static void main(String[] args) {

        LocalDate localDate = LocalDate.of(1999, 12, 13);
        LocalTime localTime = LocalTime.of(17, 50);

        LocalDateTime localDateTime = LocalDateTime.of(localDate, localTime);

        System.out.println(localDateTime);
    }
}
