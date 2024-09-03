import smbus
import RPi.GPIO as GPIO
import serial
import time
import Adafruit_DHT



# I2C addresses
bmp280_address = 0x76
tcs34725_address = 0x29

# GPIO pin for DHT11
dht11_pin = 4

# UART settings for MH-Z19
uart_port = "/dev/ttyAMA0"
baud_rate = 9600

def read_bmp280_data():
    # Read temperature and pressure registers
    temp_data = bus.read_i2c_block_data(bmp280_address, 0xEE, 6)
    press_data = bus.read_i2c_block_data(bmp280_address, 0xF7, 6)

    # Convert raw data to temperature and pressure values
    temperature = (temp_data[0] << 12) | (temp_data[1] << 4) | (temp_data[2] >> 4)
    pressure = (press_data[0] << 12) | (press_data[1] << 4) | (press_data[2] >> 4)
    return temperature, pressure

def read_dht11_data():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, dht11_pin)
    return temperature, humidity

def read_tcs34725_data():
    # Read color data registers
    data = bus.read_i2c_block_data(tcs34725_address, 0x12, 8)

    # Convert raw data to color values
    R= (data[1] << 8) | data[0]
    G= (data[3] << 8) | data[2]
    B= (data[5] << 8) | data[4]
    C= (data[7] << 8) | data[6]

    return R,G,B,C

def read_mh_z19_data():
    uart.write(b"\x00\x01\x86\x00\x00\x00\x00\x00\x00")  # Query CO2 level
    response = uart.read(9)
    if response[0] == 0x00 and response[1] == 0x01:
        co2_level = (response[2] << 8) | response[3]
        return co2_level
    else:
        return None

# Initialize communication
bus = smbus.SMBus(1)
GPIO.setmode(GPIO.BCM)
uart = serial.Serial(uart_port, baud_rate)

# Main loop
while True:
    temperature_bmp, pressure = read_bmp280_data()
    temperature_dht, humidity = read_dht11_data()
    r, g, b, c = read_tcs34725_data()
    co2_level = read_mh_z19_data()
    light_intensity = (r + g + b) / 3

    # Print the data
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Temperature (BMP280): {temperature_bmp}")
    print(f"Temperature (DHT11): {temperature_dht}")
    print(f"Humidity: {humidity}")
    print(f"Light Intensity: {light_intensity}")
    print(f"CO2 Level: {co2_level}")

    time.sleep(180)