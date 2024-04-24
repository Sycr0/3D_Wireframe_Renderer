import math

import SceneManager

def __project(vertex: list, position: list, scale: list, Scene: SceneManager.Scene):
    x,y,z = vertex
    xpos,ypos,zpos = position
    xscale,yscale,zscale = scale

    FocalLength = Scene.camera.FocalLength
    FOV = Scene.camera.FOV

    camx, camy, camz = Scene.camera.transform.getPosition()



    FinalVertices = [camx - (x * xscale + xpos), camy - (y * yscale + ypos), camz - (z + zpos)]

    print("Vertices for projection = " + str(FinalVertices))

    angle = (FOV / 180) * math.pi
    try:
        ProjectedX = FinalVertices[0] / (FinalVertices[2] * math.tan(angle / 2)) + 400
        ProjectedY = FinalVertices[1] / (FinalVertices[2] * math.tan(angle / 2)) + 400
        return ProjectedX, ProjectedY
    except(ZeroDivisionError, ValueError):
        print("Error: ZeroDivision or Value")
        return 0,0


def CalculateProjectedValues(GameObject: type(SceneManager.GameObject), Scene: SceneManager.Scene):
    transform = GameObject.transform
    xpos,ypos,zpos = transform.position.x, transform.position.y, transform.position.z
    xscale,yscale,zscale = transform.scale.x, transform.scale.y, transform.scale.z

    GameObject.ProjectedX = []
    GameObject.ProjectedY = []

    i = 0
    while i < len(GameObject.VertexTable):
        x, y, z = GameObject.VertexTable[i]
        if z < Scene.camera.NearPlane + Scene.camera.transform.position.z:
            returnX, returnY = __project(vertex=[x,y,z], position=[xpos, ypos, zpos], scale=[xscale,yscale,zscale], Scene=Scene)
            GameObject.ProjectedX.append(returnX)
            GameObject.ProjectedY.append(returnY)
        else:
            GameObject.ProjectedX.append("n")
            GameObject.ProjectedY.append("n")
        i += 1

    print("X Projected: ")
    print(GameObject.ProjectedX)
    print("Y Projected: ")
    print(GameObject.ProjectedY)


def ProjectValuesInScene(_scene: SceneManager.Scene):
    Scene = SceneManager.Scenes.get(_scene)
    for GameObject in Scene.GameObjects:
        CalculateProjectedValues(GameObject=GameObject, Scene=_scene)

    print("Camera Position = ")
    print(Scene.camera.transform.getPosition())

def __rotate(x: float, y: float,  xangle: float, yangle: float):
    xr = math.cos(xangle) * x + math.cos(xangle) * x
    yr = -math.sin(yangle) * y + math.cos(yangle) * y
    return xr, yr

def RotateModel(GameObject: SceneManager.GameObject, Scene: SceneManager.Scene):
    i = 0
    while i < len(GameObject.VertexTable):
        __rotate()