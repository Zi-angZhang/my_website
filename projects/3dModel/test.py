from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
from stl import mesh
figure = plt.figure()
axes = mplot3d.Axes3D(figure)
my_mesh = mesh.Mesh.from_file("BASE_AsianLantern2.stl")
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(my_mesh.vectors))

scale = my_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)
plt.show()
