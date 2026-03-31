# System-Cloud-Tracker 🖥️☁️

This project is a Python tool designed to monitor local PC performance and automatically sync that data to the cloud (ThingSpeak). It allows you to track hardware metrics from any device with internet access.

## 🛠️ What it does

- **API Management:** Automatically creates, deletes, and registers ThingSpeak channels using HTTP requests (POST/DELETE).
- **Live Monitoring:** Uses the `psutil` library to capture real-time CPU and RAM usage every few seconds.
- **Testing & Simulation:** Includes scripts to generate sine wave data to verify cloud visualizations before deploying live metrics.
- **Graceful Shutdown:** Implemented a signal handler to ensure the program exits cleanly when pressing CTRL+C without leaving hanging processes.

## 📁 File Breakdown

- `Practica1_KSCS.py`: The core logic managing ThingSpeak API communication and local channel registration.
- `codigo.py`: The script responsible for reading hardware metrics (RAM/CPU).
- `Prueba_ThingSpeak.py`: A testing utility for sending simulated data waves to the cloud.
- `signal_handler.py`: A small utility for handling keyboard interruptions elegantly.

## 🚀 Tech Stack
- **Language:** Python 3
- **Key Libraries:** `requests` (APIs), `psutil` (Hardware), `urllib`, and `json`.
- **Cloud Platform:** ThingSpeak (IoT Analytics).

## 💡 Why I built this
I wanted a lightweight way to centralize hardware metrics without relying on heavy third-party software. This is a direct implementation of how to bridge local scripts with IoT infrastructure for total data control.
