import pygame as pg
import moderngl as mgl
import glm


class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/peligro.png')
        self.textures[1] = self.get_texture(path='textures/marmol.jpg')
        self.textures[2] = self.get_texture(path='textures/cesped.jpeg')
        self.textures[3] = self.get_texture(path='textures/floor.png')
        self.textures[4] = self.get_texture(path='textures/Techo.png')
        self.textures['arena'] = self.get_texture(path='textures/arena.jpeg')
        self.textures['tierra'] = self.get_texture(path='textures/tierra.jpg')
        # Textura de la skybox
        self.textures['skybox'] = self.get_texture_cube(dir_path='textures/skybox/', ext='png')
        #texturas de modelos
        self.textures['mono'] = self.get_texture(path='objects/monkey/12958_Spider_Monkey_diff.jpg')
        #self.textures['gato'] = self.get_texture(path='objects/cat/cat_diffuse.jpg') 
        #self.textures['perro'] = self.get_texture(path='objects/dog/Australian_Cattle_Dog_dif.jpg')  
        self.textures['depth_texture'] = self.get_depth_texture()
        self.textures['tapir'] = self.get_texture(path='objects/tapir/tapir_diffuse.jpg')
        self.textures['rana'] = self.get_texture(path='objects/Frog/frog_diff.jpg')
        self.textures['tucan'] = self.get_texture(path='objects/Tucan/12260_Bird_Toucan_Diffuse.jpg')
        self.textures['anaconda'] = self.get_texture(path='objects/anaconda/Anaconda_diff.jpg')
        self.textures['loris'] = self.get_texture(path='objects/loris/13569_Slender_Loris_diffuse.jpg')
        self.textures['armadillo'] = self.get_texture(path='objects/armadillo/10002_Armadillo_v1_Diffuse.jpg')
        self.textures['pato'] = self.get_texture(path='objects/MandarinDuck/12253_Mandarin_Duck_diff.jpg')
        self.textures['seadragon'] = self.get_texture(path='objects/seadragon/12267_seadragon_diffuse.jpg')
        self.textures['CartelFinal'] = self.get_texture(path='objects/CartelFinal/signospost_Model_10_u1_v1_diffuse.jpeg')
        self.textures['dolphin'] = self.get_texture(path='objects/dolphin/10014_dolphin_v1_Diffuse.jpg')
        self.textures['columna'] = self.get_texture(path='objects/columna/columna.jpg')
        self.textures['camel'] = self.get_texture(path='objects/camel/10007_Camel_v03.jpg')
        self.textures['penguin'] = self.get_texture(path='objects/penguin/10033_Penguin_v1_Diffuse.jpg')
        self.textures['quetzal'] = self.get_texture(path='objects/quetzal/12245_Bird_diffuse.jpg')
        self.textures['turkey'] = self.get_texture(path='objects/turkey/wild_turkey_male_diffuse_v2.jpg')
        self.textures['dino1'] = self.get_texture(path='objects/dino1/13623_Quetzalcoatlus.jpg')
        self.textures['dino2'] = self.get_texture(path='objects/dino2/Chirostenotes_diffuse.jpg')        
        self.textures['grass'] = self.get_texture(path='objects/grass/10438_Circular_Grass_Patch_v1_Diffuse.jpg')
        self.textures['seahorse'] = self.get_texture(path='objects/seahorse/10044_SeaHorse_v1_Diffuse.jpg')
        self.textures['crab'] = self.get_texture(path='objects/Crab/10012_crab_v1_Diffuse.jpg')
        self.textures['pinkfish'] = self.get_texture(path='objects/PinkFish/13014_Six_Line_Wrasse_v1_diff.jpg')
        self.textures['diver'] = self.get_texture(path='objects/Diver/13018_Aquarium_Deep_Sea_Diver_diff.jpg')
        self.textures['coral'] = self.get_texture(path='objects/coral/10010_Coral_v1_Diffuse.jpg')
        self.textures['trunk'] = self.get_texture(path='objects/Trunk/trunk wood_final_map.jpg')
        self.textures['plataforma'] = self.get_texture(path='objects/base/10450_Rectangular_Grass_Patch_v1_Diffuse.jpg')
        self.textures['frame'] = self.get_texture(path='objects/frame/mountain.jpg')
        self.textures['frame2'] = self.get_texture(path='objects/frame/sea.jpg')
        self.textures['frame3'] = self.get_texture(path='objects/frame/bosque.jpg')

    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)
        return depth_texture
    
    def get_texture_cube(self, dir_path, ext='png'):
        faces = ['right', 'left', 'top', 'bottom'] +  ['front', 'back'][::-1]
        #textures = [pg.image.load(dir_path + f'{face}.{ext}').convert() for face in faces]
        textures = []
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)
        
        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)
        
        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)
        
        return texture_cube
        
    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]