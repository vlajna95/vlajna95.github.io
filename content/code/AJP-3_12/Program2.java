import java.time.*;

public class Program2 {
    public static void main(String[] args) throws InterruptedException {

        LocalTime time1 = LocalTime.now();
        Thread.sleep(1000);
        LocalTime time2 = LocalTime.now();
        
        Duration duration = Duration.between(time1, time2);
        System.out.println(duration.getSeconds());
    }
}
