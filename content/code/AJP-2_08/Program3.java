import java.util.*;

public class Program3 {
    public static void main(String[] args) {

        HashSet myCollection = new HashSet();
        
        myCollection.add("One");
        myCollection.add("Two");
        myCollection.add("Three");
        myCollection.add("Four");
        myCollection.add("Five");
        
        myCollection.add("One");
        
        Iterator i = myCollection.iterator();
        
        while (i.hasNext()) {
            System.out.println(i.next());
        }
    }
}
