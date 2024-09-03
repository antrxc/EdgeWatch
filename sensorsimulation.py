import random


import random

def sensor():
    temp = random.uniform(15, 35)
    humidity = random.uniform(30, 80)
    light_intensity = random.uniform(0, 1000)
    co2 = random.uniform(400, 1000)
    pressure = random.uniform(950, 1050)  # Assuming pressure range in millibars

    #some code for calamity
    if random.random() < 0.01:  # 1% chance of anomaly
        catastrophe_type = random.choice(['temperature', 'humidity', 'light_intensity', 'co2_level', 'pressure'])
        if catastrophe_type == 'temperature':
            temp = random.choice([-100, 100])
        elif catastrophe_type == 'humidity':
            humidity = random.choice([0, 100])
        elif catastrophe_type == 'light_intensity':
            light_intensity = 10000
        elif catastrophe_type == 'co2_level':
            co2 = 5000
        elif catastrophe_type == 'pressure':
            pressure = random.choice([0, 2000])  # Assuming extreme pressure values

    return temp, humidity, light_intensity, co2, pressure

i= sensor()
print(i)
