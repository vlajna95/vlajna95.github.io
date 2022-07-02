import java.util.regex.*;

public class Program3 {
  public static void main(String[] args) {
      
        String str = "This is some text, that will be searched for occurrences of word: some";
        
        String regex = "some";
        
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(str);
        
        int count = 0;
        while (matcher.find()) {
            count++;
            System.out.println("found: " + count + " : " + matcher.start() + " - " + matcher.end());
        }
  }
}
