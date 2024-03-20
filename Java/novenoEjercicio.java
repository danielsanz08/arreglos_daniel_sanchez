import java.util.Random;
import java.util.Scanner;

public class novenoEjercicio {
    public static void main(String[] args) {
        int intentos = 5;
        int[] numeros = new int[intentos];
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int[] aleatorio = new int[1];

        for (int i = 0; i < aleatorio.length; i++) {
            aleatorio[i] = random.nextInt(101);
        }
        System.out.println("Tienes 5 intentos para adivinar el número aleatorio");
        for (int i = 0; i < intentos; i++) {
            System.out.println("digite un numero");
            int num = esEntero(scanner);
            numeros[i]=num;
            buscarNumero(aleatorio, num);
        }
        if (intentos==0){
            System.out.println("¡lo siento, pero no adivinaste!");
        }
        System.out.println("El número a adivinar era: ");
        for (int aleator: aleatorio){
            System.out.println(aleator);
        }
        System.out.print("Los números que digitaste: ");
        for (int numero: numeros){
            System.out.print(numero + " ");
        }
    }
    public static boolean buscarNumero(int[] vector,int numero) {
        for (int num : vector) {
            if (num > numero) {
                System.out.println("¡Frio, frio!");
                return true;
            }else if (num<numero){
                System.out.println("¡Caliente, Caliente!");
            }else{
                System.out.println("Haz atinado");
            }

        }
        return false;
    }
    public static int esEntero(Scanner scanner){
        while (true){
            try {
                return Integer.parseInt(scanner.next());
            }catch (NumberFormatException e){
                System.out.println("Error: ingrese un nuevo entero");
            }
        }
    }
}
