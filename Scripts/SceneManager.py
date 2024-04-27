from Scripts.MyUtils import *
import ObjConverter

class GameObject:
    def __init__(self):
        self.Name = ""
        self.ModelFileName = ""

        # Model Values
        self.VertexTable = []
        self.RotatedVertexTable = []

        self.FaceTable = [[3]]

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

    def NewGameObject(self, Name: str, ModelFileName: str):
        object1 = GameObject.__new__(GameObject)
        self.GameObjects[Name] = object1
        object1.__init__()

        object1.Name = Name
        object1.ModelFileName = ModelFileName

        object1.VertexTable, object1.FaceTable = ObjConverter.GetVerticesInFile(object1.ModelFileName)
        print("Vertex Table: ", object1.VertexTable)
        print("Face Table: ", object1.FaceTable)

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