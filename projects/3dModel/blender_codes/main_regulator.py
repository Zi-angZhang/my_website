import bpy
import math

cos = lambda x: math.cos(x / 180 * math.pi)
sin = lambda x: math.sin(x / 180 * math.pi)

radius_outer = 5 #cm
radius_inner = 4.5 #cm
height = 5 #cm

spatial_resolution = 1 #1/10 cm
angle_resolution = 2 #1/2 degree

inner_split = 12
curves_height = .3 #amplitude of side curves

def out_path(theta, z):
    x = radius_outer * cos(theta)
    y = radius_outer * sin(theta)
    return (x, y, z)

def inner_path(theta, z):
    x = radius_inner * cos(theta) + curves_height * cos(theta*inner_split)
    y = radius_inner * sin(theta) + curves_height * sin(theta*inner_split)
    return (x, y, z)

verts= []
faces = []
fack = []

for j in range(2):
    for i in range(0, 360*angle_resolution):
        theta = i / angle_resolution
        z = j * height
        verts.append(out_path(theta, z))
        verts.append(inner_path(theta, z))
        if j == 0:
            faces.append((2*i, 2*i+1, 2*i+3, 2*i+2))
        else: 
            faces.append((720*angle_resolution + 2*i, 720*angle_resolution*(j-1) + 2*i,\
                   720*angle_resolution*(j-1) + 2*i+2, 720*angle_resolution*j + 2*i + 2))
            faces.append((720*angle_resolution + 2*i+1, 2*i+1,\
                   2*i+3, 720*angle_resolution + 2*i + 3))
            faces.append((720*angle_resolution+ 2*i, 720*angle_resolution+ 2*i+1, 720*angle_resolution+2*i+3, 720*angle_resolution+2*i+2))


    if j == 0:
        faces.pop(-1)
        faces.append((0,1, 720*angle_resolution-1, 720*angle_resolution-2))
        print(len(verts))
    else:
        faces.pop(-1)
        faces.pop(-1)
        faces.pop(-1)
        faces.append((0, 720*angle_resolution-2, 2*720*angle_resolution-2, 720*angle_resolution))
        faces.append((1, 720*angle_resolution-1, 2*720*angle_resolution-1, 720*angle_resolution+1))
        faces.append((720*angle_resolution+ 0,720*angle_resolution+ 1, 720*angle_resolution+ 720*angle_resolution-1, 720*angle_resolution+ 720*angle_resolution-2))
#j += 1
#z = height
#for i in range(0, 360*angle_resolution):
#    theta = i/angle_resolution
#    verts.append(out_path(theta, z))
#    verts.append(inner_path(theta, z))
#
#faces.pop(-1)

mesh = bpy.data.meshes.new('regulator')
obj = bpy.data.objects.new(mesh.name, mesh)
col = bpy.data.collections.get('Collection')
col.objects.link(obj)
bpy.context.view_layer.objects.active = obj

mesh.from_pydata(verts, [], faces)
        
        

        


