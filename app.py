from flask import Flask
import time
import board
import busio
import adafruit_mlx90614

app = Flask(__name__)

# 🔁 Sensor Initialization with Retry (prevents crash on boot)
while True:
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = adafruit_mlx90614.MLX90614(i2c)
        print("✅ Sensor connected successfully")
        break
    except Exception as e:
        print("⏳ Waiting for sensor...", e)
        time.sleep(2)

# 🔥 Threshold temperature (change if needed)
THRESHOLD = 40

@app.route("/")
def home():
    try:
        temp = sensor.object_temperature

        if temp > THRESHOLD:
            status = "OVERHEATING 🔥"
            color = "red"
        else:
            status = "NORMAL ✅"
            color = "lightgreen"

    except Exception as e:
        temp = 0
        status = "Sensor Error ⚠️"
        color = "orange"

    return f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="2">
        <title>Transformer Monitoring</title>
        <style>
            body {{
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                font-family: Arial, sans-serif;
                text-align: center;
                color: white;
                margin: 0;
                padding: 0;
            }}
            .container {{
                margin-top: 100px;
            }}
            .card {{
                background: rgba(255,255,255,0.1);
                padding: 40px;
                border-radius: 20px;
                display: inline-block;
                box-shadow: 0 0 20px rgba(0,0,0,0.3);
            }}
            h1 {{
                font-size: 40px;
                margin-bottom: 20px;
            }}
            .temp {{
                font-size: 60px;
                font-weight: bold;
            }}
            .status {{
                font-size: 30px;
                margin-top: 20px;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <div class="card">
                <h1>AI-Based Transformer Monitoring System</h1>
                <div class="temp">{temp:.2f} °C</div>
                <div class="status" style="color:{color};">
                    {status}
                </div>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    # 🌐 Allow access from other devices in network
    app.run(host="0.0.0.0", port=5000)
