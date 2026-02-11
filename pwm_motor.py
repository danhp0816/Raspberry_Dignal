from gpiozero import Motor
from time import sleep

# Configuramos el motor:
# forward=IN1, backward=IN2, enable=Pin de tu código de brillo (GPIO 12)
motor = Motor(forward=17, backward=22, enable=12) 

try:
    while True:
        # Tu misma lógica de incremento de "brillo" aplicada a "velocidad"
        for valor in range(0, 101, 5):
            velocidad = valor / 100.0 # gpiozero usa escala de 0.0 a 1.0
            motor.forward(velocidad)   # En lugar de led.value, usamos motor.forward
            print(f"Velocidad Motor: {valor}%")
            sleep(1)

        for valor in range(100, -1, -5):
            velocidad = valor / 100.0
            motor.forward(velocidad)
            print(f"Velocidad Motor: {valor}%")
            sleep(1)

        sleep(3)
        
        for valor in range(0, 101, 5):
            velocidad = valor / 100.0 # gpiozero usa escala de 0.0 a 1.0
            motor.backward(velocidad)   # En lugar de led.value, usamos motor.forward
            print(f"Velocidad Motor: {valor}%")
            sleep(1)

        for valor in range(100, -1, -5):
            velocidad = valor / 100.0
            motor.backward(velocidad)
            print(f"Velocidad Motor: {valor}%")
            sleep(1)


except KeyboardInterrupt:
    print("\nDeteniendo motor")
    motor.stop() # Limpieza automática de gpiozero

