import SceneManager

def __project(vertex: list, position: list, scale: list, Scene: SceneManager.Scene):
    x,y,z = vertex
    xpos,ypos,zpos = position
    xscale,yscale,zscale = scale

    FocalLength = Scene.camera.FocalLength

    camx, camy, camz = Scene.camera.transform.getPosition()

    FinalVertices = [camx - (x * xscale + xpos), camy - (y * yscale + ypos), camz - (z * zscale + zpos)]

    print("Vertices for projection = " + str(FinalVertices))

    try:
        ProjectedX = (FocalLength * FinalVertices[0]) / (FocalLength + FinalVertices[2]) + 400
        ProjectedY = (FocalLength * FinalVertices[1]) / (FocalLength + FinalVertices[2]) + 400
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
        returnX, returnY = __project(vertex=[x,y,z], position=[xpos, ypos, zpos], scale=[xscale,yscale,zscale], Scene=Scene)
        GameObject.ProjectedX.append(returnX)
        GameObject.ProjectedY.append(returnY)
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