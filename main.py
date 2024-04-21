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

fpsCap = 30

def BlankLine(amount: int):
    i = 0
    while i < amount:
        print("")
        i+=1

def Start():
    CreateModels()

def RenderObject(object1: SceneManager.GameObject):
    ProjX, ProjY = object1.ProjectedX, object1.ProjectedY

    i = 0
    while i<len(ProjX):
        pg.draw.circle(surface=screen, color="blue", center=[ProjX[i],ProjY[i]], radius=5, width=0)
        print("Vertex Draw at: " + str(ProjX[i]),str(ProjY[i]))
        i += 1

    i = 0
    while i<len(object1.EdgeTable):
        Edge1, Edge2 = object1.EdgeTable[i]
        pg.draw.line(surface=screen, color="blue", start_pos=[ProjX[Edge1], ProjY[Edge1]], end_pos=[ProjX[Edge2], ProjY[Edge2]], width=2)
        print("Line drawn from:  " + str(ProjX[Edge1]) + ", " + str(ProjY[Edge1]) + " to:  " + str(ProjX[Edge2]) + ", " + str(ProjY[Edge2]))
        i += 1

    i = 0
    while i<len(object1.FaceTable):
        break

def Update():
    BlankLine(5)
    print("------------------------------ Update Called - New Tick ------------------------------")
    BlankLine(2)
    print("--------------- Camera Movement Started ---------------")
    CameraMovement.Check(fpsCap=fpsCap)
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

def CreateModels():
    cube = SceneManager.CurrentScene.NewGameObject(Name="Cube",
                                            VertexTable = [[1,1,1],[1,-1,1],[-1,-1,1],[-1,1,1],[1,1,-1],[1,-1,-1],[-1,-1,-1],[-1,1,-1]],
                                            EdgeTable = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]])
    cube.transform.scale.x = 80
    cube.transform.scale.y = 80
    cube.transform.scale.z = 80
    cube.FaceTable = [[1,2,3,4],[5,6,7,8],]

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