import math
import time

def draw_heart():
    for angle in range(0, 360, 10):
        radian = math.radians(angle)
        x = 16 * math.sin(radian) ** 3
        y = 13 * math.cos(radian) - 5 * math.cos(2 * radian) - 2 * math.cos(3 * radian) - math.cos(4 * radian)
        x = int(x) + 20
        y = int(y) + 10
        print("\033c")  # Ekranı temizle
        print("\n" * y + " " * x + "❤️")
        time.sleep(0.01)

draw_heart()
