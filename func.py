import bpy

def leg_transform(context,obj):
    bpy.ops.object.select_all(action='DESELECT')
    context.view_layer.objects.active = obj
    context.object.select = True
    bpy.ops.object.duplicate_move()
    for mod in context.object.modifiers:
        bpy.ops.object.modifier_apply(modifier=mod.name)

    high = context.object.data.vertices[0].co[2]
    for point in context.object.data.vertices:
        if high > point.co[2]:
            high = point.co[2]

    bpy.ops.object.delete()
    return high

def leg_to_ground(context):
    arm = context.object
    bone = context.active_pose_bone
    bpy.ops.object.mode_set(mode='OBJECT')
    bone_left = context.scene.imotion.target_bone_left
    bone_right = context.scene.imotion.target_bone_right
    if bone.name == bone_left:
        obj_left = context.scene.imotion.target_mesh_left
        high = leg_transform(context,obj_left)
    elif bone.name == bone_right:
        obj_right = context.scene.imotion.target_mesh_right
        high = leg_transform(context, obj_right)
    else:
        return

    context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='POSE')
    axis = context.scene.imotion.control_axis
    if axis == "X":
        bone.location[0] -= high
    elif axis == "Y":
        bone.location[1] -= high
    elif axis == "Z":
        bone.location[2] -= high
