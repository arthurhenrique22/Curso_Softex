class divisao{
    public static void main (String[] args){
        int a = 10, b = 5, c = 5, resultado;
        try {
           resultado = a / (b - c);
           System.out.println("Resultado" + resultado); 
        
        }
        catch(ArithmeticException ex){
            System.out.println("Excepetion: Contas de divisão não pode ser dividido por 0");
        }
    }
}