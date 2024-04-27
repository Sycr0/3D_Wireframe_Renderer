import SceneManager
import pygame as pg

def DrawTriangle(Vertex1: tuple, Vertex2: tuple, Vertex3: tuple, screen):
    pg.draw.lines(screen, 'blue', True, [Vertex1, Vertex2, Vertex3, Vertex1], 3)

def RenderObject(object1: SceneManager.GameObject, screen):
    ProjX, ProjY = object1.ProjectedX, object1.ProjectedY

    i = 0
    while i<len(ProjX):
        if ProjX[i] != 'n' and ProjY[i] != 'n':
            print("Vertex Draw at: " + str(ProjX[i]), str(ProjY[i]))
            pg.draw.circle(surface=screen, color="blue", center=[ProjX[i],ProjY[i]], radius=2, width=0)
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

def RenderScene(Scene: SceneManager.Scene, screen):
    i = 0
    while i < len(Scene.GameObjects):
        Object = list(Scene.GameObjects.values())[i]
        RenderObject(Object, screen)
        i += 1
