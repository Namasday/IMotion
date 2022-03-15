import bpy
from bpy.types import PropertyGroup
from bpy.props import StringProperty,PointerProperty,EnumProperty,IntProperty

from . import register_list

def get_bone_left(prop):
    return prop.get('target_bone_left', '')

def set_bone_left(prop, value):
    bones = bpy.context.object.data.bones
    if value not in bones:
        return
    else:
        prop['target_bone_left'] = value

def get_bone_right(prop):
    return prop.get('target_bone_right', '')

def set_bone_right(prop, value):
    bones = bpy.context.object.data.bones
    if value not in bones:
        return
    else:
        prop['target_bone_right'] = value

@register_list
class IMProps(PropertyGroup):
    target_mesh_left : PointerProperty(
        name="目标左足鞋",
        type=bpy.types.Object,
        description="被控制的物体",
    )

    target_mesh_right : PointerProperty(
        name="目标右足鞋",
        type=bpy.types.Object,
        description="被控制的物体",
    )

    target_bone_left: StringProperty(
        name='目标左足骨',
        description='用于控制z轴位移的足骨',
        default='',
        get=get_bone_left,
        set=set_bone_left,
    )

    target_bone_right: StringProperty(
        name='目标右足骨',
        description='用于控制z轴位移的足骨',
        default='',
        get=get_bone_right,
        set=set_bone_right,
    )

    control_axis : EnumProperty(
        name="控制轴",
        description="骨骼纵向移动的轴",
        items=[
            ('X', 'X', "", 0),
            ('Y', 'Y', "", 1),
            ('Z', 'Z', "", 2),
            ],
        default=2,
    )

    key_start : IntProperty(
        name="插帧起始点",
        description="足骨贴地插帧的开始帧数",
        min=0,
    )

    key_end: IntProperty(
        name="插帧结束点",
        description="足骨贴地插帧的结束帧数",
        min = 0,
    )