"""
PROMPT PARA GENERAR ESTE CÓDIGO:

Necesito crear un script en Python que combine la lógica de control de LEDs vía Arduino con una interfaz gráfica Qt. Los requisitos son:

1. Integración de Componentes:
   - Usar la interfaz gráfica generada por Qt Designer (Interfaz_Arduino.py)
   - Implementar la lógica de comunicación serial del archivo comunicacion_python_arduino.py
   - Mantener separada la lógica de negocio de la interfaz gráfica

2. Funcionalidad de Conexión:
   - Detectar y listar automáticamente los puertos COM disponibles
   - Permitir conectar/desconectar del puerto seleccionado
   - Cambiar el texto del botón entre "Conectar" y "Desconectar" según el estado
   - Mostrar el estado de conexión en la interfaz

3. Control de LEDs:
   - Implementar botones ON/OFF para dos LEDs
   - Mapear los comandos:
     * LED 1 ON -> '1'
     * LED 1 OFF -> '2'
     * LED 2 ON -> '3'
     * LED 2 OFF -> '4'
   - Actualizar el estado en la interfaz después de cada acción

4. Manejo de Errores:
   - Validar la disponibilidad de puertos
   - Manejar errores de conexión serial
   - Mostrar mensajes de error en la interfaz
   - Prevenir acciones cuando no hay conexión

5. Estructura del Código:
   - Usar el patrón MVC (Modelo-Vista-Controlador)
   - Clase ArduinoController para la lógica de comunicación
   - Clase MainWindow para la gestión de la interfaz
   - Mantener la modularidad para facilitar cambios en la interfaz

6. Cierre Limpio:
   - Desconectar el puerto serial al cerrar la aplicación
   - Liberar recursos adecuadamente

El código debe ser robusto y mantener la separación de responsabilidades para que las modificaciones en la interfaz gráfica no afecten la lógica de funcionamiento.

PROMPT ALTERNATIVO (VERSIÓN CORTA):
Crea un script en Python que:
1. Integre una interfaz Qt (desde Interfaz_Arduino.py) con la lógica de control Arduino
2. Detecte y liste puertos COM disponibles
3. Permita conectar/desconectar y controlar 2 LEDs con botones ON/OFF
4. Maneje errores y muestre estados en la interfaz
5. Use patrón MVC para separar la lógica de la interfaz

PROMPT ORIGINAL:
Tengo un archivo llamado comunicacion_python_arduino.py el cual se encarga de controlar leds mediante comunicación serial de Python a Arduino. También tengo generado desde Qt Designer llamado Interfaz_Arduino.py el cual solo es la interfaz gráfica usando pyuic5.
Quiero crear un archivo llamado main.py el cual utilice la lógica del programa de comunicacion_python_arduino.py pero enfocado a la interfaz grafica y que en caso de que yo quiera modificar el archivo Interfaz_Arduino.py la lógica de funcionamiento (botones, puertos, etc.) no salga afectada.
"""

import sys
import serial
import time
from PyQt5 import QtWidgets
from Interfaz_Arduino import Ui_Dialog
import serial.tools.list_ports

class ArduinoController:
    def __init__(self):
        self.arduino = None
        self.conectado = False

    def conectar_arduino(self, puerto):
        try:
            self.arduino = serial.Serial(puerto, 9600, timeout=1)
            time.sleep(2)  # Esperar a que se establezca la conexión
            self.conectado = True
            return True
        except serial.SerialException:
            self.conectado = False
            return False

    def desconectar_arduino(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.close()
        self.conectado = False
        return True

    def controlar_led(self, led_num, accion):
        if not self.conectado or not self.arduino:
            return False
        
        # Mapeo de acciones a comandos
        comandos = {
            ('1', 'on'): '1',
            ('1', 'off'): '2',
            ('2', 'on'): '3',
            ('2', 'off'): '4'
        }
        
        comando = comandos.get((led_num, accion))
        if comando:
            self.arduino.write(comando.encode())
            return True
        return False

    @staticmethod
    def obtener_puertos_disponibles():
        puertos = []
        for puerto in serial.tools.list_ports.comports():
            puertos.append(puerto.device)
        return puertos

class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Inicializar el controlador
        self.controller = ArduinoController()
        
        # Cargar puertos disponibles
        self.cargar_puertos_disponibles()
        
        # Conectar señales
        self.ui.pushButton_ConectarPuerto.clicked.connect(self.toggle_conexion)
        self.ui.pushButton_Encender_LED1.clicked.connect(lambda: self.controlar_led('1', 'on'))
        self.ui.pushButton_Apagar_LED1.clicked.connect(lambda: self.controlar_led('1', 'off'))
        self.ui.pushButton_Encender_LED2.clicked.connect(lambda: self.controlar_led('2', 'on'))
        self.ui.pushButton_Apagar_LED2.clicked.connect(lambda: self.controlar_led('2', 'off'))
        
        # Actualizar estado inicial
        self.actualizar_estado_conexion()

    def cargar_puertos_disponibles(self):
        self.ui.comboBox_SeleccionadorPuertos.clear()
        puertos = self.controller.obtener_puertos_disponibles()
        if puertos:
            self.ui.comboBox_SeleccionadorPuertos.addItems(puertos)
        else:
            self.ui.comboBox_SeleccionadorPuertos.addItem("No hay puertos disponibles")

    def toggle_conexion(self):
        if self.controller.conectado:
            # Desconectar
            if self.controller.desconectar_arduino():
                self.ui.label_EstadoDeConexion.setText("Estado: Desconectado")
                self.ui.pushButton_ConectarPuerto.setText("Conectar")
                self.actualizar_estado_conexion()
        else:
            # Conectar
            puerto = self.ui.comboBox_SeleccionadorPuertos.currentText()
            if puerto == "No hay puertos disponibles":
                self.ui.label_EstadoDeConexion.setText("Error: No hay puertos disponibles")
                return
                
            if self.controller.conectar_arduino(puerto):
                self.ui.label_EstadoDeConexion.setText("Estado: Conectado")
                self.ui.pushButton_ConectarPuerto.setText("Desconectar")
                self.actualizar_estado_conexion()
            else:
                self.ui.label_EstadoDeConexion.setText("Estado: Error de conexión")

    def controlar_led(self, led_num, accion):
        if self.controller.controlar_led(led_num, accion):
            estado = "ON" if accion == "on" else "OFF"
            self.ui.label_EstadoDeConexion.setText(f"LED {led_num} {estado}")
        else:
            self.ui.label_EstadoDeConexion.setText("Error: No se pudo controlar el LED")

    def actualizar_estado_conexion(self):
        estado = "Conectado" if self.controller.conectado else "No conectado"
        self.ui.label_EstadoDeConexion.setText(f"Estado: {estado}")
        # Actualizar texto del botón
        self.ui.pushButton_ConectarPuerto.setText("Desconectar" if self.controller.conectado else "Conectar")

    def closeEvent(self, event):
        self.controller.desconectar_arduino()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) 
    