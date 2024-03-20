import java.util.Random;
import java.util.Scanner;

public class decimoEjercicio {
    public static void main(String[] args) {
        int intentos = 10;
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        System.out.println("Simulador de lanzamientos de dados");
        System.out.println("Tienes 10 intentos");
        System.out.println("1. lanzar los dados.\n 2. Dejarlos quietos");
        System.out.println("Digita una opcion");
        int op = esEntero(scanner);
        switch (op) {
            case 1:
                for (int i = 0; i < intentos; i++) {
                    int elemento1 = random.nextInt(1,6);
                    int elemento2 =random.nextInt(1,6);
                    int[]vector1={elemento1};//Aqui se van a almacenar las jugadas del dado1
                    int[]vector2 ={elemento2}; //Aqui lo mismo pero del dado 2

                    System.out.println("Dado 1: " + elemento1 + "| Dado 2: " + elemento2);
                    if (elemento1==elemento2){
                        System.out.println("Has sacado par ¡Ganado!");
                    }
                    System.out.println(" ");

                }

                break;
            case 2:
                System.out.println("Has dejado quieto los dados");

            default:
                System.out.println("Opción inválida ¡Adiós! \n By: Daniel Sánchez" );
                break;
        }

    }

    public static int esEntero(Scanner scanner) {
        while (true) {
            try {
                return Integer.parseInt(scanner.next());
            } catch (NumberFormatException e) {
                System.out.println("Error: ingrese un nuevo entero");

            }

        }
    }
}
