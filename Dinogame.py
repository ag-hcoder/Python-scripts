import pyautogui
import time
import pyscreenshot as ImageGrab


def hit(key):
    pyautogui.press(key)
    return


def iscollide(data):
    for i in range(195, 400):
        for j in range(430, 490):
            if data[i, j] < 100:
                hit("up")
                return


if __name__ == "__main__":
    print("This is Dino Game Automation")
    time.sleep(3)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscollide(data)

    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    # for i in range(183, 300):
    #     for j in range(430, 500):
    #         data[i, j] = 0
    #
    # image.show()
