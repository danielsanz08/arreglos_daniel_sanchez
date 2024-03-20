import java.util.Random;
import java.util.Scanner;

public class PrimerEjercicio {

    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        // Obtener la cantidad de estudiantes utilizando ValidadorEntero
        System.out.println("Ingresa la cantidad de estudiantes ");
        int cantAlumnos = validarNumeroEntero(scanner);

        int[] calificaciones = new int[cantAlumnos];
        for (int i = 0; i < calificaciones.length; i++) {
            calificaciones[i] = random.nextInt(101);
        }
        for (int i = 0; i < calificaciones.length; i++) {
            System.out.println("Las calificaciones son: " + calificaciones[i]);
        }

        int mayor = calificaciones[0];
        int menor = calificaciones[0];

        for (int nota : calificaciones) {
            if (nota < menor) {
                menor = nota;
            }
            if (nota > mayor) {
                mayor = nota;
            }
        }
        System.out.println("La nota más baja es: " + menor);
        System.out.println("La nota más alta es: " + mayor);
    }
    public static int validarNumeroEntero(Scanner scanner) {
        while (true) {
            try {
                return Integer.parseInt(scanner.next());
            } catch (NumberFormatException e) {
                System.out.println("Error: Debe ingresar una cantidad valida de alumnos.");
            }
        }
    }

}
