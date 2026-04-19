# 🔥 Transformer Temperature Monitoring System

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge&logo=github">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Raspberry%20Pi-4-red?style=for-the-badge&logo=raspberrypi">
  <img src="https://img.shields.io/badge/IoT-Project-orange?style=for-the-badge">
</p>

---

## 🚀 Overview

A **real-time transformer temperature monitoring system** using Raspberry Pi and MLX90614 infrared sensor.
The system detects overheating and displays live data on a **web dashboard**, running automatically on boot.

---

## ⚡ Features

✔ Non-contact temperature sensing
✔ Real-time monitoring
✔ Overheat detection 🔥
✔ Web dashboard (Flask) 🌐
✔ Auto-start on boot (systemd) ⚙️
✔ Fault-tolerant sensor handling

---

## 🧠 Tech Stack

* Python 🐍
* Flask 🌐
* Raspberry Pi OS 🍓
* I2C Communication
* Embedded Systems

---

## 🔧 Hardware Used

* Raspberry Pi 4 Model B
* MLX90614 Infrared Temperature Sensor
* Power Adapter
* Jumper Wires

---

## 🔄 System Flow

```
Sensor → Raspberry Pi → Processing → Web Dashboard → Alert
```

---

## 🧪 Working

1. Sensor reads temperature
2. Raspberry Pi processes data
3. Flask server displays output
4. If threshold exceeded → alert triggered

---

## 🌐 Web Interface

* Live temperature display
* Color-based status
* Auto refresh every 2 seconds

---

## ⚙️ Installation

```bash
git clone https://github.com/SRECONICS/Transformer-Temperature-Monitoring-System-using-Raspberry-PI-4.git
cd repo-name

python3 -m venv myenv
source myenv/bin/activate

pip install -r requirements.txt
python app.py
```

---

## 🚀 Auto Start Setup

```bash
sudo systemctl enable tempmonitor.service
sudo systemctl start tempmonitor.service
```

---

## 📈 Future Enhancements

* 📊 Temperature graphs
* ☁️ Cloud integration
* 🤖 AI-based prediction
* 📱 Mobile alerts

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## ⭐ Show Your Support

Give a ⭐ if you like this project!

---

## 👨‍💻 Author

**Sree**
Electronics & Communication Engineering Student
Building real-world IoT systems 🚀
