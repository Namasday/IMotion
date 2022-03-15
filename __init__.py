bl_info = {
    "name": "IMotion",
    "author": "Iyinpic",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Tool Shelf > IMotion Panel",
    "description": "动画",
    "warning": "",
    "doc_url": "",
    "category": "Animation",
}

import bpy
from bpy.props import PointerProperty

list_cls = []
def register_list(cls):
    list_cls.append(cls)
    return cls

from . import (
    properties,
    opers,
    panel,
    func,
    )

def register():
    for cls in list_cls:
        bpy.utils.register_class(cls)

    bpy.types.Scene.imotion = PointerProperty(type=properties.IMProps)

def unregister():
    for cls in list_cls:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.imotion

if __name__ == '__main__':
    register()