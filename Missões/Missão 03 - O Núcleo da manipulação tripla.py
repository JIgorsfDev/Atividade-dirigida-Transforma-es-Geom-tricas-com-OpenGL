#Está na hora de abandonar os atalhos e moldar o espaço com suas próprias mãos, Guardião(ã). Em seu laboratório de modelagem, você deverá criar um objeto tridimensional único, sem o auxílio dos
#artefatos prontos da GLUT. Mas apenas construí-lo não basta, você deve ser capaz de manipulá-lo com maestria em todos os três eixos, aplicando transformações geométricas compostas.
#Mostre tudo que você é capaz de fazer seguindo os passos abaixo:
#• Modele manualmente um objeto 3D (ex: pirâmide, prisma, robô minimalista, estrutura composta de cubos ou polígonos)
#• Aplique duas transformações geométricas (positivas e negativas) para cada eixo (X, Y e Z), por exemplo:
#• Translação no eixo X com 't' / 'T'
#• Rotação no eixo Y com 'y' / 'Y'
#• Escala no eixo Z com 'e' / 'E'
#• As transformações devem ser realizadas combinando funções como glTranslatef, glRotatef, glScalef.

import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

apice = [0.0, 0.0, 1.0]

triangles = [
  apice,
  [0.0, -0.5, 0.0],
  [0.5, -0.15, 0.0],

  apice,
  [0.5, -0.15, 0.0],
  [0.3, 0.5, 0.0],

  apice,
  [0.3, 0.5, 0.0],
  [-0.3, 0.5, 0.0],

  apice,
  [-0.3, 0.5, 0.0],
  [-0.5, -0.15, 0.0],

  apice,
  [-0.5, -0.15, 0.0],
  [0.0, -0.5, 0.0],
]

base = [
  [0.0, -0.5, 0.0],
  [0.5, -0.15, 0.0],
  [0.3, 0.5, 0.0],
  [-0.3, 0.5, 0.0],
  [-0.5, -0.15, 0.0],
]

def keyboard(key, x, y): #decidi fazer as três transformações propostas pela questão, já fiz rotação e translação antes, então, queria fazer a escala também e juntar tudo 
  if key == b't':
     translacao_horariaX()
  elif key == b'T':
     translacao_antihorariaX()
  elif key == b'r':
     rotacao_horariaY()
  elif key == b'R':
     rotacao_antihorariaY()
  elif key == b'e':
      escala_positivaZ()
  elif  key == b'E':
      escala_negativaZ()

def translacao_horariaX():
     gl.glTranslatef(0.1, 0.0, 0.0)
     glut.glutPostRedisplay()

def translacao_antihorariaX():
     gl.glTranslatef(-0.1, 0.0, 0.0)
     glut.glutPostRedisplay()

def rotacao_horariaY():
     gl.glRotatef(10, 0.0, 1.0, 0.0)
     glut.glutPostRedisplay()

def rotacao_antihorariaY():
     gl.glRotatef(-10, 0.0, 1.0, 0.0)
     glut.glutPostRedisplay()

def escala_positivaZ():
     gl.glScalef(1.0, 1.0, 1.5)
     glut.glutPostRedisplay()

def escala_negativaZ():
     gl.glScalef(1.0, 1.0, 0.5)
     glut.glutPostRedisplay()

def cam_init():
  gl.glMatrixMode(gl.GL_PROJECTION)
  gl.glLoadIdentity()
  glu.gluPerspective(32, 1.0, 1.0, 20)
  gl.glMatrixMode(gl.GL_MODELVIEW)
  gl.glLoadIdentity()
  glu.gluLookAt(8.0, 0.0, 2.0,
                0.0, 0.0, 1.0,
                0.0, 0.0, 1.0
  )

  glut.glutPostRedisplay()

def figure():
   gl.glColor3f(1.0, 1.0, 1.0)
   gl.glBegin(gl.GL_TRIANGLES)

   for triangle in triangles:
       gl.glVertex3fv(triangle)

   gl.glEnd()

   gl.glColor3f(1.0, 1.0, 1.0)
   gl.glBegin(gl.GL_POLYGON)

   for vertex in base:
       gl.glVertex3fv(vertex)

   gl.glEnd()

   gl.glColor3f(0.0, 0.0, 0.0)
   gl.glBegin(gl.GL_LINES)

   for triangle in triangles:
       gl.glVertex3fv(apice)
       gl.glVertex3fv(triangle)

   gl.glEnd()

def draw():
 gl.glClearColor(0.0, 0.0, 0.0, 0.0)
 gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
 figure()
 glut.glutSwapBuffers()


  
glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutCreateWindow('O Núcleo da manipulação tripla')
cam_init()
glut.glutReshapeWindow(500, 500)
glut.glutKeyboardFunc(keyboard)
gl.glEnable(gl.GL_DEPTH_TEST)
glut.glutDisplayFunc(draw)
glut.glutMainLoop()
  
