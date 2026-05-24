import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def keyboard(key, x, y):
   if key == b'x':
      reflexaoX() 
   elif key == b'y':
      reflexaoY()

def reflexaoX():
  gl.glScalef(-1.0, 1.0, 1.0)
  glut.glutPostRedisplay()

def reflexaoY():
  gl.glScalef(1.0, -1.0, 1.0)
  glut.glutPostRedisplay()

def axes(x, y, text):
  gl.glRasterPos2f(x, y)

  for l in text:
    glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_18, ord(l))

  
def cartersian():
  gl.glColor3f(1, 1, 1)

  gl.glBegin(gl.GL_LINES)
  gl.glVertex2f(-1, 0)
  gl.glVertex2f(1, 0)
  gl.glVertex2f(0, -1)
  gl.glVertex2f(0, 1)
  gl.glEnd()

  axes(-0.95, 0.03, 'X') 
  axes(0.93, 0.03, 'X') 
  axes(0.03, -0.95, 'Y')
  axes(0.03, 0.93, 'Y')

def cam():
  gl.glMatrixMode(gl.GL_PROJECTION)
  gl.glLoadIdentity()
  glu.gluOrtho2D(-2.0, 2.0, -2.0, 2.0)

  gl.glMatrixMode(gl.GL_MODELVIEW)

def figure(): #Simbolo antigo, da ordem do caos
  gl.glBegin(gl.GL_TRIANGLES)
  gl.glColor3f(1.0, 0.0, 0.0)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(0.3, 0.7)
  gl.glVertex2f(0.0, 0.5)

  gl.glVertex2f(-0.3, 0.7)
  gl.glVertex2f(0.0, 0.5)
  gl.glVertex2f(0.0, 0.0)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(-0.7, 0.3)
  gl.glVertex2f(-0.5, 0.0)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(-0.5, 0.0)
  gl.glVertex2f(-0.7, -0.3)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(0.0, -0.5)
  gl.glVertex2f(0.3, -0.7)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(0.0, -0.5)
  gl.glVertex2f(-0.3, -0.7)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(0.7, 0.3)
  gl.glVertex2f(0.5, 0.0)

  gl.glVertex2f(0.0, 0.0)
  gl.glVertex2f(0.5, 0.0)
  gl.glVertex2f(0.7, -0.3)

  gl.glEnd()

  

def draw():
  gl.glClearColor(0.0, 0.0, 0.0, 1.0)
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)
  gl.glLoadIdentity()
  cartersian()
  gl.glTranslatef(0.8, 0.8, 0.0)
  figure()
  glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutCreateWindow("O Encontro das sombras")
cam()
glut.glutReshapeWindow(1000, 1000)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()
