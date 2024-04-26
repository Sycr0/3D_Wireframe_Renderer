from Scripts.Sy3D_MyUtils import *

class GameObject:
    def __init__(self):
        self.Name = ""

        # Model Values
        self.VertexTable = []
        self.RotatedVertexTable = []

        self.EdgeTable = [[tuple]]

        self.FaceTable = []

        self.ProjectedX = []
        self.ProjectedY = []

        self.transform = transform.__new__(transform)
        print("GameObject Initilialised")

class Camera:
    def __init__(self):
        self.NearPlane = 20 #Higher = Closer??
        self.FOV = 90
        self.transform = transform.__new__(transform)
        self.transform.__init__()
        print("Camera Initilialised")

class Scene:
    def __init__(self, Name):
        self.Name = Name

        #List of all GameObjects in scene
        self.GameObjects = {}
        self.camera = Camera.__new__(Camera)
        self.camera.__init__()
        print("Scene Initilialised")

    def NewGameObject(self, Name: str, VertexTable: list, EdgeTable: list):
        object1 = GameObject.__new__(GameObject)
        self.GameObjects[Name] = object1
        object1.__init__()

        object1.Name = Name

        object1.VertexTable = VertexTable
        object1.EdgeTable = EdgeTable

        object1.transform.__init__()

        return object1

    def DeleteGameObject(self, Name: str):
        del self.GameObjects[Name]

Scenes = {
    "Default": Scene(Name="Default").__new__(Scene)
}
CurrentScene = Scenes.get("Default")
CurrentScene.__init__("Default")
print("Scene Name: " + CurrentScene.Name)