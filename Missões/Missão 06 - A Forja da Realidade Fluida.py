#Guardião(ã), você mostrou que já dominou a forma, a rotação, o reflexo e o espaço. Mas agora, precisa ir além: distorcer a própria estrutura do mundo geométrico.
#Esta é a arte perdida do Cisalhamento, conhecida por poucos e dominada por ainda menos. Ela permite alterar a forma de um objeto sem mover seus vértices, como se dobrasse o espaço ao redor dele.
#Sua missão é invocar o Cubo Primordial e aplicar sobre ele uma força de cisalhamento em um dos eixos, como se o próprio tempo o tivesse o forjado na diagonal. Nesta missão, você deve:
#• Modelar um cubo 3D manualmente (sem GLUT), utilizando GL_QUADS ou GL_POLYGON
#• Aplicar a transformação de cisalhamento sobre o cubo
#• Dica do Dr. Forgilson: deforme o eixo X proporcional ao Y, alterando a matriz de cisalhamento ou modificando manualmente as coordenadas dos vértices
#• Exemplo de matriz de cisalhamento para uma transformação no eixo X proporcional a Y:
#• Implementar teclas para ativar o efeito de cisalhamento:
#• 'h' → aplicar o cisalhamento suavemente no eixo X
#• 'H' → desfazer o cisalhamento suavemente
#• 'z' → restaurar o cubo à forma original

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

cisalhamento = 0

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

vertices_originais = [v.copy() for v in vertices]

faces = [
  [0, 1, 2, 3],
  [4, 5, 6, 7],
  [3, 2, 6, 7],
  [0, 1, 5, 4],
  [1, 2, 6, 5],
  [0, 3, 7, 4]
             ]

def keyboard(key, x, y):
  global cisalhamento
  if key == b'h':
     shear()
     cisalhamento += 1
  elif key == b'H':
    if cisalhamento != 0:
     unshear()
     cisalhamento -= 1
  elif key == b'z':
     original_cube()
     cisalhamento = 0

def shear():
   novos_pontos = []

   for (px, py, pz) in vertices:

      x_att = px + 0.1 * py
      y_att = py
      z_att = pz

      novos_pontos.append([x_att, y_att, z_att])

   for i in range(len(vertices)):
      vertices[i] = novos_pontos[i]

   glut.glutPostRedisplay()

def unshear():
   novos_pontos = []

   for (px, py, pz) in vertices:

      x_att = px - 0.1 * py
      y_att = py
      z_att = pz

      novos_pontos.append([x_att, y_att, z_att])

   for i in range(len(vertices)):
      vertices[i] = novos_pontos[i]

   glut.glutPostRedisplay()

def original_cube():
  for i in range(len(vertices)):
    vertices[i] = vertices_originais[i].copy()

  glut.glutPostRedisplay()

def figure():
  gl.glColor3f(1.0, 1.0, 1.0)
  gl.glBegin(gl.GL_QUADS)

  for face in faces:
    for vertex in face:
      gl.glVertex3fv(vertices[vertex])

  gl.glEnd()

def cam():
   gl.glMatrixMode(gl.GL_PROJECTION)
   gl.glLoadIdentity()
   glu.gluPerspective(32, 1.0, 1.0, 20)
   gl.glMatrixMode(gl.GL_MODELVIEW)
   gl.glLoadIdentity()
   glu.gluLookAt(10.0, 0.0, 2.0,
                 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0)

   glut.glutPostRedisplay()

def draw():
   gl.glClearColor(0.0, 0.0, 0.0, 0.0)
   gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
   figure()
   glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutCreateWindow('A Forja da Realidade Fluida')
cam()
glut.glutReshapeWindow(1000, 1000)
gl.glEnable(gl.GL_DEPTH_TEST)
glut.glutDisplayFunc(draw)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()
