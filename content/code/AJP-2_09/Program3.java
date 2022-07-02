import java.util.*;

public class Program3 {
  public static void main(String[] args) {
      
        ArrayList listStudent = new ArrayList<>();
        ArrayList listPerson = new ArrayList<>();
        
        Person o = new Person();
        o.name = "John";
        
        Student s = new Student();
        s.name = "David";
        s.idNumber = "25/25";
        
        listPerson.add(o);
        listStudent.add(s);

        show(listPerson);
        show(listStudent);
    }
  
    static void show(ArrayList<? extends Person> os){
        for(Person o : os)
            System.out.println(o.name);
    }
}

