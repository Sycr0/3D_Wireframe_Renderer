from MyUtils import *

class GameObject:
    def __init__(self):
        # Model Values
        self.VertexTable = []
        self.RotatedVertexTable = []

        self.EdgeTable = [[tuple]]

        self.FaceTable = []

        self.ProjectedX = []
        self.ProjectedY = []

        self.transform = transform.__new__(transform)
        self.CompletedRotation = Vector3.__new__(Vector3)
        self.CompletedRotation.__init__(0,0,0)
        print("GameObject Initilialised")

class Camera:
    def __init__(self):
        self.NearPlane = 10000 #Higher = Closer??
        self.FOV = 30
        self.transform = transform.__new__(transform)
        self.transform.__init__()
        print("Camera Initilialised")

class Scene:
    def __init__(self):
        #List of all GameObjects in scene
        self.GameObjects = {}
        self.camera = Camera.__new__(Camera)
        self.camera.__init__()
        print("Scene Initilialised")

    def NewGameObject(self, Name: str, VertexTable: list, EdgeTable: list):
        object1 = GameObject.__new__(GameObject)
        self.GameObjects[Name] = object1
        object1.__init__()

        object1.VertexTable = VertexTable
        object1.EdgeTable = EdgeTable

        object1.transform.__init__()

        return object1

    def DeleteGameObject(self, Name: str):
        del self.GameObjects[Name]

Scenes = {
    "Default": Scene().__new__(Scene)
}
CurrentScene = Scenes.get("Default")
CurrentScene.__init__()