# This script will create 250 .obj files in the folder $PATH/ProjectName/OBJ

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from skimage import measure
 
x = np.linspace(-15,15,200)   # The grid size depends on the orbital you are plotting
X,Y,Z = np.meshgrid(x,x,x)    # Creates the 3D field of x,y,z values
R = np.sqrt(X**2+Y**2+Z**2)   # Associates each point of the grid with an R (spherical coordinate transformation)
theta = np.arccos(Z/R)        # Associates each point of the grid with a theta
phi = np.arctan2(Y,X)         # Associates each point with a phi. Important to use arctan2(Y,X) to cover the whole 2 pi range.

s = lambda r: 1/np.sqrt(np.pi)*np.exp(-r) # (n = 1, l = 0, m = 0) 
p0 = lambda r,theta: 1/(4*np.sqrt(2*np.pi))*r*np.exp(-r/2)*np.cos(theta) # (2,1,0) 
p1 = lambda r,theta,phi: 1/(8*np.sqrt(np.pi))*r*np.exp(-r/2)*np.sin(theta)*np.exp(1j*phi) # (2,1,1)
d0 = lambda phi,theta,r: 1/(81*np.sqrt(6*np.pi))*r**2*np.exp(-r/3)*(3*np.cos(theta)**2-1) # (3,2,0)
d1 = lambda phi,theta,r: 1/(81*np.sqrt(np.pi))*r**2*np.exp(-r/3)*np.sin(theta)*np.cos(theta)*np.exp(1j*phi) # (3,2,1)
d2 = lambda phi,theta,r: 1/(162*np.sqrt(np.pi))*r**2*np.exp(-r/3)*np.sin(theta)**2*np.exp(1j*2*phi) # (3,2,2)

Initial_State = d0(phi,theta,R) # The orbital that the mole
Final_State = d1(phi,theta,R)

#res0 = integrate.tplquad(lambda phi,theta,r: r**2*np.sin(theta)*abs(d1(phi,theta,r))**2,0,np.inf,lambda r: 0, lambda r: np.pi, lambda r,theta: 0, lambda r,theta: np.pi*2)
#print(res0[0])  # Whenever I add a new function, I use this to make sure that the wavefunction is normalized. Need to add 'import scipy.integrate as integrate'


# This next section generates the .obj file
N_frames = 250 # Number of frames
for t in range(0,N_frames):  

 # The following line calculates the squared of the wave function (|Psi|^2) for time t.
 # The wavefunction has the form a(t)|g> + b(t)|e>e^{-i omega t}
 # The coefficients are given by a(t) = cos(omega_r * t), b(t) = sin(omega_r * t)
 # In this case, I want the state to transition from ground to excited in 250 frames (pi/2 pulse lasting 250 frames), and the quantum beats to occur 10 times.
 Psi_squared = abs(np.cos(t*np.pi/(2*N_frames)) * Initial_State + np.sin(t*np.pi/(2*N_frames)) * Final_State * np.exp(-1j*t*2*np.pi/25))**2  

 # The isosurface is generated using the method of marching cubes. You need to have the Scikit-Image (skimage) module installed
 # Scikit-Image: https://scikit-image.org/
 verts, faces, normals, values = measure.marching_cubes_lewiner(Psi_squared, 0.0001) # The isosurface value of 0.0001 was selected for the d-orbitals. 0.001 works well for 1s/2p transition. I usually set N_frames to 1 and experiment with this until I like it.

 # This next part generates an obj file. The file contains the object name, followed by the vertices, normals, and faces.
 # Vertices are each the three coordinates of a vertex point
 # the faces tell you which three vertices connect to form a triangle
 # and the normals are the vectors normal to each of the faces

 o = open('OBJ/%s.obj' % t,'w')
 o.write('o Wavefunction\n')
 for i in verts:
  o.write('v %s %s %s \n' %(i[0],i[1],i[2]))
 for i in normals:
  o.write('vn %s %s %s \n' %(i[0],i[1],i[2]))
 for i in faces:
  o.write('f %s %s %s \n' %(i[0]+1,i[1]+1,i[2]+1))
 o.close()



# Created by Maximilian Paradiz
