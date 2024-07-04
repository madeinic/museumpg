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
        
    # (dimension = 2; entonces sera una losa de dimension 2x2)
    def generarLosa(self, dimensiones, posicion_centro, textura):
        app = self.app
        add = self.add_object
        n, s = dimensiones, 2
        cx, cy, cz = posicion_centro
        for x in range(cx - n, cx + n, s):
            for z in range(cz - n, cz + n, s):
                add(Cubo(app, vao_name='cube', tex_id=textura, pos=(x, cy, z)))
    
    
    def generarPared(self, dimension, posicion, orientacion, textura):
        app = self.app
        add = self.add_object
        n, s = dimension, 2
        cx, cy, cz = posicion

        if orientacion == 'frontal':
            for x in range(cx, cx + n * s, s):
                for y in range(cy, cy + n * s, s):
                    add(Cubo(app, vao_name='cube', tex_id=textura, pos=(x, y, cz)))
                    
        elif orientacion == 'lateral':
            for z in range(cz, cz + n * s, s):
                for y in range(cy, cy + n * s, s):
                    add(Cubo(app, vao_name='cube', tex_id=textura, pos=(cx, y, z)))

    
        
    def load(self):
        app = self.app
        add = self.add_object
        generarLosa = self.generarLosa
        generarPared = self.generarPared
        #Areas de sonido
        
        self.add_sound_area((0, -1, -10), 10, 'sound/woof.mp3',pg.K_f)
        
        # Generar el suelo exterior
        generarLosa(30, (0, -2, 0),2)
        generarLosa(30,(0,-2, -60),3)
        #techo
        generarLosa(30,(0,19, -60),4)
        # Generar las paredes de la estructura de exhibición
        
        # Paredes frontales
        #mas cercanas 
        generarPared(15, (-34, -9, -30), 'frontal', 1)
        generarPared(15, (4, -9, -30), 'frontal', 1)
        #mas alejadas
        generarPared(15, (-30, -9, -90), 'frontal', 1)
        generarPared(15, (0, -9, -90), 'frontal', 1)

        # Paredes laterales
        generarPared(15, (-30, -9, -60), 'lateral', 1)
        generarPared(15, (-30, -9, -90), 'lateral', 1)
        generarPared(15, (30, -9, -90), 'lateral', 1)
        generarPared(15, (30, -9, -60), 'lateral', 1)
            
        '''n, s = 30, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cubo(app, vao_name='cube', tex_id=2, pos=(x, -s, z)))'''
            
        add(Mono(app, vao_name='mono', tex_id='mono', pos=(0, -1, -10)))   
        #add(Gato(app, vao_name='gato', tex_id='gato', pos=(-10, -1, -10)))
        #add(Perro(app, vao_name='perro', tex_id='perro', pos=(10, -1, -10)))  
        add(Tapir(app, vao_name='tapir', tex_id='tapir', pos=(-20, -1, -70))) #original -15,-1,-70
        add(Rana(app, vao_name='rana', tex_id='rana', pos=(-15, -1, -67)))
        add(Tucan(app, vao_name='tucan', tex_id='tucan', pos=(-10, 2, -80)))
        add(Anaconda(app, vao_name='anaconda', tex_id='anaconda', pos=(-15, -1, -76)))
        add(Loris(app, vao_name='loris', tex_id='loris', pos=(-15, -1, -70)))
        add(Pato(app, vao_name='pato', tex_id='pato', pos=(-5, -1, -80)))
        add(SeaDragon(app, vao_name='seadragon', tex_id='seadragon', pos=(13, -1, -5)))
        add(Armadillo(app, vao_name='armadillo', tex_id='armadillo', pos=(-20, -1, -75))) 
        add(CartelFinal(app, vao_name='CartelFinal', tex_id='CartelFinal', pos=(12, -1, -5)))
        add(Dolphin(app, vao_name='dolphin', tex_id='dolphin', pos=(25, -1, -75)))
        add(Camel(app, vao_name='camel', tex_id='camel', pos=(-20, -1, -66)))
        add(Penguin(app, vao_name='penguin', tex_id='penguin', pos=(25, -1, -80)))
        add(Quetzal(app, vao_name='quetzal', tex_id='quetzal', pos=(0, 1, -80)))
        add(Turkey(app, vao_name='turkey', tex_id='turkey', pos=(5, -1, -80)))
        add(Dino1(app, vao_name='dino1', tex_id='dino1', pos=(0, 6, -75)))
        add(Dino2(app, vao_name='dino2', tex_id='dino2', pos=(-1, -1, -60)))
        add(Grass(app, vao_name='grass', tex_id='grass', pos=(-1, -1, -60)))
        add(SeaHorse(app, vao_name='seahorse', tex_id='seahorse', pos=(20, -1, -75)))
        add(Crab(app, vao_name='crab', tex_id='crab', pos=(20, -1, -70)))
        add(PinkFish(app, vao_name='pinkfish', tex_id='pinkfish', pos=(20, -1, -73)))
        add(Diver(app, vao_name='diver', tex_id='diver', pos=(25, -1, -65)))
        add(Coral(app, vao_name='coral', tex_id='coral', pos=(22, -1, -66)))
        
        add(columna(app, vao_name='columna', tex_id='columna', pos=(18, -18, -83)))
        add(columna(app, vao_name='columna', tex_id='columna', pos=(-20, -18, -83)))
        add(columna(app, vao_name='columna', tex_id='columna', pos=(18, -18, -60)))
        add(columna(app, vao_name='columna', tex_id='columna', pos=(-20, -18, -60)))
        add(columna(app, vao_name='columna', tex_id='columna', pos=(18, -18, -35)))
        add(columna(app, vao_name='columna', tex_id='columna', pos=(-20, -18, -35)))

    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()
    
    def update_sounds(self, key_pressed):
        cam_pos = self.app.camera.position

        for sound_area in self.sound_areas:
            sound_area.check_and_play(cam_pos, key_pressed)
