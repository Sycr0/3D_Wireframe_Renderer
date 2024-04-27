#Libraries
import pygame as pg

#Scripts
import SceneManager
import Projection
import CameraMovement
import Render

pg.init()
pg.display.set_caption("3D Wireframe Renderer in Python")
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)
GUI = pg.display.set_mode((1280, 720), pg.RESIZABLE)
clock = pg.time.Clock()
running = True

fpsCap = 60

def BlankLine(amount: int):
    i = 0
    while i < amount:
        print("")
        i+=1

def Start():
    CreateModels()


def CreateModels():
    cube = SceneManager.CurrentScene.NewGameObject(Name="Cube", ModelFileName="Cube.obj")

    cube.transform.scale.x = 200
    cube.transform.scale.y = 200
    cube.transform.scale.z = 200
    cube.transform.position.z = -20
    cube.transform.position.x = -5000

    IcoSphere = SceneManager.CurrentScene.NewGameObject(Name="IcoSphere", ModelFileName="IcoSphere.obj")

    IcoSphere.transform.scale.x = 300
    IcoSphere.transform.scale.y = 300
    IcoSphere.transform.scale.z = 300
    IcoSphere.transform.position.z = -20

    Monkey = SceneManager.CurrentScene.NewGameObject(Name="Monkey", ModelFileName="Monkey.obj")

    Monkey.transform.scale.x = 200
    Monkey.transform.scale.y = 200
    Monkey.transform.scale.z = 200
    Monkey.transform.position.z = -20
    Monkey.transform.position.x = 5000

    Dog = SceneManager.CurrentScene.NewGameObject(Name="Dog", ModelFileName="Dog.obj")

    Dog.transform.scale.x = 200
    Dog.transform.scale.y = 200
    Dog.transform.scale.z = 200
    Dog.transform.position.z = -20
    Dog.transform.position.x = 10000




def Update():
    cube = SceneManager.CurrentScene.GameObjects["Cube"]
    cube.transform.rotation.x += 1
    cube.transform.rotation.y += 1
    cube.transform.rotation.z += 1

    IcoSphere = SceneManager.CurrentScene.GameObjects["IcoSphere"]
    IcoSphere.transform.rotation.x += 1
    IcoSphere.transform.rotation.y += 1

    Monkey = SceneManager.CurrentScene.GameObjects["Monkey"]
    Monkey.transform.rotation.x += 1

    Dog = SceneManager.CurrentScene.GameObjects["Dog"]
    Dog.transform.rotation.x += 0.5

    BlankLine(5)
    print("------------------------------ Update Called - New Tick ------------------------------")

    BlankLine(2)
    print("--------------- Rotation Started ---------------")
    Projection.RotateModelsInScene(SceneManager.CurrentScene)
    print("--------------- Rotation Complete ---------------")

    BlankLine(2)
    print("--------------- Camera Movement Started ---------------")
    CameraMovement.Check()
    print("--------------- Camera Movement Complete ---------------")

    BlankLine(2)
    print("--------------- Projection Started ---------------")
    Projection.ProjectValuesInScene(SceneManager.CurrentScene)
    print("--------------- Projection Complete ---------------")

    BlankLine(2)
    print("--------------- Rendering Started ---------------")
    Render.RenderScene(SceneManager.CurrentScene, screen)
    print("--------------- Rendering Complete ---------------")

    BlankLine(2)
    print("------------------------------ Update Complete - End of Tick ------------------------------")

Start()
while running:
    # Check for clicking 'X' and end everything
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill("Black") # Background Color

    Update()
    
    pg.display.flip()
    clock.tick(fpsCap)
pg.quit()