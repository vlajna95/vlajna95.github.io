public class Program2 {
  public static void main(String[] args) {
      
    String str = "This is a sentence.  This is a question, right?  Yes!  It is.";
    String[] wordArray = str.split("[ .,?!]+");
    
    System.out.println("Return Value: ");
    for (String s : wordArray) {
        System.out.println(s);
    }
  }
}

