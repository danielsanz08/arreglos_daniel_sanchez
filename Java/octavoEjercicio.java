import java.util.Scanner;

public class octavoEjercicio {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int o = 0;
        System.out.println("Digita la cantidad de nombres de estudiantes que vas a digitar");
        int cantNombres = validarNumeroEntero(scanner);
        String[] nombres = new String[cantNombres];
        while (o < cantNombres) {
            System.out.println("Digita los nombres, no importa si son iguales");
            nombres[o] = scanner.next();
            o++;
        }

        System.out.println("Los nombres ingresados son:");
        for (String nombre : nombres) {
            System.out.print(nombre + " ");
        }
        System.out.println(" ");
        String[] nombresNodupicados = eliminarDuplicados(nombres);
        System.out.println("los nombres no duplicados son : ");
        for (int i = 0; i < nombresNodupicados.length; i++) {
            if (nombresNodupicados[i] != null) {

                System.out.print(nombresNodupicados[i] + " ");
            }
        }
    }

    public static String[] eliminarDuplicados(String[] vector) {
        for (int i = 0; i < vector.length; i++) {
            if (vector[i] != null) {
                for (int j = i + 1; j < vector.length; j++) {
                    if (vector[i].equals(vector[j])) {
                        vector[j] = null;
                    }
                }
            }
        }
        return vector;
    }

    public static int validarNumeroEntero(Scanner scanner) {
        while (true) {
            try {
                return Integer.parseInt(scanner.next());
            } catch (NumberFormatException e) {
                System.out.println("Error: Debe ingresar un número.");
            }
        }
    }
}


