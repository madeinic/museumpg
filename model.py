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
        size = 1.0  # Tamaño base
        min_corner = self.pos - glm.vec3(size * 1.5)
        max_corner = self.pos + glm.vec3(size * 1.5)
        return (min_corner, max_corner)
    
   
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

class Tapir(ExtendedBaseModel):
    def __init__(self, app, vao_name='tapir', tex_id='tapir', pos=(0,0,0), rot=(-90,0,0), scale=(0.05,0.05,0.05)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Rana(ExtendedBaseModel):
    def __init__(self, app, vao_name='rana', tex_id='rana', pos=(0,0,0), rot=(-90,0,0), scale=(0.1,0.1,0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Tucan(ExtendedBaseModel):
    def __init__(self, app, vao_name='tucan', tex_id='tucan', pos=(0,0,0), rot=(-90,0,0), scale=(0.04,0.04,0.04)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Anaconda(ExtendedBaseModel):
    def __init__(self, app, vao_name='anaconda', tex_id='anaconda', pos=(0,0,0), rot=(-90,0,0), scale=(0.03,0.03,0.03)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Loris(ExtendedBaseModel):
    def __init__(self, app, vao_name='loris', tex_id='loris', pos=(0,0,0), rot=(-90,0,0), scale=(0.03,0.03,0.03)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Armadillo(ExtendedBaseModel):
    def __init__(self, app, vao_name='armadillo', tex_id='armadillo', pos=(0,0,0), rot=(-90,0,0), scale=(0.03,0.03,0.03)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Pato(ExtendedBaseModel):
    def __init__(self, app, vao_name='pato', tex_id='pato', pos=(0,0,0), rot=(-90,0,0), scale=(0.03,0.03,0.03)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class CartelFinal(ExtendedBaseModel):
    def __init__(self, app, vao_name='CartelFinal', tex_id='CartelFinal', pos=(0,0,0), rot=(-90,0,0), scale=(0.03,0.03,0.03)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class SeaDragon(ExtendedBaseModel):
    def __init__(self, app, vao_name='seadragon', tex_id='seadragon', pos=(0,0,0), rot=(-90,0,0), scale=(0.1,0.1,0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

class Dolphin(ExtendedBaseModel):
    def __init__(self, app, vao_name='dolphin', tex_id='dolphin', pos=(0,0,0), rot=(-90,0,0), scale=(0.1,0.1,0.1)):
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
