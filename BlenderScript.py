# Open Blender, get into 'cycles render'
# Load one of the .obj files (preferably one of the largest objects)
# Setup the camera and scene manually
# Make a material and call it 'ElectronDensity', this will be the material of your objects
# Make sure that the OBJ and Render paths exist
# Open the text editor, load this script, and hit run.


import bpy


path = '$PATH/ProjectName/OBJ/'
renderpath='$PATH/ProjectName/Render/'

for i in range(0,250):
 bpy.ops.import_scene.obj(filepath=path+"%s.obj" % i) # Import OBJ
 D = bpy.data
 WF = bpy.context.selected_objects[0].name
 D.objects[WF].data.materials.append(D.materials['ElectronDensity']) # Assign material to object
 bpy.data.scenes['Scene'].render.filepath = renderpath+'%s.png' % (i) # Render image
 bpy.ops.render.render(write_still=True)
 bpy.ops.object.select_all(action='DESELECT')
 bpy.data.objects[WF].select = True
 bpy.ops.object.delete()   # Delete the object








#Created by Maximilian Paradiz
 
