import bpy


keymaps =[
            # 3D View Keymaps
            {
                "name": "3D View",
                "space_type": "VIEW_3D",
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
                        "operator": "object.eck_simpleoperator", #wm.call_menu_pie is a built in operator 
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
            # {
            #     "name": "UV Editor",
            #     "space_type": "EMPTY",
            #     "items":
            #     [
            #         {
            #             "operator": "wm.call_menu_pie",
            #             "type": "D",
            #             "value": "PRESS",
            #             "prop_name": "ECK_MT_Bevel_Menu",
            #             "shift": False,
            #             "ctrl": False,
            #             "alt": False,
            #             "oskey": False,
            #         },
            #     ]
            # },            
        ]



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
