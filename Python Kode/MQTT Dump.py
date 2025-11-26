import paho.mqtt.client as mqtt
import datetime
import pandas as pd
import json
import os

# --- MQTT konfiguration ---
MQTT_BROKER = "142.93.135.2"
MQTT_PORT = 1883


# --- Callback når klienten forbinder ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Forbundet til MQTT-broker")
        client.subscribe("NodeRedData")
    else:
        print(f"Forbindelsesfejl, kode: {rc}")

# --- Callback når en besked modtages ---
def on_message(client, userdata, msg):
    print(f"\nModtog besked fra topic '{msg.topic}'")
    try:
        payload = json.loads(msg.payload.decode("utf-8"))
        entry = payload[0]
        series = entry["series"]
        data = [d[0] for d in entry["data"]]
        timestamp = entry["tidsstempel"]
        
        dt = datetime.datetime.fromtimestamp(timestamp / 1000)
        
        # --- AFRUND NUMERISKE KOLONNER TIL 3 DECIMALER ---
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_cols] = df[numeric_cols].round(3)

        df = pd.DataFrame([data], columns=series)
        df["timestamp"] = dt
        print(df)
    
        # Tjek om filen allerede eksisterer
        file_exists = os.path.isfile("sensor_data.csv")
        
        # Tilføj data til CSV (append mode)
        df.to_csv("sensor_data2.csv", mode='a', header=not file_exists, index=False)
        

    except Exception as e:
        print(f"Fejl ved behandling af data: {e}")

# --- MQTT klient opsætning ---
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)

print("Venter på data... (tryk Ctrl+C for at stoppe)")
client.loop_forever()