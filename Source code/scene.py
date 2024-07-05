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

   
    def plataforma(self, position, orientation, texture):
        app = self 
        add = self.add_object
        
        px,py,pz = position
        
        if orientation == "lateral":
            add(Cubo(app, vao_name='cube', tex_id=texture, pos=(px, py, pz), scale=(1,0.5,11)))
    
        if orientation == "frontal":
            add(Cubo(app, vao_name='cube', tex_id=texture, pos=(px, py, pz), scale=(11,0.5,1)))
            
    def load(self):
        app = self.app
        add = self.add_object
        generarLosa = self.generarLosa
        generarPared = self.generarPared
        #plataforma = self.plataforma
        #Areas de sonido
        #Aves
        self.add_sound_area((-10, -1, -80), 5, 'sound/Tucan.mp3',pg.K_f)
        self.add_sound_area((-5, -1.09, -80), 5, 'sound/pato_mandarin.mp3',pg.K_f)
        self.add_sound_area((0, 1, -80), 5, 'sound/Quetzal.mp3',pg.K_f)
        self.add_sound_area((5, -1.09, -80), 5, 'sound/Pavo.mp3',pg.K_f)

        #Acuatico
        self.add_sound_area((25, 0, -65), 4, 'sound/Delfin.mp3',pg.K_f)
        self.add_sound_area((25, 0, -75), 4, 'sound/Penguin.mp3',pg.K_f)
        self.add_sound_area((20, 0, -70), 4, 'sound/caballo_mar.mp3',pg.K_f)
        self.add_sound_area((20, 0, -55), 4, 'sound/Cangrejo.mp3',pg.K_f)
        self.add_sound_area((20, 0, -63), 4, 'sound/Burbuja.mp3',pg.K_f)

        #Terrestre
        self.add_sound_area((-20, -1, -65), 4, 'sound/Tapir.mp3',pg.K_f)
        self.add_sound_area((-20, -0.8, -55), 4, 'sound/Camello.mp3',pg.K_f)
        self.add_sound_area((-20, -0.9, -75), 4, 'sound/Armadillo.mp3',pg.K_f)
        self.add_sound_area((-15, 0, -57), 4, 'sound/Rana.mp3',pg.K_f)
        self.add_sound_area((-15, -1, -63), 4, 'sound/Loris.mp3',pg.K_f)
        self.add_sound_area((-15, -1, -70), 4, 'sound/Anaconda.mp3',pg.K_f)
     
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
            
        #add(Mono(app, vao_name='mono', tex_id='mono', pos=(0, -1, -10)))   
        #add(Gato(app, vao_name='gato', tex_id='gato', pos=(-10, -1, -10)))
        #add(Perro(app, vao_name='perro', tex_id='perro', pos=(10, -1, -10)))  
        
        #Seccion de terrestres
        
        #camello tapir armadello
        #plataforma((-20,-1,-59),'lateral','tierra')
        add(Tapir(app, vao_name='tapir', tex_id='tapir', pos=(-20, -1, -65))) #original -15,-1,-70
        add(Camel(app, vao_name='camel', tex_id='camel', pos=(-20, -0.8, -55)))
        add(Armadillo(app, vao_name='armadillo', tex_id='armadillo', pos=(-20, -0.9, -75))) 
        #rana lemur serpiente
        #plataforma((-15,-1,-59),"lateral",'tierra')
        add(Plataforma(app, vao_name='plataforma', tex_id='tierra', pos=(-20, -1, -57-15)))
        add(Plataforma(app, vao_name='plataforma', tex_id='tierra', pos=(-20, -1, -53-15)))
        add(Plataforma(app, vao_name='plataforma', tex_id='tierra', pos=(-20, -1, -49-15)))
        add(Plataforma(app, vao_name='plataforma', tex_id='tierra', pos=(-20, -1, -45-15)))
        add(Plataforma(app, vao_name='plataforma', tex_id='tierra', pos=(-20, -1, -40-15)))
        add(Rana(app, vao_name='rana', tex_id='rana', pos=(-15, 0, -57)))
        add(Loris(app, vao_name='loris', tex_id='loris', pos=(-15, -1, -63)))
        add(Anaconda(app, vao_name='anaconda', tex_id='anaconda', pos=(-15, -1, -70)))
        add(Frame3(app, vao_name='frame3', tex_id='frame3', pos=(-25, -1, -65)))
        
        #Seccion de aves
        add(Tucan(app, vao_name='tucan', tex_id='tucan', pos=(-10, 1.5, -80)))
        add(Pato(app, vao_name='pato', tex_id='pato', pos=(-5, 1.5, -80)))
        add(Quetzal(app, vao_name='quetzal', tex_id='quetzal', pos=(0, 1.5, -80)))
        add(Turkey(app, vao_name='turkey', tex_id='turkey', pos=(5, 1.5, -80)))
        add(Plataforma(app, vao_name='plataforma', tex_id='plataforma', pos=(0, -1, -83)))
        add(Frame(app, vao_name='frame', tex_id='frame', pos=(0, 1, -86)))

        #Troncos
        add(Trunk(app, vao_name='trunk', tex_id='trunk', pos=(-10.4, 0, -80)))
        add(Trunk(app, vao_name='trunk', tex_id='trunk', pos=(-5, 0, -80)))
        add(Trunk(app, vao_name='trunk', tex_id='trunk', pos=(0, 0, -80)))
        add(Trunk(app, vao_name='trunk', tex_id='trunk', pos=(5, 0, -80)))


        add(Dino1(app, vao_name='dino1', tex_id='dino1', pos=(0, 6, -75)))


        #Seccion de acuaticos
        add(Plataforma(app, vao_name='plataforma', tex_id='arena', pos=(27, -1, -57-15)))
        add(Plataforma(app, vao_name='plataforma', tex_id='arena', pos=(27, -1, -53-15)))
        add(Plataforma(app, vao_name='plataforma', tex_id='arena', pos=(27, -1, -49-15)))
        add(Plataforma(app, vao_name='plataforma', tex_id='arena', pos=(27, -1, -45-15)))
        add(Plataforma(app, vao_name='plataforma', tex_id='arena', pos=(27, -1, -40-15)))
        add(SeaDragon(app, vao_name='seadragon', tex_id='seadragon', pos=(13,200.8, -5)))
        add(Dolphin(app, vao_name='dolphin', tex_id='dolphin', pos=(25, -1, -65)))
        add(Penguin(app, vao_name='penguin', tex_id='penguin', pos=(25, -1, -75)))
        add(SeaHorse(app, vao_name='seahorse', tex_id='seahorse', pos=(20, -1, -70)))
        add(Crab(app, vao_name='crab', tex_id='crab', pos=(20, -1, -55)))
        add(PinkFish(app, vao_name='pinkfish', tex_id='pinkfish', pos=(20, -1, -63)))
        add(Diver(app, vao_name='diver', tex_id='diver', pos=(25, -1, -55)))
        add(Coral(app, vao_name='coral', tex_id='coral', pos=(23, -1, -60)))
        add(Frame2(app, vao_name='frame2', tex_id='frame2', pos=(28, 1, -63)))
        
        #Seccion de en medio 
        add(Grass(app, vao_name='grass', tex_id='grass', pos=(-1, -1, -60)))
        add(Dino2(app, vao_name='dino2', tex_id='dino2', pos=(-1, -1, -60)))

        add(CartelFinal(app, vao_name='CartelFinal', tex_id='CartelFinal', pos=(12, -1, -5)))
        
        #Columnas
        add(columna(app, vao_name='columna', tex_id='columna', pos=(18, -18, -83)))
        add(columna(app, vao_name='columna', tex_id='columna', pos=(-20, -18, -83)))
        add(columna(app, vao_name='columna', tex_id='columna', pos=(18, -18, -45)))
        add(columna(app, vao_name='columna', tex_id='columna', pos=(-20, -18, -45)))

        #plataformas


    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()
    
    def update_sounds(self, key_pressed):
        cam_pos = self.app.camera.position

        for sound_area in self.sound_areas:
            sound_area.check_and_play(cam_pos, key_pressed)
