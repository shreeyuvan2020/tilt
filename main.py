import pybooklid
import streamlit
import math
from PIL import Image,ImageDraw
import random
sensor = pybooklid.LidSensor()
for angle in sensor.monitor():
    ## streamlit.write(f"Lid angle: {angle} degrees")
    base_angle = random.randint(0, 180)
    second_angle = random.randint(0, 180-base_angle)
    third_angle = 180-second_angle-base_angle
    base = 100
    second = abs(100 * math.sin(math.radians(second_angle)) / math.sin(math.radians(base_angle)))
    third = abs(second * math.sin(math.radians(third_angle)) / math.sin(math.radians(base_angle)))
    print(base_angle, second_angle, third_angle)
    print(base, second, third)

