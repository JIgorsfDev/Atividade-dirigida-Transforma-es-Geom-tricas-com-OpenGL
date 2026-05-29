#Três entidades geométricas coexistem no Espaço Gráfico. Cada uma possui uma essência distinta e reage de forma única à manipulação dimensional. Cabe a você, Guardião(ã), manter o equilíbrio. Cada objeto deve crescer, retrair ou expandir sua forma, mas somente quando você desejar. Use o clique do mouse ou comandos distintos para acionar a transformação de escala individualmente em cada objeto da seguinte forma:
#• Desenhe três objetos diferentes (podem ser 2D, 3D ou mistos)
#• Atribua a cada objeto uma tecla ou um clique de mouse (botões direita e esquerda) no objeto que ative transformações de escala (scaling):
#• ‘1' → aumenta ou diminui o tamanho do Objeto A
#• ‘2' → ativa o scaling do Objeto B
#• '3' → aplica o scaling no Objeto C
#• Ou, alternativamente, implemente detecção de clique do mouse sobre os objetos. Uso o botão direito / esquerdo para aumentar/diminuir
#• Use glScalef para aplicar a transformação de forma visual.
#ESCOLHIDO: a/A aumenta/diminui o tamanho do Objeto A, b/B do Objeto B, c/C do Objeto C

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

scaleA = 1.0
scaleB = 1.0
scaleC = 1.0

def keyboard(key, x, y):
   if key == b'a':
     scaleAPlus() 
   elif key == b'A':
     scaleAMinus()
   elif key == b'b':
     scaleBPlus()
   elif key == b'B':
     scaleBMinus()
   elif key == b'c':
     scaleCPlus()
   elif key == b'C':
     scaleCMinus()

def scaleAPlus():
   global scaleA
   scaleA *= 1.5
   glut.glutPostRedisplay()

def scaleAMinus():
   global scaleA
   scaleA *= 0.5
   glut.glutPostRedisplay()

def scaleBPlus():
   global scaleB
   scaleB *= 1.5
   glut.glutPostRedisplay()

def scaleBMinus():
   global scaleB
   scaleB *= 0.5
   glut.glutPostRedisplay()

def scaleCPlus():
   global scaleC
   scaleC *= 1.5
   glut.glutPostRedisplay()

def scaleCMinus():
   global scaleC
   scaleC *= 0.5
   glut.glutPostRedisplay()

def draw():
   gl.glClearColor(0.0, 0.0, 0.0, 0.0)
   gl.glClear(gl.GL_COLOR_BUFFER_BIT)

   gl.glColor3f(1.0, 1.0, 1.0)

   gl.glPushMatrix()
   gl.glTranslatef(-0.4, 0.0, 0.0)
   gl.glScalef(scaleA, scaleA, 1.0)

   gl.glBegin(gl.GL_TRIANGLES)
   gl.glVertex2f(-0.1, 0.1)
   gl.glVertex2f(0.1, 0.1)
   gl.glVertex2f(0.0, 0.4)
   gl.glEnd()

   gl.glPopMatrix()

   gl.glPushMatrix()
   gl.glTranslatef(0.0, 0.0, 0.0)
   gl.glScalef(scaleB, scaleB, 1.0)

   gl.glBegin(gl.GL_TRIANGLES)
   gl.glVertex2f(-0.1, 0.1)
   gl.glVertex2f(0.1, 0.1)
   gl.glVertex2f(0.1, 0.4)
   gl.glEnd()

   gl.glPopMatrix()

   gl.glPushMatrix()
   gl.glTranslatef(0.4, 0.0, 0.0)
   gl.glScalef(scaleC, scaleC, 1.0)

   gl.glBegin(gl.GL_TRIANGLES)
   gl.glVertex2f(-0.1, 0.1)
   gl.glVertex2f(0.1, 0.1)
   gl.glVertex2f(-0.1, 0.4)
   gl.glEnd()

   gl.glPopMatrix()

   gl.glFlush()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
glut.glutCreateWindow("A Harmonia dos Três Reinos")
glut.glutReshapeWindow(1000, 1000)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()
