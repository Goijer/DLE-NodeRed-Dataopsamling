import paho.mqtt.client as mqtt
from pymodbus.client import ModbusTcpClient

MQTT_BROKER = "142.93.135.2"
MQTT_TOPIC = "DLE/Data/Jadetcarl"

MODBUS_HOST = "127.0.0.1"
MODBUS_PORT = 502

modbus = ModbusTcpClient(MODBUS_HOST, port=MODBUS_PORT)

if not modbus.connect():
    print("Modbus fejler")
else:
    print("Modbus OK")

def on_message(client, userdata, msg):
    print("\nModtog MQTT:", msg.payload)

    try:
        payload = msg.payload.decode("utf-8")

        # Konverter string → bool
        if payload.lower() in ["true"]:
            value = True
        else:
            value = False

        print("Bool værdi:", value)

        # Skriv til coil 00001
        modbus.write_coil(0, value)
        print("Skrev bool til Modbus coil 00001")

    except Exception as e:
        print("Fejl:", e)


client = mqtt.Client()
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)
client.subscribe(MQTT_TOPIC)

print("Lytter på MQTT...")
client.loop_forever()
