import bpy

from . import register_list

@register_list
class IMOTION_PT_View3D(bpy.types.Panel):
    bl_idname = "IMOTION_PT_BM"
    bl_label = "骨骼运动"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "IMotion"

    def draw(self,context):
        scn = context.scene.imotion
        ob = context.object
        layout = self.layout

        row = layout.row()
        c = row.column()
        c.prop(scn, 'target_mesh_left', text="左足鞋")
        c.prop(scn, 'target_mesh_right', text="右足鞋")
        if ob.pose:
            c.prop_search(scn, 'target_bone_left', ob.pose, 'bones', text="左足骨",icon='BONE_DATA')
            c.prop_search(scn, 'target_bone_right', ob.pose, 'bones', text="右足骨",icon='BONE_DATA')
            c.row(heading="控制轴",align=True).prop(scn,'control_axis',expand=True)
            c.operator("bm.ltg",text="足鞋贴地")

            col = layout.column()
            row = col.row(align=True)
            row.prop(scn, 'key_start')
            row.prop(scn, 'key_end')
            col.operator("bm.ltgk",text="足鞋贴地插帧")

        row = layout.row()
        c=row.column()
        c.prop(scn, 'em_leftleg', text="左脚空物体")
        c.prop(scn, 'em_rightleg', text="右脚空物体")
        c.row(heading="控制轴",align=True).prop(scn,'control_axis_center',expand=True)
        c.row(heading="选择脚", align=True).prop(scn, 'charge_in', expand=True)
        c.operator("bm.ctg", text="重心着地")