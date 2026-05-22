#No centro do plano dimensional repousa o Objeto Errante, um elemento que aguarda o comando do(a) Guardião(ã) para mover-se livremente pelo espaço bidimensional.
#Seu objetivo é conceder movimento ao objeto, aplicando translação por meio das teclas do teclado. Com isso, o objeto deixará de ser estático, assumindo sua primeira forma de liberdade: o deslocamento. Maaas, para isso, você deve realizar as seguintes ações:
#• Desenhe um objeto 2D qualquer (ex: triângulo, quadrado, estrela, símbolo místico)
#• Implemente translação com comandos do teclado, utilizando as funções de transformação da própria OpenGL (glTranslatef)
#• Utilize teclas específicas para cada direção:
#• 'w' → translação positiva no eixo Y
#• 's' → translação negativa no eixo Y
#• 'a' → translação negativa no eixo X
#• 'd' → translação positiva no eixo X

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def keyboard(key, x, y):
  if key == b'w':
     subir()
  elif key == b's':
     descer()
  elif key == b'a':
     esquerda()
  elif key == b'd':
     direita()

def subir():
  gl.glTranslatef(0.0, 0.1, 0.0)
  glut.glutPostRedisplay()

def descer():
  gl.glTranslatef(0.0, -0.1, 0.0)
  glut.glutPostRedisplay()

def esquerda():
  gl.glTranslatef(-0.1, 0.0, 0.0)
  glut.glutPostRedisplay()

def direita():
  gl.glTranslatef(0.1, 0.0, 0.0)

def draw():
  gl.glClearColor(0.0, 0.0, 0.0, 1.0)
  gl.glClear(gl.GL_COLOR_BUFFER_BIT)

  gl.glShadeModel(gl.GL_FLAT)
  gl.glBegin(gl.GL_QUADS)
  gl.glColor3f(1.0, 1.0, 1.0)
  gl.glVertex3f(0.1, 0.1, 0.0)
  gl.glVertex3f(-0.1, 0.1, 0.0)
  gl.glVertex3f(-0.1, -0.1, 0.0)
  gl.glVertex3f(0.1, -0.1, 0.0)
  gl.glEnd()
  gl.glFlush()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
glut.glutCreateWindow("O Despertar do objeto errante")
glut.glutReshapeWindow(1000, 1000)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()
