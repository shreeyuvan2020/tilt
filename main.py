import pybooklid
import streamlit
from PIL import Image,ImageDraw
import random
sensor = pybooklid.LidSensor()
for angle in sensor.monitor():
    streamlit.write(f"Lid angle: {angle} degrees")
    base = random.randint(0, 178)
    img = Image.new('RGB', (255,255))
    draw = ImageDraw.Draw(img)
