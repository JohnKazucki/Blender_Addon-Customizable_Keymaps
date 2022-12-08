import bpy

from bpy.types import Operator


class ECK_OT_SIMPLEOPERATOR(Operator):
    bl_idname = "object.eck_simpleoperator"
    bl_label = "Example Simple Operator"
    bl_description = "Pops up an Info message"

    def execute(self, context):

        self.report({'INFO'}, "Custom Keymap in action!")

        return {'FINISHED'}
