from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarPasto():
    glColor3f(0.0,143.0,0.23)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.8,0.0)
    glVertex3f(1.0,-0.8,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()

def dibujarSol():
    glColor3f(1.0,1.0,0.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.6 , sin(angulo) * 0.2 + 0.4 ,0.0)
    glEnd()

def dibujarRayosDeSol():
    glColor3f(1.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(-0.35,0.4)
    glVertex2f(-0.32,0.4)
    glVertex2f(-0.6,0.18)
    glVertex2f(-0.6,0.15)
    
    glVertex2f(-0.85,0.4)
    glVertex2f(-0.82,0.4)
    glVertex2f(-0.6,0.65)
    glVertex2f(-0.6,0.63)

    glVertex2f(-0.85,0.18)
    glVertex2f(-0.32,0.65)
    
    glVertex2f(-0.32,0.18)
    glVertex2f(-0.85,0.65)
    glEnd()

def dibujarPared():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_QUADS)
    glVertex3f(-0.3,-0.8,0.0)
    glVertex3f(0.9,-0.8,0.0)
    glVertex3f(0.9,-0.2,0.0)
    glVertex3f(-0.3,-0.2,0.0)
    glEnd()

def dibujarVentana():
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_QUADS)
    glVertex3f(-0.2,-0.6,0.0)
    glVertex3f(0.5,-0.6,0.0)
    glVertex3f(0.5,-0.39,0.0)
    glVertex3f(-0.2,-0.39,0.0)
    glEnd()

def dibujarTecho():
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.4,-0.2,0.0)
    glVertex3f(0.3,0.3,0.0)
    glVertex3f(1,-0.2,0.0)
    glEnd()

def dibujarPuerta():
    glColor(0.8,0.5,0)
    glBegin(GL_QUADS)
    glVertex3f(0.6,-0.8,0.0)
    glVertex3f(0.8,-0.8,0.0)
    glVertex3f(0.8,-0.4,0.0)
    glVertex3f(0.6,-0.4,0.0)
    glEnd()

def dibujarManija():
    glColor3f(1.0,1.0,0.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.75 , sin(angulo) * 0.02 - 0.6 ,0.0)
    glEnd()

def dibujarTronco():
    glColor(0.8,0.5,0)
    glBegin(GL_QUADS)
    glVertex3f(-0.8,-0.8,0.0)
    glVertex3f(-0.6,-0.8,0.0)
    glVertex3f(-0.6,-0.5,0.0)
    glVertex3f(-0.8,-0.5,0.0)
    glEnd()

def dibujarHojas1():
    glColor3f(0.0,143.0,0.23)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.7 , sin(angulo) * 0.2 + -0.4 ,0.0)
    glEnd()

def dibujarHojas2():
    glColor3f(0.0,143.0,0.23)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.7 , sin(angulo) * 0.2 + -0.2 ,0.0)
    glEnd()

def dibujarHojas3():
    glColor3f(0.0,143.0,0.23)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.8 , sin(angulo) * 0.2 + -0.3 ,0.0)
    glEnd()

def dibujarHojas4():
    glColor3f(0.0,143.0,0.23)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.6 , sin(angulo) * 0.2 + -0.3 ,0.0)
    glEnd()

def dibujarNube1():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 + 0.5 , sin(angulo) * 0.1 + 0.8 ,0.0)
    glEnd()

def dibujarNube2():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 + 0.7 , sin(angulo) * 0.1 + 0.7 ,0.0)
    glEnd()

def dibujarNube3():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.2 + 0.1 , sin(angulo) * 0.1 + 0.7 ,0.0)
    glEnd()

def dibujar():
    #rutinas de dibujo
    dibujarPasto()
    dibujarRayosDeSol()
    dibujarSol()
    dibujarPared()
    dibujarVentana()
    dibujarTecho()
    dibujarPuerta()
    dibujarTronco()
    dibujarHojas1()
    dibujarHojas2()
    dibujarHojas3()
    dibujarHojas4()
    dibujarManija()
    dibujarNube1()
    dibujarNube2()
    dibujarNube3()

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(600,600,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,600,600)
        #Establece color de borrado
        glClearColor(0.4,0.8,0.1,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()