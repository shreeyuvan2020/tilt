import pybooklid
import streamlit
import math
from PIL import Image,ImageDraw
import random
sensor = pybooklid.LidSensor()
for angle in sensor.monitor():
    streamlit.write(f"Lid angle: {angle} degrees")
    base_angle = random.randint(0, 178)
    second_angle = random.randint(0, 180-base_angle-1)
    third_angle = 180-second_angle
    base = 100
    second = 100 * math.sin(base_angle) / math.sin(second_angle)
    third = second * math.sin(second_angle) / math.sin(third_angle)
    print(base_angle, second_angle, third_angle)
    print(base, second, third)

