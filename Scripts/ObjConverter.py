import os

def GetVerticesInFile(FileName: str):
    # Get the path to the current file
    Script = os.path.abspath(__file__)

    # Go To the main directory in order to access the models folder
    MainDir = os.path.dirname(os.path.dirname(Script))

    # Access the models folder
    ModelsFolder = "Models"
    ModelsFolderPath = os.path.join(MainDir, ModelsFolder)

    # Access the model file
    ModelPath = os.path.join(ModelsFolderPath, FileName)

    # Read the file
    with open(ModelPath, 'r') as file:
        ModelData = file.read()
        # ModelData = ''.join([char for char in ModelData if not char.isalpha()])
        ModelData = ModelData.splitlines()
        ModelData = ModelData[3:]
        print(ModelData)

        Vertices = []
        Faces = []

        for line in ModelData:
            print("Current Line:", line)
            data = line[2:]
            print("Data: ", data)
            linedata = []
            currentVal = ''

            i = 0
            print("Length: ", len(data))
            while i < len(data):
                print(" ")
                print("----- NEW CHARACTER -----")
                char = data[i]

                if line[0] == 'v': DataType = "Vertex"
                elif line[0] == 'f': DataType = "Face"
                elif line[0] == 's': DataType = "Space"

                print("DataType: ", DataType)
                print("Current Character: ", char)
                if not char.isspace():
                    print("Previous Value: ", currentVal)
                    currentVal = str(currentVal) + str(char)
                    print("Current Value: ", currentVal)
                elif char.isspace():
                    print("Current Value: Space")
                    if DataType == 'Vertex': linedata.append(float(currentVal))
                    elif DataType == 'Face': linedata.append(int(currentVal))

                    currentVal = ''
                    print("Current Data: ", linedata)
                i += 1

            if DataType == 'Vertex': linedata.append(float(currentVal))
            elif DataType == 'Face': linedata.append(int(currentVal))

            print("Current Data: ", linedata)

            print("Data: ", linedata)

            if DataType == 'Vertex':
                Vertices.append(linedata)

            if DataType == 'Face':
                Faces.append(linedata)

            print("Vertices: ", Vertices)
            print("Faces: ", Faces)
            print("---------- END OF LINE ----------")
    return Vertices, Faces


