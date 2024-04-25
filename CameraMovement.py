from SceneManager import *
import keyboard

def Check(fpsCap: int):
    moveSpeed = 10000
    currentCam = CurrentScene.camera
    pos = currentCam.transform.position

    if keyboard.is_pressed('a'):
        pos.x += moveSpeed
        print("A Key Pressed")
    if keyboard.is_pressed('d'):
        pos.x -= moveSpeed
        print("D Key Pressed")

    if keyboard.is_pressed('e'):
        pos.y += moveSpeed
        print("E Key Pressed")
    if keyboard.is_pressed('q'):
        pos.y -= moveSpeed
        print("Q Key Pressed")

    if keyboard.is_pressed('w'):
        pos.z -= moveSpeed / 500
        print("w Key Pressed")
    if keyboard.is_pressed('s'):
        pos.z += moveSpeed / 500
        print("S Key Pressed")