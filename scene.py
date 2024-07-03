from model import *
from sound_area import SoundArea


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.sound_areas = []
        self.load()
        # Skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)
    
    #Añadir area de sonido
    def add_sound_area(self, position, radius, sound_file, key):
        sound_area = SoundArea(position, radius, sound_file, key)
        sound_area.load_sound()
        self.sound_areas.append(sound_area)
        print(f'Sound Area Added: Position={position}, Radius={radius}, Sound File={sound_file}')  # Registro de depuración
        

    def load(self):
        app = self.app
        add = self.add_object

        #Areas de sonido
        
        self.add_sound_area((0, -1, -10), 10, 'sound/woof.mp3',pg.K_f)
        
            
        n, s = 30, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cubo(app, vao_name='cube', tex_id=1, pos=(x, -s, z)))
            
        add(Mono(app, vao_name='mono', tex_id='mono', pos=(0, -1, -10)))   
        #add(Gato(app, vao_name='gato', tex_id='gato', pos=(-10, -1, -10)))
        #add(Perro(app, vao_name='perro', tex_id='perro', pos=(10, -1, -10)))  
        add(Tapir(app, vao_name='tapir', tex_id='tapir', pos=(15, -1, -10)))
        add(Rana(app, vao_name='rana', tex_id='rana', pos=(5, -1, -10)))
        add(Tucan(app, vao_name='tucan', tex_id='tucan', pos=(15, -1, -5)))
        add(Anaconda(app, vao_name='anaconda', tex_id='anaconda', pos=(-5, -1, -10)))
        add(Loris(app, vao_name='loris', tex_id='loris', pos=(15, -1, 0)))
        add(Pato(app, vao_name='pato', tex_id='pato', pos=(9, -1, -5)))
        add(SeaDragon(app, vao_name='seadragon', tex_id='seadragon', pos=(13, -1, -5)))
        add(Armadillo(app, vao_name='armadillo', tex_id='armadillo', pos=(10, -1, -5)))
        add(CartelFinal(app, vao_name='CartelFinal', tex_id='CartelFinal', pos=(12, -1, -5)))


    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()
    
    def update_sounds(self, key_pressed):
        cam_pos = self.app.camera.position

        for sound_area in self.sound_areas:
            sound_area.check_and_play(cam_pos, key_pressed)
