import sys

red = (255, 0, 0)
blue = ()
green = ()
yellow = ()
pink = ()
sky = ()
white = (255, 255, 255)
black = (0, 0, 0)

def gray(value):
    if 0 <= value < 256: return (value, value, value)
    print(f"value should be 0 to 255, not {value}!")
    sys.exit()


