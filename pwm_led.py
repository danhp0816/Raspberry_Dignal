from gpiozero import PWMLED
import time

led = PWMLED(12)

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        #Incrementar intensidad del LED
        for valor in range (0,101,5):
            brillo = valor/100.0
            led.value = brillo 
            print(f"Brilo: {valor}%")
            time.sleep(0.5)

        #Disminuir Intensidad del LED
        for valor in range (100,-1,-5):
            brillo = valor/100.0
            led.value = brillo 
            print(f"Brilo: {valor}%")
            time.sleep(0.5)
except KeyboardInterrupt:
    print("Programa detenido")

