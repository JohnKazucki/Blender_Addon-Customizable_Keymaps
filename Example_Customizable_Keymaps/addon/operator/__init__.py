import bpy

from .simple_operator import ECK_OT_SIMPLEOPERATOR


classes = (
    ECK_OT_SIMPLEOPERATOR,
)


def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
