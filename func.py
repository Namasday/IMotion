import bpy

def leg_transform(context,obj):
    bpy.ops.object.select_all(action='DESELECT')
    context.view_layer.objects.active = obj
    context.object.select_set(True)
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

def center_to_ground(context):
    bone = context.active_pose_bone
    em_l = context.scene.imotion.em_leftleg
    em_r = context.scene.imotion.em_rightleg
    axis = int(context.scene.imotion.control_axis_center)
    charge = context.scene.imotion.charge_in
    accuracy = 0.001

    LEFT = 'el - em_l.matrix_world[2][3]'
    RIGHT = 'er - em_r.matrix_world[2][3]'
    ALL = 'eval(LEFT) + eval(RIGHT)'
    charge = eval(charge)

    while True:
        el = em_l.matrix_world[2][3]
        er = em_r.matrix_world[2][3]

        bone.location[axis] = bone.location[axis] - accuracy
        bpy.ops.object.mode_set(mode='OBJECT')                      #刷新约束创建的世界矩阵

        if eval(charge) < accuracy * 0.01:
            bone.location[axis] = bone.location[axis] + accuracy
            break
        else:
            continue

    bpy.ops.object.mode_set(mode='POSE')