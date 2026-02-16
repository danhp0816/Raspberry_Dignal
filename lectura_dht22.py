#librerías
import time
from pymodbus.client import ModbusTcpClient

IP = "192.168.3.78"
PORT = 502

#rEGISTROS
REG_TEMP = 0
REG_HUM = 1 

client = ModbusTcpClient(IP, port=PORT)
if not client.connect():
    print("Conexión con ESP32 no establecida")
    exit();

print("Conexión establecida, leyendo cada 5 segundos\n")

try: 
    while True:
        rr = client.read_holding_registers(REG_TEMP, count=2, device_id=1)

        if rr.isError():
            print("Error en la lectura")
        else:
            temp = rr.registers[0]
            hum = rr.registers[1]
            print(f"Temperatura: {temp/100.0:.2f} | Humedad: {hum/100.0:.2f}")
        time.sleep(5)
except KeyboardInterrupt:
    print("\nFinalizando")
    client.close()
    print("\n Conexión finalizada")