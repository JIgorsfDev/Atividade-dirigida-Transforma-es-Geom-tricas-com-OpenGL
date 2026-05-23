import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

vertices = [
  [1, -1, -1],
  [1, 1, -1],
  [-1, 1, -1],
  [-1, -1, -1],
  [1, -1, 1],
  [1, 1, 1],
  [-1, 1, 1],
  [-1, -1, 1]
           ]

faces = [
  [0, 1, 2, 3],
  [4, 5, 6, 7],
  [3, 2, 6, 7],
  [0, 1, 5, 4],
  [1, 2, 6, 5],
  [0, 3, 7, 4]
             ]

def keyboard(key, x, y):
   if key == b'h':
     shear()
   elif key == b'H':
     unshear()
   elif key == b'z':
     original_cube()

def shear():
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   gl.glTranslatef(0.0, 0.0, -5.0)
   gl.glScalef(1.0, 1.0, 1.0)

def unshear():
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   gl.glTranslatef(0.0, 0.0, -5.0)
   gl.glScalef(1.0, 1.0, 1.0)

def original_cube():
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   gl.glTranslatef(0.0, 0.0, -5.0)

def figure():
  gl.glBegin(gl.GL_QUADS)

  for i in range(len(faces)):
      gl.glColor3fv(1.0, 1.0, 1.0)

  for vertex in faces[i]:
      gl.glVertex3fv(vertices[vertex])

  gl.glEnd()

def draw():
  
