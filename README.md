# ESP8266-RaspberryPi-RGB-Controller

This project consists of two main components:

1. **ESP8266 Server Code**: Controls two sets of RGB lights connected to an ESP8266 microcontroller. It acts as a server and receives POST requests to adjust the intensity of each color for both sets of RGB lights.

2. **Raspberry Pi Pico GUI Controller**: A Python GUI program running on a Raspberry Pi Pico, allowing users to control the RGB lights remotely. The GUI includes sliders for adjusting the intensity of red, green, and blue for each RGB light, as well as on/off switches for each light.

## ESP8266 Server Code

The `esp8266_server.ino` file contains the Arduino code for the ESP8266 server. It sets up an HTTP server that listens for POST requests on the `/rgb` endpoint. Upon receiving a request, it adjusts the intensity of each color for both sets of RGB lights.

### Setup

1. Open the `esp8266_server.ino` file in the Arduino IDE.
2. Make sure you have the necessary libraries installed (ESP8266WiFi, ESPAsyncTCP, ESPAsyncWebServer).
3. Replace `ssid` and `pass` with your WiFi credentials.
4. Upload the code to your ESP8266 board.

## Raspberry Pi Pico GUI Controller

The `pico_rgb_controller.py` file contains the Python code for the GUI controller running on the Raspberry Pi Pico. It uses the Tkinter library for GUI development and the `requests` library for sending HTTP POST requests to the ESP8266 server.

### Setup

1. Run the `pico_rgb_controller.py` script on your Raspberry Pi Pico.
2. Make sure to install the `requests` library if not already installed (`pip install requests`).

### Usage

1. Adjust the sliders to set the intensity of red, green, and blue for each RGB light.
2. Toggle the on/off switches to control the state of each RGB light.
3. Click the "Send RGB" button to send the updated RGB values to the ESP8266 server.

## Contributing

Contributions to improve this project are welcome! If you find any issues or have suggestions for enhancements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
