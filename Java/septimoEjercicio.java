import java.util.Scanner;

public class septimoEjercicio {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese la cantidad de letras ");
        int cantidad = esNumero(scanner);
        char[] letras = new char[cantidad];
        for (int i =0; i<cantidad;i++){
            letras[i]= (char) ('a'+ Math.random()*('z' - 'a'+1));
        }
        System.out.println("El vector es: ");
        for (char letra: letras){
            System.out.println(letra + " ");
        }
        System.out.println(" ");
        calcularFrecuencia(letras);
    }
    public static int esNumero(Scanner scanner){
        while (true){
            try {
                return Integer.parseInt(scanner.next());
            }catch (NumberFormatException e){
                System.out.println("Error: Debe ingresar un número.");
            }
        }
    }
    public static void calcularFrecuencia(char[] letras){
        int[] frecuencia = new int[26];
        for (char letra : letras){
            frecuencia[letra - 'a']++;
        }
        System.out.println("La frecuencia dec cada caracter");
        for (int i=0; i<frecuencia.length;i++){
            System.out.println((char) ('a'+i) + ": "+frecuencia[i]);
        }
    }
}
