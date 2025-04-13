/*
PROMPT PARA GENERAR ESTE CÓDIGO:

Necesito un código para Arduino que haga lo siguiente:

1. Configuración de Hardware:
   - Usar LED 1 conectado al pin 13
   - Usar LED 2 conectado al pin 12

2. Funcionalidad requerida:
   - Comunicación serial a 9600 baudios
   - Control de dos LEDs mediante comandos seriales
   - Los comandos deben ser:
     * '1' para encender LED 1
     * '2' para apagar LED 1
     * '3' para encender LED 2
     * '4' para apagar LED 2

3. Características adicionales:
   - Mostrar mensaje de bienvenida al iniciar con los comandos disponibles
   - Enviar confirmación por serial cuando se ejecute cada comando
   - Indicar cuando se recibe un comando no válido

El código debe poder comunicarse con una interfaz en Python mediante comunicación serial.
*/

// Definición de pines para los LEDs
const int LED1 = 13;
const int LED2 = 12;

void setup() {
  // Inicializar comunicación serial
  Serial.begin(9600);
  
  // Configurar pines de LEDs como salidas
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  
  // Mensaje de bienvenida
  Serial.println("Sistema de control de LEDs");
  Serial.println("Comandos disponibles:");
  Serial.println("1 - Encender LED 1");
  Serial.println("2 - Apagar LED 1");
  Serial.println("3 - Encender LED 2");
  Serial.println("4 - Apagar LED 2");
}

void loop() {
  // Verificar si hay datos disponibles en el puerto serial
  if (Serial.available() > 0) {
    char comando = Serial.read();
    
    // Procesar el comando recibido
    switch(comando) {
      case '1':
        digitalWrite(LED1, HIGH);
        Serial.println("LED 1 encendido");
        break;
      case '2':
        digitalWrite(LED1, LOW);
        Serial.println("LED 1 apagado");
        break;
      case '3':
        digitalWrite(LED2, HIGH);
        Serial.println("LED 2 encendido");
        break;
      case '4':
        digitalWrite(LED2, LOW);
        Serial.println("LED 2 apagado");
        break;
      default:
        Serial.println("Comando no válido");
        break;
    }
  }
}
