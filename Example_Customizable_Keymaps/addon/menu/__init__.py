import bpy

from .pie import ECK_MT_Pie_Menu

classes = (
    ECK_MT_Pie_Menu,
)


def register_menus():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_menus():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
