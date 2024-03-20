import java.util.Scanner;

public class segundoEjercicio {
    public static void main(String[] args) {
        float[] ventas = new float[7];

        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < ventas.length; i++) {
            ventas[i] = -1;
        }
        System.out.println("0. Lunes, 1. Martes, 2. Miércoles, 3.Jueves, 4. Viernes, 5. Sábado, 6. Domingo");
        System.out.println("Digite el dia a registrar un valor");
        int dia = validarNumeroEntero(scanner);
        for(float vect : ventas){
            System.out.println("Digite el valor");
            float valor = validarNumeroFloat(scanner);
            ventas[dia] = valor;
            for (float venta : ventas){
                System.out.println(venta + ",");
            }
            break;

        }

        }
    public static float validarNumeroFloat(Scanner scanner) {
        while (true) {
            try {
                return Float.parseFloat(scanner.next());
            } catch (NumberFormatException e) {
                System.out.println("Error: Debe ingresar un número válido...");
            }
        }
    }
    public static int validarNumeroEntero(Scanner scanner) {
        while (true) {
            try {
                return Integer.parseInt(scanner.next());
            } catch (NumberFormatException e) {
                System.out.println("Error: Debe ingresar un número correctamente.");
            }
        }
    }
    }
