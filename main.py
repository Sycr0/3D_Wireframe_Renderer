#Libraries
import pygame as pg

#Scripts
import SceneManager
import Projection
import CameraMovement

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

    print("Cube2: " + str(cube))
    print(cube.transform.rotation.x, cube.transform.rotation.y, cube.transform.rotation.z)
    BlankLine(5)
    print("------------------------------ Update Called - New Tick ------------------------------")
    BlankLine(2)
    print("--------------- Rotation Started ---------------")
    Projection.RotateModelToAngle(cube, cube.transform.rotation.x, cube.transform.rotation.y, cube.transform.rotation.z)
    print("--------------- Rotation Complete ---------------")
    BlankLine(2)
    print("--------------- Camera Movement Started ---------------")
    CameraMovement.Check()
    print("--------------- Camera Movement Complete ---------------")
    BlankLine(2)
    print("--------------- Projection Started ---------------")
    Projection.CalculateProjectedValues(SceneManager.CurrentScene.GameObjects["Cube"], SceneManager.CurrentScene)
    print("--------------- Projection Complete ---------------")
    BlankLine(2)
    print("--------------- Rendering Started ---------------")
    RenderObject(SceneManager.CurrentScene.GameObjects["Cube"])
    print("--------------- Rendering Complete ---------------")
    BlankLine(2)
    print("------------------------------ Update Complete - End of Tick ------------------------------")

def RenderObject(object1: SceneManager.GameObject):
    ProjX, ProjY = object1.ProjectedX, object1.ProjectedY

    i = 0
    while i<len(ProjX):
        if ProjX[i] != 'n' and ProjY[i] != 'n':
            print("Vertex Draw at: " + str(ProjX[i]), str(ProjY[i]))
            pg.draw.circle(surface=screen, color="blue", center=[ProjX[i],ProjY[i]], radius=5, width=0)
        else:
            print("Vertex Past Near Plane")
        i += 1

    i = 0
    while i<len(object1.EdgeTable):
        Edge1, Edge2 = object1.EdgeTable[i]
        if ProjX[Edge1] != "n" and ProjY[Edge1] != "n" and ProjX[Edge2] != "n" and ProjY[Edge2] != "n":
            pg.draw.line(surface=screen, color="blue", start_pos=[ProjX[Edge1], ProjY[Edge1]], end_pos=[ProjX[Edge2], ProjY[Edge2]], width=2)
            print("Line drawn from:  " + str(ProjX[Edge1]) + ", " + str(ProjY[Edge1]) + " to:  " + str(ProjX[Edge2]) + ", " + str(ProjY[Edge2]))
        else:
            print("Edge Past Near Plane")
        i += 1

    i = 0
    while i<len(object1.FaceTable):
        break

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