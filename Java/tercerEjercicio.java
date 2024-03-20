import java.util.Scanner;

public class tercerEjercicio {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int mayorEdad = 0;
        int menorEdad = 0;
        System.out.println("Digite la cantidad de invitados: ");
        int cantInvitados = validarNumeroEntero(scanner);
        int[] edades = new int[cantInvitados];
        for (int i = 0; i < edades.length; i++) {
            System.out.print("Digite la edad del invitado: " + (i + 1) + " ");
            int edad =validarNumeroEntero(scanner);
                    edades[i] = edad;
        }
        System.out.print("Las edades en desorden son: ");
        for (int edad : edades) {
            System.out.print(edad + " ");
        }
        ordenar(edades);
        System.out.println(" ");


        System.out.print("Las edades en orden son: ");
        for (int age : edades) {
            System.out.print(age + " ");

        }
        System.out.println(" ");


        System.out.println("............");
        for (int i = 0; i < cantInvitados; i++) {
            if (edades[i] >= 18) {
                mayorEdad++;
            } else {
                menorEdad++;
            }

        }

        System.out.println("Los mayores de edad son: " + mayorEdad);
        System.out.println("Los menores de edad son: " + menorEdad);
    }

    public static void ordenar(int[] vector) {
        //inicia el ordenamiento
        int orden = vector.length;
        for (int i = 0; i < orden - 1; i++) {
            for (int j = 0; j < orden - i - 1; j++) {
                if (vector[j] > vector[j + 1]) {
                    int temp = vector[j];
                    vector[j] = vector[j + 1];
                    vector[j + 1] = temp;
                }
            }
        }
    }

    public static int validarNumeroEntero(Scanner scanner) {
        while (true) {
            try {
                int num = Integer.parseInt(scanner.next());
                if (num >= 1 && num <= 110) {// se pone hasta 110 porque hay personas que han llegado a esa edad
                    return num;
                } else {
                    System.out.println("Error: Debe ingresar un número entre 1 y 110 años.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Error: Debe ingresar un número válido.");
            }
        }
    }
}


