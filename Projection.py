import math

import SceneManager

def __project(vertex: list, position: list, scale: list, Scene: SceneManager.Scene):
    x,y,z = vertex
    xpos,ypos,zpos = position
    xscale,yscale,zscale = scale

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
    while i < len(GameObject.RotatedVertexTable):
        x, y, z = GameObject.RotatedVertexTable[i]
        if z < Scene.camera.transform.position.z + Scene.camera.NearPlane:
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

def __rotate(x, y, _angle):
    angle = math.radians(_angle)
    xr = (math.degrees(math.cos(angle)) * x)   -   (math.degrees(math.sin(angle)) * y)
    yr = (math.degrees(math.sin(angle)) * x)   +   (math.degrees(math.cos(angle)) * y)
    return xr, yr

def RotateModel(GameObject: SceneManager.GameObject, xRotation: float, yRotation: float, zRotation: float):
    if len(GameObject.VertexTable) == len(GameObject.RotatedVertexTable):
        VerticesToRotate = GameObject.RotatedVertexTable.copy()
    else:
        VerticesToRotate = GameObject.VertexTable.copy()
    GameObject.RotatedVertexTable.clear()

    i = 0
    while i < len(VerticesToRotate):
        print(GameObject.RotatedVertexTable)
        x = VerticesToRotate[i][0]
        y = VerticesToRotate[i][1]
        z = VerticesToRotate[i][2]

        # X Rotation
        y,z = __rotate(y, z, xRotation)

        # Y Rotation
        x, z = __rotate(x, z, yRotation)

        # Z Rotation
        x, y = __rotate(x, y, zRotation)

        GameObject.RotatedVertexTable.append([x,y,z])
        i += 1
        print("Finished One Vertex")
        print("i = " + str(i))

    print("Rotated Vertex Table: ")
    print(GameObject.RotatedVertexTable)