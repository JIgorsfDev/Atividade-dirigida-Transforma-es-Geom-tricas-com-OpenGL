#Guardião(ã), chegou o momento de fazer o mundo girar sob sua vontade. Na câmara central do Espaço Tridimensional repousa um artefato ancestral, um objeto GLUT. Mas ele só poderá revelar sua essência quando for 
#girado corretamente  ao redor dos três eixos que sustentam o universo gráfico. Seu desafio é comandar a rotação do objeto em torno dos eixos X, Y e Z, utilizando comandos do teclado
#para fazê-lo girar no sentido horário e anti-horário.
#Para isso, você deve:
#• Utilizar um objeto pronto da GLUT (ex: glutSolidTeapot, glutWireSphere, glutSolidCube etc.)
#• Implementar rotações nos três eixos (glRotatef), usando teclas distintas para sentido horário e anti- horário:
#• 'x' → rotação no sentido horário no eixo X
#• 'X' → rotação no sentido anti-horário no eixo X
#• 'y' / 'Y' → rotação no eixo Y
#• 'z' / 'Z' → rotação no eixo Z
#• Manter o objeto no centro da cena; altere apenas sua orientação, isto quer dizer que você NÃO deve mudar os valores dos vértices do objeto

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def keyboard(key, x, y):
   if key == b'x':
      rotacao_horariaX()
   elif key == b'X':
      rotacao_antihorariaX()
   elif key == b'y':
      rotacao_horariaY() 
   elif key ==  b'Y':
      rotacao_antihorariaY()
   elif key == b'z':
      rotacao_horariaZ()
   elif  key == b'Z':
      rotacao_antihorariaZ()

def rotacao_horariaX():
     gl.glRotatef(10, 1, 0, 0)
     glut.glutPostRedisplay()

def rotacao_antihorariaX():
   gl.glRotatef(-10, 1, 0, 0)
   glut.glutPostRedisplay()

def rotacao_horariaY():
   gl.glRotatef(10, 0, 1, 0)
   glut.glutPostRedisplay()

def rotacao_antihorariaY():
   gl.glRotatef(-10, 0, 1, 0)
   glut.glutPostRedisplay()

def rotacao_horariaZ():
   gl.glRotatef(10, 0, 0, 1)
   glut.glutPostRedisplay()

def rotacao_antihorariaZ():
   gl.glRotatef(-10, 0, 0, 1)
   glut.glutPostRedisplay()

def draw():
   gl.glClearColor(0, 0, 0, 0)
   gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
   gl.glColor3f(1, 1, 1)
   glut.glutWireCube(0.5)
   glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutCreateWindow("Os eixos da eternidade")
gl.glEnable(gl.GL_DEPTH_TEST)
glut.glutReshapeWindow(1000, 1000)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()

   
 
