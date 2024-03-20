import java.util.Scanner;
import java.lang.Math;

public class quintoEjercicio {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese la cantidad de productos a comprar");
        int cantCompra = validarNumeroEntero(scanner);
        float[] precio_compra = new float[cantCompra];
        float[] precio_venta = new float[cantCompra];
        int j = 0;
        int k = 0;
        int i = 0;
        int o = 0;

        while (j < precio_compra.length) {
            System.out.println("Digita el precio de la compra " + (j + 1));
            float producto = validarNumeroFloat(scanner);
            precio_compra[j] = Math.round(producto);

            j++;
        }
        System.out.print("Los precios son: ");
        while (k < precio_compra.length) {

            System.out.print(precio_compra[k] + ",");
            k++;
        }
        System.out.println(" ");
        while (o < precio_compra.length) {
            precio_venta[o] = Math.round(precio_compra[o] * 1.1F);
            o++;
        }
        System.out.print("Las ventas mas el 10% es: ");
        while (i < precio_venta.length) {
            System.out.print(precio_venta[i] + " ");
            i++;

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

    public static float validarNumeroFloat(Scanner scanner) {
        while (true) {
            try {
                return Float.parseFloat(scanner.next());
            } catch (NumberFormatException e) {
                System.out.println("Error: Debe ingresar un número.");
            }
        }
    }

}
