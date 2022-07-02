import java.io.*;

public class Program1 {
    public static void main(String[] args) {
        try (FileInputStream fs = new FileInputStream("my_file.txt")) {
            int content = fs.read();
            while (content != -1) {
                System.out.print((char) content);
                content = fs.read();
            }
        } catch (IOException exc) {
            System.out.println(exc.getMessage());
        }
    }
}
