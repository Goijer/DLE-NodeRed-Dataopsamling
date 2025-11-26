import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("sensor_data.csv")

# Læs sidste linje for flere kolonner
sidste_linje = df.iloc[-1]

print(f"P1: {sidste_linje['P1']}")
print(f"P2: {sidste_linje['P2']}")
print(f"timestamp: {sidste_linje['timestamp']}")

plt.bar(df['timestamp'], df['P1'], label='P1')
plt.bar(df['timestamp'], df['P2'], label='P2')

plt.xlabel('Timestamp')
plt.ylabel('Values')
plt.title('Sensor Data Over Tid')
plt.legend()
plt.show()