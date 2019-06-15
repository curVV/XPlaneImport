bl_info = {
    "name": "Import X-Plane OBJ",
    "author": "Dave Prue <dave.prue@lahar.net>",
    "version": (1,0,1),
    "blender": (2,80,0),
    "api": 36273,
    "location": "File > Import/Export > XPlane",
    "description": "Import X-Plane obj files",
    "warning": "",
    "wiki_url": "https://github.com/curvian/XPlaneImport/wiki",
    "tracker_url": "https://github.com/curvian/XPlaneImport/issues",
    "support": "COMMUNITY",
    "category": "Import-Export"
}


import bpy

from . xpi_import import XPI_OT_import


classes = (XPI_OT_import,)

def menu_func(self, context):
    self.layout.operator(XPI_OT_import.bl_idname, text="XPlane Object (.obj)")
    
def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls) 
    bpy.types.TOPBAR_MT_file_import.append(menu_func)
    
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls) 
    bpy.types.TOPBAR_MT_file_import.remove(menu_func)



if __name__ == "__main__":
    register()
