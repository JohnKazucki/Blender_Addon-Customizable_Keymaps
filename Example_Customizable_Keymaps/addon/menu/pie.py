import bpy
from bpy.types import Menu

class ECK_MT_Pie_Menu(Menu):
    bl_idname = "ECK_MT_Pie_Menu"
    bl_label = "Example Pie Menu"

    def draw(self, context):

        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'

        pie = layout.menu_pie()

        # WEST
        pieItemRow = pie.row()
        pieItemRow.operator("object.eck_simpleoperator", icon='HIDE_ON', text="Simple Operator")

        # EAST
        pieItemRow = pie.row()
        pieItemRow.operator("object.eck_simpleoperator", icon='HIDE_ON', text="Simple Operator")

        # SOUTH
        pieItemRow = pie.row()
        pieItemRow.operator("object.eck_simpleoperator", icon='HIDE_ON', text="Simple Operator")

        # NORTH
        pieItemRow = pie.row()
        pieItemRow.operator("object.eck_simpleoperator", icon='HIDE_ON', text="Simple Operator")
        

        # NORTH WEST
        pieItemRow = pie.row()
        pieItemRow.operator("object.eck_simpleoperator", icon='HIDE_ON', text="Simple Operator")

        # NORTH EAST
        pieItemRow = pie.row()
        pieItemRow.operator("object.eck_simpleoperator", icon='HIDE_ON', text="Simple Operator")
    
        # SOUTH WEST
        pieItemRow = pie.row()
        pieItemRow.operator("object.eck_simpleoperator", icon='HIDE_ON', text="Simple Operator")

        # SOUTH EAST
        pieItemRow = pie.row()
        pieItemRow.operator("object.eck_simpleoperator", icon='HIDE_ON', text="Simple Operator")
