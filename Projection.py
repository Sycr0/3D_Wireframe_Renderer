import math
from MyUtils import *
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
    Transform = GameObject.transform
    xpos,ypos,zpos = Transform.position.x, Transform.position.y, Transform.position.z
    xscale,yscale,zscale = Transform.scale.x, Transform.scale.y, Transform.scale.z
    GameObject.ProjectedX = []
    GameObject.ProjectedY = []

    print("Vertex Table" + str(GameObject.VertexTable))
    print("Rotated Vertex Table: " + str(GameObject.RotatedVertexTable))

    i = 0
    while i < len(GameObject.RotatedVertexTable):
        x, y, z = GameObject.RotatedVertexTable[i]
        print()
        print("-------------")
        print("Position")
        print(x, y, z)
        print("Near Plane Position")
        print(Scene.camera.transform.position.z + Scene.camera.NearPlane)
        if z < Scene.camera.transform.position.z + Scene.camera.NearPlane:
            print("Allowed")
            returnX, returnY = __project(vertex=[x,y,z], position=[xpos, ypos, zpos], scale=[xscale,yscale,zscale], Scene=Scene)
            GameObject.ProjectedX.append(returnX)
            GameObject.ProjectedY.append(returnY)
        else:
            print("Denied")
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

def RotateModel(VerticesToRotate, xRotation: float, yRotation: float, zRotation: float):

    FinalVertices = []

    i = 0
    while i < len(VerticesToRotate):

        x = VerticesToRotate[i][0]
        y = VerticesToRotate[i][1]
        z = VerticesToRotate[i][2]

        # X Rotation
        y,z = __rotate(y, z, xRotation)

        # Y Rotation
        x, z = __rotate(x, z, yRotation)

        # Z Rotation
        x, y = __rotate(x, y, zRotation)

        FinalVertices.append([x,y,z])

        print("Finished One Vertex")
        print("i = " + str(i))
        print(FinalVertices[i])

        i += 1

    print("Rotated Vertex Table: ")
    print(FinalVertices)

    return FinalVertices

def RotateModelToAngle(GameObject: SceneManager.GameObject, xAngle, yAngle, zAngle):
    completedRotation = GameObject.CompletedRotation
    xr, yr, zr = completedRotation.x, completedRotation.y, completedRotation.z
    print("Completed Rotation: " + str([xr, yr, zr]))
    print("Angle to Rotate to: " + str([xAngle, yAngle, zAngle]))

    if xr != xAngle or yr != yAngle or zr != zAngle:
        print("Calculating")
        VerticesToRotate = GameObject.VertexTable

        xAngleToRotate = xAngle - xr
        yAngleToRotate = yAngle - yr
        zAngleToRotate = zAngle - zr
        print("Amount To Rotate: " + str([xAngleToRotate, yAngleToRotate, zAngleToRotate]))

        RotatedVertices = RotateModel(VerticesToRotate, xAngleToRotate, yAngleToRotate, zAngleToRotate)
        GameObject.RotatedVertexTable = RotatedVertices

    GameObject.CompletedRotation.x, GameObject.CompletedRotation.y, GameObject.CompletedRotation.z = xAngle, yAngle, zAngle