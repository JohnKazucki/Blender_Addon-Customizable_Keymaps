import bpy


# To better understand what values a keymap needs to work, check out this resource:
# https://github.com/brybalicious/toggle_mmb_numpad/blob/master/keymap_implementation.md
# It goes over all the possible Keymap Names, Region/Map/Space/Key Types, Values, etc.

# This implementation does not include the Region or Map Types
# For most use cases they are not very relevant, so they have been deliberately omitted here

keymaps =[
            # 3D View Keymaps
            {
                # Keymap name, this is one of 224 hardcoded strings from Blender
                "name": "3D View", 
                # Space Type, one of these https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items
                # This relates to the editor you wish to have the keymap work in. Such as the Node Editor or Console, etc.
                "space_type": "VIEW_3D", 
                # A list of KeyMap Items (kmi), each item being one shortcut
                "items":
                [
                    # Calling a Pie Menu
                    {
                        "operator": "wm.call_menu_pie", # wm.call_menu_pie is a built in operator 
                        "type": "C", # Key Types, what mouse or keyboard button is pressed to call the operator
                        "value": "PRESS", # Value, What type of button action must be performed to call this operator, usually PRESS is all that is needed
                        "prop_name": "ECK_MT_Pie_Menu", # pie menu that you want to call

                        # Modifier keys, pressed together with the key in "type"
                        "shift": False,
                        "ctrl": False,
                        "alt": True,
                        "oskey": False,
                    },
                    # Calling a regular Operator
                    {
                        "operator": "object.eck_simpleoperator", 
                        "type": "D",
                        "value": "PRESS",
                        # prop_name is not applicable for regular operators
                        # "prop_name": "", 
                        "shift": False,
                        "ctrl": False,
                        "alt": False,
                        "oskey": False,
                    },
                ]
            },
            # UV Editor Keymaps
            {
                "name": "UV Editor",
                "space_type": "EMPTY",
                "items":
                [
                    # Calling a Pie Menu
                    {
                        "operator": "wm.call_menu_pie", # wm.call_menu_pie is a built in operator 
                        "type": "C",
                        "value": "PRESS",
                        "prop_name": "ECK_MT_Pie_Menu", # pie menu that you want to call
                        "shift": False,
                        "ctrl": False,
                        "alt": True,
                        "oskey": False,
                    },
                    # Calling a regular Operator
                    {
                        "operator": "object.eck_simpleoperator", 
                        "type": "D",
                        "value": "PRESS",
                        # prop_name is not applicable for regular operators
                        # "prop_name": "", 
                        "shift": False,
                        "ctrl": False,
                        "alt": False,
                        "oskey": False,
                    },
                ]
            },            
        ]


# to keep track of the custom keymaps this addon adds to Blender. These will be removed again when we unregister/disable the addon
keys = []



def register_keymap():

    wm = bpy.context.window_manager
    addon_keyconfig = wm.keyconfigs.addon

    kc = addon_keyconfig

    for keymap in keymaps:
        name = keymap["name"]
        space_type = keymap["space_type"]

        km = kc.keymaps.new(name=name, space_type=space_type)

        for item in keymap["items"]:
            operator = item["operator"]
            type = item["type"]
            value = item["value"]

            shift = item["shift"]
            ctrl = item["ctrl"]
            alt = item["alt"]
            oskey = item["oskey"]

            kmi = km.keymap_items.new(operator, type=type, value=value, shift=shift, ctrl=ctrl, alt=alt, oskey=oskey)

            if "prop_name" in item:
                kmi.properties.name = item["prop_name"]
            kmi.active = True

    keys.append((km, kmi))
    


def unregister_keymap():

    wm = bpy.context.window_manager

    for km, kmi in keys:
        km.keymap_items.remove(kmi)
    keys.clear()
