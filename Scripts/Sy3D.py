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
    # cube = SceneManager.CurrentScene.NewGameObject(Name="Cube",
    #                                                VertexTable = [[1,1,1],[1,-1,1],[-1,-1,1],[-1,1,1],[1,1,-1],[1,-1,-1],[-1,-1,-1],[-1,1,-1]],
    #                                                EdgeTable = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]])
    # cube.transform.scale.x = 300
    # cube.transform.scale.y = 300
    # cube.transform.scale.z = 300
    # cube.transform.position.z = -20
    # cube.RotatedVertexTable = cube.VertexTable.copy()
    # print("Cube1: " + str(cube))
    IcoSphere = SceneManager.CurrentScene.NewGameObject(Name="IcoSphere",
                                                        VertexTable=[[0.000000, -1.000000, 0.000000],
[0.723607, -0.447220, 0.525725],
[-0.276388, -0.447220, 0.850649],
[-0.894426, -0.447216, 0.000000],
[-0.276388, -0.447220, -0.850649],
[0.723607, -0.447220, -0.525725],
[0.276388, 0.447220, 0.850649],
[-0.723607, 0.447220, 0.525725],
[-0.723607, 0.447220, -0.525725],
[0.276388, 0.447220, -0.850649],
[0.894426, 0.447216, 0.000000],
[0.000000, 1.000000, 0.000000],
[-0.162456, -0.850654, 0.499995],
[0.425323, -0.850654, 0.309011],
[0.262869, -0.525738, 0.809012],
[0.850648, -0.525736, 0.000000],
[0.425323, -0.850654, -0.309011],
[-0.525730, -0.850652, 0.000000],
[-0.688189, -0.525736, 0.499997],
[-0.162456, -0.850654, -0.499995],
[-0.688189, -0.525736, -0.499997],
[0.262869, -0.525738, -0.809012],
[0.951058, 0.000000, 0.309013],
[0.951058, 0.000000, -0.309013],
[0.000000, 0.000000, 1.000000],
[0.587786, 0.000000, 0.809017],
[-0.951058, 0.000000, 0.309013],
[-0.587786, 0.000000, 0.809017],
[-0.587786, 0.000000, -0.809017],
[-0.951058, 0.000000, -0.309013],
[0.587786, 0.000000, -0.809017],
[0.000000, 0.000000, -1.000000],
[0.688189, 0.525736, 0.499997],
[-0.262869, 0.525738, 0.809012],
[-0.850648, 0.525736, 0.000000],
[-0.262869, 0.525738, -0.809012],
[0.688189, 0.525736, -0.499997],
[0.162456, 0.850654, 0.499995],
[0.525730, 0.850652, 0.000000],
[-0.425323, 0.850654, 0.309011],
[-0.425323, 0.850654, -0.309011],
[0.162456, 0.850654, -0.499995]],
                                                        EdgeTable=[]
)
    IcoSphere.transform.scale.x = 100
    IcoSphere.transform.scale.y = 100
    IcoSphere.transform.scale.z = 100
    IcoSphere.transform.position.z = -20




def Update():
    # cube = SceneManager.CurrentScene.GameObjects["Cube"]
    # cube.transform.rotation.x += 1
    # cube.transform.rotation.y += 1
    # cube.transform.rotation.z += 1

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