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
#     cube = SceneManager.CurrentScene.NewGameObject(Name="Cube",
#                                                    VertexTable = [[1.000000, 1.000000, -1.000000],
# [1.000000, -1.000000, -1.000000],
# [1.000000, 1.000000, 1.000000],
# [1.000000, -1.000000, 1.000000],
# [-1.000000, 1.000000, -1.000000],
# [-1.000000, -1.000000, -1.000000],
# [-1.000000, 1.000000, 1.000000],
# [-1.000000, -1.000000, 1.000000]],
#                                                    FaceTable= [[1, 5, 7, 3],
# [4, 3, 7, 8],
# [8, 7, 5, 6],
# [6, 2, 4, 8],
# [2, 1, 3, 4],
# [6, 5, 1, 2]])
#
#     cube.transform.scale.x = 300
#     cube.transform.scale.y = 300
#     cube.transform.scale.z = 300
#     cube.transform.position.z = -20

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
                                                        FaceTable=[[1, 14, 13],
[2, 14, 16],
[1, 13, 18],
[1, 18, 20],
[1, 20, 17],
[2, 16, 23],
[3, 15, 25],
[4, 19, 27],
[5, 21, 29],
[6, 22, 31],
[2, 23, 26],
[3, 25, 28],
[4, 27, 30],
[5, 29, 32],
[6, 31, 24],
[7, 33, 38],
[8, 34, 40],
[9, 35, 41],
[10, 36, 42],
[11, 37, 39],
[39, 42, 12],
[39, 37, 42],
[37, 10, 42],
[42, 41, 12],
[42, 36, 41],
[36, 9, 41],
[41, 40, 12],
[41, 35, 40],
[35, 8, 40],
[40, 38, 12],
[40, 34, 38],
[34, 7, 38],
[38, 39, 12],
[38, 33, 39],
[33, 11, 39],
[24, 37, 11],
[24, 31, 37],
[31, 10, 37],
[32, 36, 10],
[32, 29, 36],
[29, 9, 36],
[30, 35, 9],
[30, 27, 35],
[27, 8, 35],
[28, 34, 8],
[28, 25, 34],
[25, 7, 34],
[26, 33, 7],
[26, 23, 33],
[23, 11, 33],
[31, 32, 10],
[31, 22, 32],
[22, 5, 32],
[29, 30, 9],
[29, 21, 30],
[21, 4, 30],
[27, 28, 8],
[27, 19, 28],
[19, 3, 28],
[25, 26, 7],
[25, 15, 26],
[15, 2, 26],
[23, 24, 11],
[23, 16, 24],
[16, 6, 24],
[17, 22, 6],
[17, 20, 22],
[20, 5, 22],
[20, 21, 5],
[20, 18, 21],
[18, 4, 21],
[18, 19, 4],
[18, 13, 19],
[13, 3, 19],
[16, 17, 6],
[16, 14, 17],
[14, 1, 17],
[13, 15, 3],
[13, 14, 15],
[14, 2, 15]]
)
    IcoSphere.transform.scale.x = 300
    IcoSphere.transform.scale.y = 300
    IcoSphere.transform.scale.z = 300
    IcoSphere.transform.position.z = -20

def Update():
    # cube = SceneManager.CurrentScene.GameObjects["Cube"]
    # cube.transform.rotation.x += 1
    # cube.transform.rotation.y += 1
    # cube.transform.rotation.z += 1

    IcoSphere = SceneManager.CurrentScene.GameObjects["IcoSphere"]
    IcoSphere.transform.rotation.x += 1
    IcoSphere.transform.rotation.y += 1
    IcoSphere.transform.rotation.z += 1

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