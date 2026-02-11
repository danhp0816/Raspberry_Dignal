from gpiozero import LED
import time

led = LED(12)

#PIO.setmode(GPIO.BCM) Tipo de Numeración
#PIO.setup(LED_PIN, GPIO.OUT) #Establecer como salida pin 12

try: #encapsular código para detectar cuando ocurre un cierto evento
    while True:
        led.on()
        print("ENCENDIENDO LED") #MENSAJE PARA EL USUARIO
        time.sleep(1) #Cantidad de segundos que espera antes de continuar

        led.off()
        print("Apagando LED")
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa detenido")