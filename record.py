from mss import mss
from PIL import Image
import imageio
import time

sct = mss()

monitor = sct.monitors[1]

frames = []

print("Masz 3 sekundy na przełączenie się do gry...")
time.sleep(3)

for _ in range(100):  # około 10 sekund przy 10 FPS
    screenshot = sct.grab(monitor)
    img = Image.frombytes(
        "RGB",
        screenshot.size,
        screenshot.rgb
    )
    frames.append(img)
    time.sleep(0.1)

imageio.mimsave("snake.gif", frames, fps=10)

print("GIF zapisany jako snake.gif")