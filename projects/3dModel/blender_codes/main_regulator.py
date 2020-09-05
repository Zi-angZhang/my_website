import bpy
import math

cos = lambda x: math.cos(x / 180 * math.pi)
sin = lambda x: math.sin(x / 180 * math.pi)

radius_outer = 5 #cm
radius_inner = 4.5 #cm
height = 0 #cm

spatial_resolution = 1 #1/10 cm
angle_resolution = 1 #1/2 degree

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

for j in range(1 + height * spatial_resolution):
    for i in range(0, 361*angle_resolution):
        theta = i / angle_resolution
        z = j / spatial_resolution
        verts.append(out_path(theta, z))
        verts.append(inner_path(theta, z))
        if j == 0:
            faces.append((2*i, 2*i+1, 2*i+3, 2*i+2))
        else: 
            faces.append((len(verts), len(verts)-2, \
                    len(verts) - 360*angle_resolution - 2, len(verts) - 360*angle_resolution))
            faces.append((len(verts)-1, len(verts)+1, \
                    len(verts) - 360*angle_resolution + 1, len(verts) - 360*angle_resolution-1))
    if j == 0:
        faces.pop(-1)
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
        
        

        


