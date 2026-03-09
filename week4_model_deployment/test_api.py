import requests
import json
import random

url = 'http://localhost:5000/predict'

# Creating dummy sensor readings
sensor_data = {f"sensor_{i}": random.uniform(-2.0, 2.0) for i in range(10)}

payload = {
    "sensor_readings": sensor_data
}

print(f"Sending request to {url}...\n")
print("Payload:")
print(json.dumps(payload, indent=2))
print("\n---\n")

try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    
    if response.status_code == 200:
        result = response.json()
        print("\nResponse:")
        print(json.dumps(result, indent=2))
        print(f"\nLatency: {result['latency_ms']:.2f} ms")
        if result['latency_ms'] < 50:
            print("🚀 Real-time latency check passed! (< 50ms)")
        else:
            print("⚠️ Latency took longer than 50ms.")
    else:
        print("Error:", response.text)
except requests.exceptions.ConnectionError:
    print("Failed to connect. Make sure the Flask app is running (python app.py).")
