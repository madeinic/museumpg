from model import *

class Scene:
    def __init__ (self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
            self.objects.append(obj)
        
    def load(self):
            app = self.app
            add = self.add_object
            
            add(Cubo(app, scale=(10,1,1)))
            add(Cubo(app, tex_id=1, pos=(-3,0,0), rot=(45, 0, 30),scale=(1,10,10)))
        
    def render(self):
            for obj in self.objects:
                obj.render()