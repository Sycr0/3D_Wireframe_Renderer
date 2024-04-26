import math
import SceneManager

def __project(vertex: list, position: list, scale: list, Scene: SceneManager.Scene):
    x,y,z = vertex
    xpos,ypos,zpos = position
    xscale,yscale,zscale = scale

    FOV = Scene.camera.FOV

    camx, camy, camz = Scene.camera.transform.getPosition()



    FinalVertices = [camx - (x * xscale + xpos), camy - (y * yscale + ypos), camz - (z + zpos)]

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
        print(Scene.camera.transform.position.z + Scene.camera.NearPlane)
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

def __rotate(_x, _y, _z, _pitch, _roll, _yaw):
    x, y, z = math.radians(_x), math.radians(_y), math.radians(_z)
    pitch, roll, yaw = math.radians(_pitch), math.radians(_roll), math.radians(_yaw)

    xRotated = math.cos(yaw) * math.cos(pitch) * x + (math.cos(yaw) * math.sin(pitch) * math.sin(roll) - math.sin(yaw) * math.cos(roll)) * y + (math.cos(yaw) * math.sin(pitch) * math.cos(roll) + math.sin(yaw) * math.sin(roll)) *z
    yRotated = math.sin(yaw) * math.cos(pitch) * x + (math.sin(yaw) * math.sin(pitch) * math.sin(roll) + math.cos(yaw) * math.cos(roll)) * y + (math.sin(yaw) * math.sin(pitch) * math.cos(roll) - math.cos(yaw) * math.sin(roll)) * z
    zRotated = -math.sin(pitch) * x + math.cos(pitch) * math.sin(roll) * y + math.cos(pitch) * math.cos(roll) * z

    return math.degrees(xRotated), math.degrees(yRotated), math.degrees(zRotated)

def RotateModel(VerticesToRotate, xRotation: float, yRotation: float, zRotation: float):

    FinalVertices = []

    i = 0
    while i < len(VerticesToRotate):

        x, y, z  = VerticesToRotate[i][0:3]

        # X Rotation
        x, y, z = __rotate(x, y, z, xRotation, yRotation, zRotation)

        FinalVertices.append([x,y,z])

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

        RotatedVertices = RotateModel(VerticesToRotate, xAngle, yAngle, zAngle)
        GameObject.RotatedVertexTable = RotatedVertices

    GameObject.CompletedRotation.x, GameObject.CompletedRotation.y, GameObject.CompletedRotation.z = xAngle, yAngle, zAngle