import pygame as pg
import moderngl as mgl
import sys 
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene

class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        # inicializar modulo pygame
        pg.init()
        # Tamaño de ventana
        self.WIN_SIZE = win_size
        # establecer atributos de la version de opengl a usar
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # crear contexto para opengl
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        
        #configurar puntero del mouse para esconderlo y no limitar movimiento
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        
        #nombre de la ventana
        pg.display.set_caption('Museo de animales (preparación del entorno)')
        
        #quitar icono por defecto y personalizarlo
        icono = pg.image.load('./textures/peligro.png')
        pg.display.set_icon(icono)
        
        # detectar el contexto opengl
        self.ctx = mgl.create_context()
        #Activa Depth test para que se muestren las caras de manera correcta y cull face para que no se rendericen las caras interiores
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
       
        # crear objeto que haga seguimiento del tiempo
        self.clock = pg.time.Clock()
        self.time = 0
        #para que el movimiento de la camara sea independiente del frame rate
        self.delta_time = 0
        
        # LUZ, CAMARA, ACCIÓN!
        
        # Instanciacion de un objeto luz
        self.light = Light()
        
        # Instanciación de una camara
        self.camera = Camera(self)

        #Instanciación de mesh
        self.mesh = Mesh(self)
        
        # Creacion de la escena (elementos en pantalla)
        self.scene = Scene(self)

    # Funcion que detecta eventos y actua en consecuencia (como el presionado de teclas)
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # limpiar framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # renderizar escena
        self.scene.render()
        # intercambiar buffers
        pg.display.flip()
        
        
    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            #establecer framerate (fps)
            self.delta_time = self.clock.tick(60)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
