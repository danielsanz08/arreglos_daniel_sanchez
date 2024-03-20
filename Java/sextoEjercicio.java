import java.util.Scanner;

public class sextoEjercicio {
    public static int[] calcularPromedio(int[] Lunes, int[] Viernes) {
        int cantidadTemperatura = Lunes.length;
        int[] vectorNuevo = new int[cantidadTemperatura];

        for (int i = 0; i < cantidadTemperatura; i++) {
            vectorNuevo[i] = (Lunes[i] + Viernes[i]) / 2;
        }

        return vectorNuevo;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] dia = {"Lunes", "Viernes"};
        System.out.println("Digita la cantidad de veces que deseen \nrealizar la toma de temperatura por dia");
        int cantidadTemperatura = validarNumeroEntero(scanner);
        int[] Lunes = new int[cantidadTemperatura];
        int[] Viernes = new int[cantidadTemperatura];
        System.out.println("Toma de temperatura del dia Lunes");
        for (int i = 0; i < cantidadTemperatura; i++) {
            System.out.println("Digita la temperatura" + (i + 1));
            Lunes[i] = validarNumeroEntero(scanner);
        }
        System.out.println("Toma de temperatura del dia Viernes");
        for (int i = 0; i < cantidadTemperatura; i++) {
            System.out.println("Digita la temperatura" + (i + 1));
            Viernes[i] = validarNumeroEntero(scanner);
        }

        int[] nuevoVector = calcularPromedio(Lunes,Viernes);
        System.out.println("promedio de las temperaturas de Lunes y Viernes:");
        for (int i = 0; i < 2; i++) {
            System.out.println("Promedio del dia " + dia[i] + " :" + nuevoVector[i] + " °C");
        }

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
