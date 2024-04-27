import SceneManager
import pygame as pg

def RenderFace(Faces: list, screen):

    i = 0
    while i < len(Faces):
        x, y = Faces[i]
        pg.draw.circle(surface=screen, color="blue", center=[x, y], radius=2, width=0)
        i += 1

    pg.draw.lines(screen, 'blue', True, Faces, 3)

def RenderObject(object1: SceneManager.GameObject, screen):
    ProjX, ProjY = object1.ProjectedX, object1.ProjectedY

    i = 0
    while i<len(object1.FaceTable):

        Vertices = object1.FaceTable[i]

        index = 0
        while index < len(Vertices) - 1:
            pg.draw.line(surface=screen, color='blue', start_pos= [ProjX[Vertices[index] - 1], ProjY[Vertices[index] - 1]], end_pos=[ProjX[Vertices[index + 1] - 1], ProjY[Vertices[index + 1] - 1]], width=5)
            index += 1
        pg.draw.line(surface=screen, color='blue', start_pos=[ProjX[Vertices[index] - 1], ProjY[Vertices[index] - 1]],
                     end_pos=[ProjX[Vertices[0] - 1], ProjY[Vertices[0] - 1]], width=5)

        i += 1

def RenderScene(Scene: SceneManager.Scene, screen):
    i = 0
    while i < len(Scene.GameObjects):
        Object = list(Scene.GameObjects.values())[i]
        RenderObject(Object, screen)
        i += 1
