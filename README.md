# OrbitalTransitions
Plotting 3D isosurfaces of hydrogenic orbital transitions during a Rabi cycle with Python, Blender, and ffmpeg

The procedure consists of three steps:

1) Making the .obj files (MakeOBJFiles.py)
2) Rendering the frames in Blender (BlenderScript.py)
3) Putting the frames together into a mp4 (ffmpeg)

The directory structure is as follows:

Project folder: $PHATH/ProjectName/

OBJ files: $PATH/ProjectName/OBJ

Rendered frames: $PATH/ProjectName/Render


Finally, I render the video using:

ffmpeg -r 30 -i %d.png -c:v libx264 -pix_fmt yuv420p d-d.mp4


Output:
https://imgur.com/a/6AJnjDT


