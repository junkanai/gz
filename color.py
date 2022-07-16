import sys
import traceback

red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)
yellow = (255, 0, 255)
pink = (255, 255, 0)
sky = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)

def gray(value):
    try:
        if 0 <= value < 256: return (value, value, value)
        raise ValueError
    except ValueError as e:
        raise ValueError(f"gray should be 0 to 255, not {value}!")
