from model import *

class Scene:
    def __init__ (self, app):
        self.app = app
        self.objects = []
        self.load()
        #Skybox
        self.skybox = SkyBox(app)

    def add_object(self, obj):
            self.objects.append(obj)
        
    def load(self):
            app = self.app
            add = self.add_object
            
            n, s = 30, 2
            for x in range(-n, n, s):
                    for z in range(-n, n, s):
                            add(Cubo(app, pos=(x, -s, z)))
            add(Mono(app, pos=(0, -1, -10)))   
            add(Gato(app, pos=(-10, -1, -10)))
            add(Perro(app, pos=(10, -1, -10)))  
        
    def render(self):
            for obj in self.objects:
                obj.render()
            self.skybox.render()