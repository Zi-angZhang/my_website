import bpy
import math

cos = lambda x: math.cos(x / 180 * math.pi)
sin = lambda x: math.sin(x / 180 * math.pi)

radius_inner = 4.45 #cm
height = .7 #cm

spatial_resolution = 1 #1/10 cm
angle_resolution = 2 #1/2 degree

inner_split = 12
curves_height = .3 #amplitude of side curves

def inner_path(theta, z):
    x = radius_inner * cos(theta) + curves_height * cos(theta*inner_split)
    y = radius_inner * sin(theta) + curves_height * sin(theta*inner_split)
    return (x, y, z)

verts= [(0, 0, 0)]
faces = []
fack = []

for j in range(2):
    for i in range(1, 360*angle_resolution+1):
        theta = i / angle_resolution
        z = j * height
        verts.append(inner_path(theta, z))
        if j == 0:
            faces.append((0, i, i+1))
        else: 
            faces.append((360*angle_resolution+1 + i,  i,\
                    i+1, 360*angle_resolution + i + 2))
            faces.append((360*angle_resolution + 1, 360*angle_resolution+1+i, 360*angle_resolution+2+i))


    if j == 0:
        faces.pop(-1)
        faces.append((0, 1, 360*angle_resolution))
        print(len(verts))
        verts.append((0, 0, height))
    else:
        faces.pop(-1)
        faces.pop(-1)
        faces.append((360*angle_resolution+1, 360*angle_resolution+2, 720*angle_resolution+1))
        faces.append((360*angle_resolution, 1, 360*angle_resolution+2,  720*angle_resolution+1))
#j += 1
#z = height
#for i in range(0, 360*angle_resolution):
#    theta = i/angle_resolution
#    verts.append(out_path(theta, z))
#    verts.append(inner_path(theta, z))
#
#faces.pop(-1)

mesh = bpy.data.meshes.new('pressor')
obj = bpy.data.objects.new(mesh.name, mesh)
col = bpy.data.collections.get('Collection')
col.objects.link(obj)
bpy.context.view_layer.objects.active = obj

mesh.from_pydata(verts, [], faces)
        
        

        


