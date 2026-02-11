#07 - febrero - 2026
#Daniel Flores Ramírez
#Progrma para indicar la potencia del motor
#ENA=12, IN1=17, IN2=22


from gpiozero import Motor
from time import sleep
import time

# Configuramos el motor:
# forward=IN1, backward=IN2, enable=Pin de tu código de brillo (GPIO 12)
motor = Motor(forward=17, backward=22, enable=12) 

print("Programa para controlar potencia de un motor DC\n Presiona CTRL + C para salir")


try:
    while True:
        print("Ingresa la potencia con un entero entre 1 - 100")
        valor = input("")
        #Detección de que el valor introducido es válido 
        if not valor.isdigit():
            print("Entrada incorrecta")
            continue

        potencia = int(valor)/100.0

        if 0.0 <= potencia <= 1.0:
            motor.forward(potencia)
            print(f"La potenmcia ingresada es: {valor}%")
        else: 
            print("La potencia está fuera de los límites")

        sleep(0.1)



except KeyboardInterrupt:
    print("\nDeteniendo motor")
    forward = False
    backward = False
    enable = False
    motor.stop() # Limpieza automática de gpiozero

