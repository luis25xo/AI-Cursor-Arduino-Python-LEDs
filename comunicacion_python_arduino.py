"""
PROMPT PARA GENERAR ESTE CÓDIGO:

Necesito un script en Python que implemente la comunicación serial con Arduino para controlar LEDs. Los requisitos son:

1. Funcionalidad de Conexión:
   - Debe poder conectarse a Arduino a través de puerto serial
   - Velocidad de comunicación: 9600 baudios
   - Debe manejar errores de conexión
   - Debe incluir un tiempo de espera para establecer la conexión

2. Interfaz de Usuario:
   - Debe mostrar un menú de opciones en consola
   - Opciones del menú:
     * 1. Encender LED 1
     * 2. Apagar LED 1
     * 3. Encender LED 2
     * 4. Apagar LED 2
     * 5. Salir del programa

3. Funcionalidad de Control:
   - Debe enviar comandos al Arduino según la opción seleccionada
   - Los comandos deben ser:
     * '1' para encender LED 1
     * '2' para apagar LED 1
     * '3' para encender LED 2
     * '4' para apagar LED 2
   - Debe recibir y mostrar la respuesta del Arduino

4. Manejo de Errores:
   - Debe manejar errores de conexión serial
   - Debe validar las opciones del menú
   - Debe mostrar mensajes de error apropiados

5. Cierre Limpio:
   - Debe cerrar la conexión serial al salir del programa
   - Debe manejar la interrupción del programa (Ctrl+C)

El script debe usar la biblioteca pyserial para la comunicación serial y debe ser compatible con el código de Arduino que controla los LEDs.

PROMPT ALTERNATIVO (VERSIÓN CORTA):
Crea un script en Python que:
1. Se conecte a Arduino por puerto serial (9600 baudios)
2. Muestre un menú con opciones para controlar 2 LEDs:
   - Encender/Apagar LED 1
   - Encender/Apagar LED 2
3. Envíe comandos ('1' a '4') al Arduino según la opción seleccionada
4. Muestre las respuestas del Arduino
5. Maneje errores de conexión y cierre limpio
"""

import serial
import time

def conectar_arduino():
    try:
        # Ajusta el puerto COM según tu configuración
        arduino = serial.Serial('COM2', 9600, timeout=1)
        time.sleep(2)  # Esperar a que se establezca la conexión
        print("Conexión establecida con Arduino")
        return arduino
    except serial.SerialException:
        print("Error: No se pudo conectar al Arduino")
        return None

def mostrar_menu():
    print("\n=== Control de LEDs ===")
    print("1. Encender LED 1")
    print("2. Apagar LED 1")
    print("3. Encender LED 2")
    print("4. Apagar LED 2")
    print("5. Salir")
    print("=====================")

def main():
    arduino = conectar_arduino()
    if not arduino:
        return

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '5':
            print("Saliendo del programa...")
            break

        if opcion in ['1', '2', '3', '4']:
            arduino.write(opcion.encode())
            respuesta = arduino.readline().decode().strip()
            print(respuesta)
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

    arduino.close()

if __name__ == "__main__":
    main()
