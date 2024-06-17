from model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # Skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)
        
    def load(self):
        app = self.app
        add = self.add_object
            
        n, s = 30, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cubo(app, vao_name='cube', tex_id=1, pos=(x, -s, z)))
            
        add(Mono(app, vao_name='mono', tex_id='mono', pos=(0, -1, -10)))   
        add(Gato(app, vao_name='gato', tex_id='gato', pos=(-10, -1, -10)))
        add(Perro(app, vao_name='perro', tex_id='perro', pos=(10, -1, -10)))  
        add(Tapir(app, vao_name='tapir', tex_id='tapir', pos=(15, -1, -10)))
        add(Rana(app, vao_name='rana', tex_id='rana', pos=(5, -1, -10)))
        add(Tucan(app, vao_name='tucan', tex_id='tucan', pos=(15, -1, -5)))
        add(Anaconda(app, vao_name='anaconda', tex_id='anaconda', pos=(-5, -1, -10)))
        add(Loris(app, vao_name='loris', tex_id='loris', pos=(15, -1, 0)))
        add(Pato(app, vao_name='pato', tex_id='pato', pos=(9, -1, -5)))
        add(SeaDragon(app, vao_name='seadragon', tex_id='seadragon', pos=(13, -1, -5)))


    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()
