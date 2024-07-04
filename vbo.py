import numpy as np
import moderngl as mgl
import pywavefront
import pywavefront.wavefront
#import pywavefront.wavefront


class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        #acceder a vbo del onjeto a traves de un diccionario
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['skybox'] = SkyBoxVBO(ctx)
        self.vbos['advanced_skybox'] = AdvancedSkyBoxVBO(ctx)
        self.vbos['mono'] = MonoVBO(ctx)
        self.vbos['gato'] = GatoVBO(ctx)
        self.vbos['perro'] = PerroVBO(ctx)
        self.vbos['tapir'] = TapirVBO(ctx)
        self.vbos['rana'] = RanaVBO(ctx)
        self.vbos['tucan'] = TucanVBO(ctx)
        self.vbos['anaconda'] = AnacondaVBO(ctx)
        self.vbos['loris'] = LorisVBO(ctx)
        self.vbos['pato'] = PatoVBO(ctx)
        self.vbos['CartelFinal'] = CartelFinalVBO(ctx)
        self.vbos['armadillo'] = ArmadilloVBO(ctx)
        self.vbos['seadragon'] = SeaDragonVBO(ctx)
        self.vbos['dolphin'] = DolphinVBO(ctx)
        self.vbos['columna'] = columnaVBO(ctx)
        self.vbos['camel'] = CamelVBO(ctx)
        self.vbos['penguin'] = PenguinVBO(ctx)
        self.vbos['quetzal'] = QuetzalVBO(ctx)
        self.vbos['turkey'] = TurkeyVBO(ctx)
        self.vbos['dino1'] = Dino1VBO(ctx)
        self.vbos['dino2'] = Dino2VBO(ctx)
        self.vbos['grass'] = grassVBO(ctx)
        self.vbos['seahorse'] = SeaHorseVBO(ctx)
        self.vbos['crab'] = CrabVBO(ctx)
        self.vbos['pinkfish'] = PinkFishVBO(ctx)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]


class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attribs: list = None

    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()
        
    def load_wavefront(self, path):
        objs = pywavefront.Wavefront(path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        return np.array(vertex_data, dtype='f4')

        
class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        #Formato de atributos de objeto
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
    #usar la libreria numpy para recopilar los vertices y caras del objeto en un solo arreglo
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), ( 1, -1,  1), (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), ( 1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, indices)

        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1),]
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        normals = [( 0, 0, 1) * 6,
                   ( 1, 0, 0) * 6,
                   ( 0, 0,-1) * 6,
                   (-1, 0, 0) * 6,
                   ( 0, 1, 0) * 6,
                   ( 0,-1, 0) * 6,]
        normals = np.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data


# Clase de skybox
class SkyBoxVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f'
        self.attribs = ['in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), ( 1, -1,  1), (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), ( 1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, indices)
        vertex_data = np.flip(vertex_data, 1).copy(order='C')
        return vertex_data

class AdvancedSkyBoxVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f'
        self.attribs = ['in_position']

    def get_vertex_data(self):
        # in clip space
        z = 0.9999
        vertices = [(-1, -1, z), (3, -1, z), (-1, 3, z)]
        vertex_data = np.array(vertices, dtype='f4')
        return vertex_data

class MonoVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/monkey/12958_Spider_Monkey_v1_l2.obj')
  
class ArmadilloVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/armadillo/10002_Armadillo_v1_L3.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class GatoVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/cat/12221_Cat_v1_l3.obj')
    
  
class PerroVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/dog/13463_Australian_Cattle_Dog_v3.obj')
    
class TapirVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/tapir/12277_Tapir_v1_L2.obj')
class RanaVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/Frog/12270_Frog_v1_L3.obj')
class columnaVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/columna/columna.obj')
    
class TucanVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/Tucan/12260_Bird_Toucan_v3_l2.obj')
class AnacondaVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/anaconda/13571_Anaconda_v1_L2.obj')

class LorisVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/loris/13569_Slender_Loris_v1_L3.obj')
    
class PatoVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/MandarinDuck/12253_Mandarin_Duck_v1_l3.obj')
    
class Dino1VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/Dino1/13623_Quetzalcoatlus_v1_L2.obj')

class Dino2VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/Dino2/13632_Chirostenotes_v1_L2.obj')
    
class grassVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/grass/10438_Circular_Grass_Patch_v1_iterations-2.obj')
class CartelFinalVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/CartelFinal/signospost_Model_10.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
class SeaDragonVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/seadragon/12267_seadragon_v1_L2.obj')

class DolphinVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/dolphin/10014_dolphin_v2_max2011_it2.obj')
    
class CamelVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/camel/Camel.obj')

class PenguinVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/penguin/10033_Penguin_v1_iterations-2.obj')
    
class QuetzalVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/quetzal/12245_Bird_v1_l2.obj')

class TurkeyVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/turkey/11560_wild_turkey_male_v2_l2.obj')  
        
class SeaHorseVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/seahorse/10044_SeaHorse_v1_iterations-2.obj')  
    
class CrabVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/Crab/10012_crab_v2_iterations-1.obj')  
    
class PinkFishVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']
        
    def get_vertex_data(self):
        return self.load_wavefront('objects/PinkFish/13014_Six_Line_Wrasse_v1_l3.obj')  