#Libraries
import pygame as pg

#Scripts
import Sy3D_SceneManager
import Sy3D_Projection
import Sy3D_CameraMovement
import Sy3D_Render

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
    cube = SceneManager.CurrentScene.NewGameObject(Name="Cube",
                                                   VertexTable = [[1,1,1],[1,-1,1],[-1,-1,1],[-1,1,1],[1,1,-1],[1,-1,-1],[-1,-1,-1],[-1,1,-1]],
                                                   EdgeTable = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]])
    cube.transform.scale.x = 300
    cube.transform.scale.y = 300
    cube.transform.scale.z = 300
    cube.transform.position.z = -20
    cube.RotatedVertexTable = cube.VertexTable.copy()
    print("Cube1: " + str(cube))

def Update():
    cube = SceneManager.CurrentScene.GameObjects["Cube"]
    cube.transform.rotation.x += 1
    cube.transform.rotation.y += 1
    cube.transform.rotation.z += 1

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