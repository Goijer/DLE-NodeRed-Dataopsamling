import paho.mqtt.client as mqtt

MQTT_BROKER = "142.93.135.2"
MQTT_TOPIC = "DLE/Data/Jadetcarl"

def on_message(client, userdata, msg):
    print("\nModtog MQTT:", msg.payload)

    try:
        payload = msg.payload.decode("utf-8")

    except Exception as e:
        print("Fejl:", e)


client = mqtt.Client()
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)
client.subscribe(MQTT_TOPIC)

print("Lytter på MQTT...")
client.loop_forever()
