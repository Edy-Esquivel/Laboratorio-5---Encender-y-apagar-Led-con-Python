
#peotoolo de comunicación


#Se Importa la libreria de Firmata para la cominicación genérica con arduino
#si no se tiene se instala ejecutando el comando pip install Firmata
import pyfirmata 

#LIBRERIA DE TIEMPO
import time # Hace referencia a todas las opciones incluidas en la librería

board = pyfirmata.Arduino('COM4') #puerto de conexión físico de Arduino detectado

#ciclo de encendido y apagado de Led
while True:
    board.digital[9].write(1) #Hace referencia a la salida digital seleccionada 9
    time.sleep(3) #hace referencia al tiempo que permacerá encendido el led en segundos
    board.digital[9].write(0)#Hace referencia a la salida digital seleccionada 9
    time.sleep(1) #hace referencia al tiempo que permacerá apagado el led en segundos

#FIN











