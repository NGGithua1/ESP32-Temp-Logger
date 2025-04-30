import serial
import time
import os
from datetime import datetime

# Update this to match your actual serial port (e.g., COM3 on Windows, /dev/ttyUSB0 on Linux)
SERIAL_PORT = "COM3"
BAUD_RATE = 115200
CSV_FILE = "temperature_log.csv"

def main():
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Wait for ESP32 to reset

    # Check if the file already exists to decide whether to write the header
    file_exists = os.path.exists(CSV_FILE)

    print(f"Appending data to {CSV_FILE}...")

    # print(f"Logging data to {CSV_FILE}...")
    

    with open(CSV_FILE, "a") as file:
        if not file_exists:
            file.write("Timestamp(ms),Temperature(°C)\n")

        try:
            while True:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    print(line)
                    file.write(line + "\n")
        except KeyboardInterrupt:
            print("\nLogging stopped.")
        finally:
            ser.close()

if __name__ == "__main__":
    main()
