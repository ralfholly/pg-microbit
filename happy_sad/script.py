from microbit import *

def step():
    if (button_a.is_pressed()):
        display.show(Image.HAPPY)
    elif (button_b.is_pressed()):
        display.show(Image.SAD)

def main():
    while True:
        step()
        sleep(10)

if __name__ == '__main__':
    main()

