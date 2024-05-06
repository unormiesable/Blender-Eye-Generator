import bpy
import os
import sys
from .Eyegen import EyeGenModel as Model
from .Eyegen import EyeGenMaterial as mater

class SimplePanel(bpy.types.Panel):
    bl_label = "Eye Generator"
    bl_idname = "EYEGENERATORID"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Eye Generator"

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Pupil Color :")
        row = layout.row()
        row.prop(context.scene, "pupil_color", text="")

        layout.label(text="Iris Color :")
        row = layout.row()
        row.prop(context.scene, "iris_color", text="")

        layout.label(text="Sclera Color :")
        row = layout.row()
        row.prop(context.scene, "sclera_color", text="")
        
        layout.separator(factor=1)
        
        layout.operator("object.generate_eye", text="Generate Eye")

class GenerateEyeButton(bpy.types.Operator):
    bl_idname = "object.generate_eye"
    bl_label = "Generate Eye"
    
    def execute(self, context):
        Model.generate_eye(mater.generate_sclera(bpy.context.scene.sclera_color),
                           mater.generate_iris(bpy.context.scene.iris_color),
                            mater.generate_pupil(bpy.context.scene.pupil_color),
                             mater.generate_outer())
        
        self.report({'INFO'}, "Eye's Generated!")
        return {'FINISHED'}