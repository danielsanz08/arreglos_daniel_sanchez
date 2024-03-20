import java.util.Random;
import java.util.Scanner;
public class cuartoEjercicio {

    public static void main(String[] args) {
        int intentos = 3;
        int g=0;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite el tamaño del vector");
        int tamaño = validarNumeroEntero(scanner);

        int[] vector = new int[tamaño];
        //Crear random
        Random random = new Random();
        for (int i = 0; i < vector.length; i++) {
            vector[i] = random.nextInt(100);
        }

        System.out.println(" ");
        System.out.println("Tiene 3 intentos para adivinar el numero");
        for (int i = 0; i < intentos; i++) {
        while (g<intentos){
            System.out.println("Digite un numero");
            int numero = validarNumeroEntero(scanner);
            if (buscarNumero(vector, numero)) {
                System.out.println("¡Felicidades!, el numero está en el vector");
                break;
            } else {
                System.out.println("Lo siento! el numero no está en el vector");
            }
            g++;
        }
        }

        if (intentos == 0) {
            System.out.println("¡lo siento, pero no adivinaste!");

        }
        //temporal
        System.out.println("Vector generado:");
        for (int i = 0; i < tamaño; i++) {
            System.out.print(vector[i] + " ");

        }
    }

    public static boolean buscarNumero(int[] vector, int numero) {
        for (int num : vector) {
            if (num == numero) {
                return true;
            }
        }
        return false;
    }

    public static int validarNumeroEntero(Scanner scanner) {
        while (true) {
            try {
                return Integer.parseInt(scanner.next());
            } catch (NumberFormatException e) {
                System.out.println("Error: Debe ingresar un número entero.");
            }
        }
    }

}