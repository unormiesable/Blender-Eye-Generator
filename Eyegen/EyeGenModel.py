import bpy
import os
import sys

def generate_eye(sclera_mat, iris_mat, pupil_mat, outer_mat):
    
    # Modelling

    base = bpy.ops.mesh.primitive_uv_sphere_add(
        location=(0, 0, 0),
        scale=(1, 1, 1),
    )
    base = bpy.context.object
    base.name = "Sclera"
    bpy.ops.object.shade_smooth()

    base.data.materials.append(sclera_mat)

    subdiv = base.modifiers.new(name="Subdiv", type="SUBSURF")
    subdiv.levels = 2
    subdiv.render_levels = 2

    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.context.tool_settings.mesh_select_mode = (False, False, True)

    bpy.ops.object.mode_set(mode='OBJECT')

    for face in base.data.polygons:
        vertices = [base.data.vertices[vertex_index].co for vertex_index in face.vertices]
        y_coords = [face.y for face in vertices]
        if any(y <= -0.99 for y in y_coords):
            face.select = True
        
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_more()

    bpy.ops.mesh.looptools_circle(custom_radius=False,
        fit='best', flatten=True,
        influence=100,
        radius=1,
        angle=0,
        regular=True)

    bpy.ops.mesh.extrude_region_move(
        MESH_OT_extrude_region={
            "use_normal_flip":False,
            "use_dissolve_ortho_edges":False,
            "mirror":False},
            TRANSFORM_OT_translate={
                "value":(0, 0, -0.0474732), 
                "orient_type":'NORMAL', 
                "orient_matrix":((0.720563, -5.91241e-08, 0.69339),
                                (-0.69339, 5.68945e-08, 0.720563),
                                (-8.20527e-08, -1, 0)),
                "orient_matrix_type":'NORMAL', 
                "constraint_axis":(False, False, True), 
                "mirror":False, "use_proportional_edit":False, 
                "proportional_edit_falloff":'SMOOTH', "proportional_size":1, 
                "use_proportional_connected":False, "use_proportional_projected":False, 
                "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, 
                "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, 
                "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), 
                "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, 
                "texture_space":False, 
                "remove_on_cancel":False, "use_duplicated_keyframes":False, 
                "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, 
                "use_automerge_and_split":False
                })
    
    bpy.ops.mesh.separate(type='SELECTED')

    iris = bpy.context.selected_objects[-1]
    iris.data.materials[0] = iris_mat
    iris.name = "Iris" 

    bpy.ops.object.editmode_toggle()
    bpy.ops.object.select_all(action="DESELECT")

    bpy.context.view_layer.objects.active = iris
    iris.select_set(True)

    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.context.tool_settings.mesh_select_mode = (False, False, True)

    bpy.ops.object.mode_set(mode='OBJECT')

    for face in iris.data.polygons:
        vertices = [iris.data.vertices[vertex_index].co for vertex_index in face.vertices]
        y_coords = [face.y for face in vertices]
        if any(y < -0.95 for y in y_coords):
            face.select = True

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.transform.resize(value=(0.9, 0.9, 0.9), orient_type='NORMAL')

    bpy.ops.mesh.looptools_circle(custom_radius=False,
        fit='best', flatten=True,
        influence=100,
        radius=1,
        angle=0,
        regular=True)

    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={
        "use_normal_flip":False, 
        "use_dissolve_ortho_edges":False, 
        "mirror":False}, 
        TRANSFORM_OT_translate={"value":(0, 0, -0.3), 
                                "orient_type":'NORMAL', 
                                "orient_matrix":((0.707107, -2.62726e-07, 0.707107), (-0.707107, 2.62726e-07, 0.707107), (-3.71551e-07, -1, 0)), 
                                "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, 
                                "use_proportional_edit":False, 
                                "proportional_edit_falloff":'SMOOTH', "proportional_size":0.424098, 
                                "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, 
                                "use_snap_project":False, "snap_target":'CLOSEST', 
                                "use_snap_self":True, "use_snap_edit":True, 
                                "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, 
                                "snap_normal":(0, 0, 0), "gpencil_strokes":False, 
                                "cursor_transform":False, "texture_space":False, 
                                "remove_on_cancel":False, "use_duplicated_keyframes":False, 
                                "view2d_edge_pan":False, "release_confirm":False, 
                                "use_accurate":False, "use_automerge_and_split":False})

    bpy.ops.mesh.select_more()

    bpy.ops.transform.translate(value=(0, 0.15, 0),
                                orient_type='LOCAL',
                                orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                                orient_matrix_type='LOCAL',
                                constraint_axis=(False, True, False),
                                mirror=True, use_proportional_edit=False,
                                proportional_edit_falloff='SMOOTH',
                                proportional_size=0.424098,
                                use_proportional_connected=False,
                                use_proportional_projected=False, snap=False,
                                snap_elements={'INCREMENT'}, use_snap_project=False,
                                snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True,
                                use_snap_nonedit=True, use_snap_selectable=False)

    bpy.ops.mesh.inset(thickness=0.0118955, depth=0)
    bpy.ops.mesh.separate(type='SELECTED')

    pupil = bpy.context.selected_objects[-1]
    pupil.data.materials[0] = pupil_mat
    pupil.name = "Pupil"

    bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action="DESELECT")

    outer = bpy.ops.mesh.primitive_uv_sphere_add(
        location=(0, 0, 0),
        scale=(1.01, 1.01, 1.01),
    )
    outer = bpy.context.object
    outer.name = "Outer"
    bpy.ops.object.shade_smooth()
    outer.data.materials.append(outer_mat)

    subdiv = outer.modifiers.new(name="Subdiv", type="SUBSURF")
    subdiv.levels = 2
    subdiv.render_levels = 2

    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.context.tool_settings.mesh_select_mode = (True, False, False)

    bpy.ops.object.mode_set(mode='OBJECT')

    for vert in outer.data.polygons:
        vertices = [outer.data.vertices[vertex_index].co for vertex_index in vert.vertices]
        y_coords = [vert.y for vert in vertices]
        if any(y <= -1.005 for y in y_coords) :
            vert.select = True 
    bpy.ops.object.mode_set(mode="EDIT")

    bpy.ops.mesh.select_less()

    bpy.context.scene.tool_settings.proportional_edit_falloff = 'SPHERE'

    bpy.ops.transform.translate(value=(-0, -0.07, -0),
                                orient_type='GLOBAL',
                                orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
                                orient_matrix_type='GLOBAL', 
                                constraint_axis=(False, True, False), 
                                mirror=True, use_proportional_edit=True, 
                                proportional_edit_falloff='SPHERE', 
                                proportional_size=0.466507, 
                                use_proportional_connected=False, 
                                use_proportional_projected=False, 
                                snap=False, snap_elements={'INCREMENT'}, 
                                use_snap_project=False, 
                                snap_target='CLOSEST', 
                                use_snap_self=True, 
                                use_snap_edit=True, 
                                use_snap_nonedit=True, 
                                use_snap_selectable=False)

    bpy.ops.object.mode_set(mode="OBJECT")

    bpy.ops.object.empty_add(location=(0, 0, 0))
    empty_obj = bpy.context.object
    empty_obj.name = "Eye"

    empty_obj.empty_display_size = 2.0

    # PARENTS
    iris.parent = base
    pupil.parent = base
    base.parent = outer
    outer.parent = empty_obj