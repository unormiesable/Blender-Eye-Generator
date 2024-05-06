import bpy
    
def generate_outer():
    outer_material = bpy.data.materials.new(name="Outer_Material")
    outer_material.use_nodes = True
    principled_bsdf = outer_material.node_tree.nodes.get('Principled BSDF')
    principled_bsdf.inputs['Base Color'].default_value = (1, 1, 1, 1.0)
    principled_bsdf.inputs[3].default_value = 1.1
    principled_bsdf.inputs['Roughness'].default_value = 0.02
    principled_bsdf.inputs[12].default_value = 1
    principled_bsdf.inputs[17].default_value = 1
    return outer_material

def generate_sclera(sclera):
    sclera_material = bpy.data.materials.new(name="Sclera_Material")
    sclera_material.use_nodes = True
    principled_bsdf = sclera_material.node_tree.nodes.get('Principled BSDF')
    principled_bsdf.inputs['Base Color'].default_value = sclera
    principled_bsdf.inputs['Roughness'].default_value = 0.1
    principled_bsdf.inputs[12].default_value = 1
    return sclera_material

def generate_pupil(pupil):
    pupil_material = bpy.data.materials.new(name="Pupil_Material")
    pupil_material.use_nodes = True
    principled_bsdf = pupil_material.node_tree.nodes.get('Principled BSDF')
    principled_bsdf.inputs['Base Color'].default_value = pupil
    principled_bsdf.inputs['Roughness'].default_value = 0.02
    principled_bsdf.inputs[12].default_value = 1
    return pupil_material

def generate_iris(iris):
    iris_material = bpy.data.materials.new(name="Iris_Material")
    iris_material.use_nodes = True
    tree = iris_material.node_tree
    principled_bsdf = iris_material.node_tree.nodes.get('Principled BSDF')

    noise_texture = tree.nodes.new(type='ShaderNodeTexNoise')
    noise_texture.location = (-1000, -100)
    noise_texture.inputs['Scale'].default_value = 25.0 
    noise_texture.inputs['Detail'].default_value = 5.0
    noise_texture.inputs['Roughness'].default_value = 0.3

    bump_node = tree.nodes.new(type='ShaderNodeBump')
    bump_node.location = (-700, 100)
    bump_node.inputs['Strength'].default_value = 0.5
    tree.links.new(noise_texture.outputs['Fac'], bump_node.inputs['Height'])
    tree.links.new(bump_node.outputs['Normal'], principled_bsdf.inputs['Normal'])

    principled_bsdf.inputs['Base Color'].default_value = iris
    principled_bsdf.inputs['Roughness'].default_value = 0.02
    return iris_material
