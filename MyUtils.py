class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print("Vector3 Initiliased")

class transform:
    def __init__(self):
        self.position = Vector3(0, 0, 0)
        self.rotation = Vector3(0, 0, 0)
        self.scale = Vector3(1, 1, 1)
        print("Transform Initiliased")

    def getPosition(self):
        return self.position.x, self.position.y, self.position.z
    def getRotation(self):
        return self.rotation.x, self.rotation.y, self.rotation.z
    def getScale(self):
        return self.scale.x, self.scale.y, self.scale.z