from MyUtils import *

newtransform = transform.__new__(transform)

newtransform.position = Vector3(100,50,0)
newtransform.rotation = Vector3(0,100,50)
newtransform.scale = Vector3(50,0,100)

print(newtransform)

print(newtransform.position.x, newtransform.position.y, newtransform.position.z)
print(newtransform.rotation.x, newtransform.rotation.y, newtransform.rotation.z)
print(newtransform.scale.x, newtransform.scale.y, newtransform.scale.z)