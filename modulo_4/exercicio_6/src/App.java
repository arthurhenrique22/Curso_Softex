import java.io.*;


class Emp implements Serializable {

private static final long serialversaoUID = 123780078L;

    transient int a;
    static int b;
    String nome;
    int id;

    public Emp(String nome, int id, int a, int b){
        this.nome = nome;
        this.id = id;
        this.a = a;
        this.b = b;
    } 
}

class Serial{
   
    public static void printdados(Emp object1){
        System.out.println("nome: " + object1.nome);
        System.out.println("Idade: " + object1.id); 
        System.out.println("a: " + object1.a);
        System.out.println("b: " + object1.b);
    }


    public static void main(String[] args) throws ClassNotFoundException{
        Emp object = new Emp("Arthur",  18, 4, 1000);
        String filenome = "arthur.txt";

        try {
            FileOutputStream file = new FileOutputStream(filenome);

            ObjectOutputStream saida = new ObjectOutputStream(file);
        
            saida.writeObject(object);

            saida.close();
            file.close();

            System.out.println("Objeto foi serializado\n"
                            + "Antes da deseserialização");
            
             printdados(object);

             object.b = 2004; 
        
        }
        catch (IOException ex) {
            System.out.println("IOExcepition !!");
        }

        object = null;
        
        try {
            FileInputStream file = new FileInputStream(filenome);

            ObjectInputStream in = new ObjectInputStream(file);

            object = (Emp)in.readObject();

            in.close();
            file.close();
            System.out.println("Objeto foi deserializado\n"
            + "Dados depois da deseserialização");

            printdados(object);
        }
        catch (IOException ex){
            System.out.println("IOException !!");
        }
        catch (ClassNotFoundException ex){
            System.out.println("ClassNotFoundException !!");
        }
    }
}

