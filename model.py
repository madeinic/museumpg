import moderngl as mgl
import numpy as np
import glm
import pygame as pg

class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0,0,0), rot=(0,0,0), scale=(1,1,1)):
        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao_name = vao_name  
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera
        #delimitador
        self.bounding_box = self.calculate_bounding_box()
    
    #funcion para calcular delimtacion
    def calculate_bounding_box(self):
        # Obtén las dimensiones originales del modelo
        dimensions = self.get_model_dimensions()

        # Ajustar las dimensiones con la escala
        half_scale = glm.vec3(dimensions) * self.scale * 0.5
        adjustment_factor = 1.2  # Factor de ajuste para ampliar la caja delimitadora
        min_corner = self.pos - (half_scale * adjustment_factor)
        max_corner = self.pos + (half_scale * adjustment_factor)
        return (min_corner, max_corner)
    
    def get_model_dimensions(self):
        # Devuelve las dimensiones del modelo en su espacio de modelo, ajustando segun el tamaño del modelo en especifico
        if self.vao_name == 'columna':
            return glm.vec3(2, 50, 2)  # columna alta
        else:
            return glm.vec3(3, 3, 3)  # Tamaño base por defecto
   
    def get_model_matrix(self):
        m_model = glm.mat4()
        m_model = glm.translate(m_model, self.pos)
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(1, 0, 1))
        m_model = glm.scale(m_model, self.scale)
        return m_model
    
    def render(self):
        self.update()
        self.vao.render()

class ExtendedBaseModel(BaseModel):
    def __init__(self, app, vao_name, tex_id, pos, rot, scale):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()
    
    def update(self):
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def update_shadow(self):
        self.shadow_program['m_model'].write(self.m_model)

    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.render()
    
    def on_init(self):
        self.shadow_vao = self.app.mesh.vao.vaos['shadow_' + self.vao_name]
        self.shadow_program = self.shadow_vao.program
        self.shadow_program['m_proj'].write(self.camera.m_proj)
        self.shadow_program['m_view_light'].write(self.app.light.m_view_light)
        self.shadow_program['m_model'].write(self.m_model)
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

class Cubo(ExtendedBaseModel):
    def __init__(self, app, vao_name='cube', tex_id=1, pos=(0,0,0), rot=(0,0,0), scale=(1,1,1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

class Mono(ExtendedBaseModel):
    def __init__(self, app, vao_name='mono', tex_id='mono', pos=(0,0,0), rot=(-90,0,0), scale=(0.025,0.025,0.025)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

# class Gato(ExtendedBaseModel):
#     def __init__(self, app, vao_name='gato', tex_id='gato', pos=(0,0,0), rot=(-90,0,0), scale=(0.025,0.025,0.025)):
#         super().__init__(app, vao_name, tex_id, pos, rot, scale)
#         self.on_init()

# class Perro(ExtendedBaseModel):
#     def __init__(self, app, vao_name='perro', tex_id='perro', pos=(0,0,0), rot=(-90,0,0), scale=(0.07,0.07,0.07)):
#         super().__init__(app, vao_name, tex_id, pos, rot, scale)
#         self.on_init()

class Frame(ExtendedBaseModel):
    def __init__(self, app, vao_name='frame', tex_id='frame', pos=(90,90,90), rot=(0, -90, 0), scale=(1.0,1.0,1.0)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Frame2(ExtendedBaseModel):
    def __init__(self, app, vao_name='frame2', tex_id='frame2', pos=(90,34,90), rot=(0, 180, 0), scale=(1.0,1.0,1.0)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Frame3(ExtendedBaseModel):
    def __init__(self, app, vao_name='frame3', tex_id='frame3', pos=(90,34,90), rot=(0, 0, 0), scale=(1.0,1.0,1.0)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Trunk(ExtendedBaseModel):
    def __init__(self, app, vao_name='trunk', tex_id='trunk', pos=(0,0,0), rot=(-90,0,0), scale=(1.5,1.5,1.5)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Tapir(ExtendedBaseModel):
    def __init__(self, app, vao_name='tapir', tex_id='tapir', pos=(0,0,0), rot=(-50,-40,-80), scale=(0.05,0.05,0.05)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Rana(ExtendedBaseModel):
    def __init__(self, app, vao_name='rana', tex_id='rana', pos=(0,0,0), rot=(-90,0,0), scale=(0.1,0.1,0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Tucan(ExtendedBaseModel):
    def __init__(self, app, vao_name='tucan', tex_id='tucan', pos=(90,90,90), rot=(260, -90, 160), scale=(0.06,0.06, 0.06)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Dino1(ExtendedBaseModel):
    def __init__(self, app, vao_name='dino1', tex_id='dino1', pos=(90,90,90), rot=(-90,0,0), scale=(0.03,0.03, 0.03)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Dino2(ExtendedBaseModel):
    def __init__(self, app, vao_name='dino2', tex_id='dino2', pos=(90,90,90), rot=(-90,0,0), scale=(0.06,0.06, 0.06)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Grass(ExtendedBaseModel):
    def __init__(self, app, vao_name='grass', tex_id='grass', pos=(90,90,90), rot=(-90,0,0), scale=(0.01,0.01, 0.01)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()
class Anaconda(ExtendedBaseModel):
    def __init__(self, app, vao_name='anaconda', tex_id='anaconda', pos=(0,0,0), rot=(-90,-90,180), scale=(0.05,0.05,0.05)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Loris(ExtendedBaseModel):
    def __init__(self, app, vao_name='loris', tex_id='loris', pos=(0,0,0), rot=(-90,-90,180), scale=(0.03,0.03,0.03)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Armadillo(ExtendedBaseModel):
    def __init__(self, app, vao_name='armadillo', tex_id='armadillo', pos=(0,0,0), rot=(-90,270, -180), scale=(0.03,0.03,0.03)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Pato(ExtendedBaseModel):
    def __init__(self, app, vao_name='pato', tex_id='pato', pos=(0,0,0), rot=(-45,-40,-75), scale=(0.04,0.04,0.04)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class CartelFinal(ExtendedBaseModel):
    def __init__(self, app, vao_name='CartelFinal', tex_id='CartelFinal', pos=(0,0,0), rot=(-90,0,0), scale=(0.10,0.10,0.10)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class columna(ExtendedBaseModel):
    def __init__(self, app, vao_name='columna', tex_id='columna', pos=(0,0,0), rot=(-90,0,0), scale=(3,3,3)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()


class SeaDragon(ExtendedBaseModel):
    def __init__(self, app, vao_name='seadragon', tex_id='seadragon', pos=(0,0,0), rot=(-90,0,0), scale=(0.1,0.1,0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Dolphin(ExtendedBaseModel):
    def __init__(self, app, vao_name='dolphin', tex_id='dolphin', pos=(0,0,0), rot=(-90,0,0), scale=(0.03,0.03,0.03)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Camel(ExtendedBaseModel):
    def __init__(self, app, vao_name='camel', tex_id='camel', pos=(0,0,0), rot=(90,180,0), scale=(0.005,0.005,0.005)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Penguin(ExtendedBaseModel):
    def __init__(self, app, vao_name='penguin', tex_id='penguin', pos=(0,0,0), rot=(-90,0,0), scale=(0.03,0.03,0.03)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Quetzal(ExtendedBaseModel):
    def __init__(self, app, vao_name='quetzal', tex_id='quetzal', pos=(0,0,0), rot=(-90,0,0), scale=(0.05,0.05,0.05)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Turkey(ExtendedBaseModel):
    def __init__(self, app, vao_name='turkey', tex_id='turkey', pos=(0,0,0), rot=(-90,0,0), scale=(0.02,0.02,0.02)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class SeaHorse(ExtendedBaseModel):
    def __init__(self, app, vao_name='seahorse', tex_id='seahorse', pos=(0,0,0), rot=(-130,-40,80), scale=(0.1,0.1,0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Crab(ExtendedBaseModel):
    def __init__(self, app, vao_name='crab', tex_id='crab', pos=(0,0,0), rot=(-45,-40,-80), scale=(0.1,0.1,0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class PinkFish(ExtendedBaseModel):
    def __init__(self, app, vao_name='pinkfish', tex_id='pinkfish', pos=(0,0,0), rot=(-90,0,0), scale=(0.3,0.3,0.3)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Plataforma(ExtendedBaseModel):
    def __init__(self, app, vao_name='plataforma', tex_id='plataforma', pos=(0,0,0), rot=(-90,0,0), scale=(0.08,0.03,0.02)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Diver(ExtendedBaseModel):
    def __init__(self, app, vao_name='diver', tex_id='diver', pos=(0,0,0), rot=(130,150,70), scale=(0.3,0.3,0.3)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Coral(ExtendedBaseModel):
    def __init__(self, app, vao_name='coral', tex_id='coral', pos=(0,0,0), rot=(-90,0,0), scale=(0.03,0.03,0.03)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class AdvancedSkyBox(BaseModel):
    def __init__(self, app, vao_name='advanced_skybox', tex_id='skybox', pos=(0,0,0), rot=(0,0,0), scale=(1,1,1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        m_view = glm.mat4(glm.mat3(self.camera.m_view))
        self.program['m_invProjView'].write(glm.inverse(self.camera.m_proj * m_view))

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)
