import java.util.Random;
import java.util.Scanner;

public class cuartoEjercicio {

    public static void main(String[] args) {
        int intentos = 3;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite el tamaño del vector");
        int tamaño = validarNumeroEntero(scanner);

        int[] vector = new int[tamaño];
        // Crear random
        Random random = new Random();
        for (int i = 0; i < vector.length; i++) {
            vector[i] = random.nextInt(100);
        }

        System.out.println("\nTiene 3 intentos para adivinar el número");
        for (int i = 0; i < intentos; i++) {
            System.out.println("Intento " + (i + 1));
            System.out.println("Digite un numero");
            int numero = validarNumeroEntero(scanner);
            int indice = buscarNumero(vector, numero);
            int[]intento={intentos};
            if (indice != -1) {
                System.out.println("¡Felicidades!, el numero está en el indice " + indice);

            } else {
                System.out.println("Lo siento! el numero no está en el vector");
            }
        }
        System.out.println("¡Lo siento, pero no adivinaste!");
        System.out.println("Los números en el vector son:");
        for (int v : vector) {
            System.out.println(v);
        }

    }

    public static int buscarNumero(int[] vector, int numero) {
        for (int i = 0; i < vector.length; i++) {
            if (vector[i] == numero) {
                return i;
            }
        }
        return -1;
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
