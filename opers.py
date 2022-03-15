import bpy
from bpy.types import Operator

from . import func

from . import register_list

@register_list
class BM_OT_LegToGround(Operator):
    bl_idname = "bm.ltg"
    bl_label = "足鞋贴地"

    def execute(self,context):
        func.leg_to_ground(context)
        return {"FINISHED"}

@register_list
class BM_OT_LegToGroundKeys(Operator):
    bl_idname = "bm.ltgk"
    bl_label = "足鞋贴地插帧"

    def execute(self,context):
        key_start = context.scene.imotion.key_start
        key_end = context.scene.imotion.key_end
        origin = bpy.context.scene.frame_current
        for i in range(key_start,key_end+1):
            bpy.context.scene.frame_current = i
            func.leg_to_ground(context)
            bpy.ops.anim.keyframe_insert_menu(type='Location')

        bpy.context.scene.frame_current = origin
        return {"FINISHED"}