bl_info = {
    "name": "Eye Generator",
    "author": "Atthariq Insanulhaq Supiana",
    "version": (1, 0),
    "blender": (4, 1, 0),
    "location" : "View3D > Sidebar",
    "description": "Eye Generator V1 can help you to Make Eyes in a few clicks",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "Object",
}

import bpy
from .EyeGenMain import SimplePanel, GenerateEyeButton
def register():

    bpy.utils.register_class(SimplePanel)
    bpy.utils.register_class(GenerateEyeButton)
    
    bpy.types.Scene.pupil_color = bpy.props.FloatVectorProperty(name="Pupil Color",
    subtype='COLOR',
    size=4,
    default=(0.0, 0.0, 0.0, 1.0), min = 0.0, max = 1.0, soft_min=0.0, soft_max=1.0)
    
    bpy.types.Scene.iris_color = bpy.props.FloatVectorProperty(name="Iris Color",
    subtype='COLOR',
    size=4,
    default=(0.060477, 0.029964, 0.005565, 1.0), min = 0.0, max = 1.0, soft_min=0.0, soft_max=1.0)

    bpy.types.Scene.sclera_color = bpy.props.FloatVectorProperty(name="Sclera Color",
    subtype='COLOR',
    size=4,
    default=(1.0, 1.0, 1.0, 1.0), min = 0.0, max = 1.0, soft_min=0.0, soft_max=1.0)

def unregister():
    bpy.utils.unregister_class(SimplePanel)
    bpy.utils.unregister_class(GenerateEyeButton)
    del bpy.types.Scene.pupil_color
    del bpy.types.Scene.iris_color
    del bpy.types.Scene.sclera_color

if __name__ == "__main__":
    register()