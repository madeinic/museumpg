import pygame as pg
import moderngl as mgl
import glm


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/peligro.png')
        self.textures[1] = self.get_texture(path='textures/cesped.jpeg')
        # Textura de la skybox
        self.textures['skybox'] = self.get_texture_cube(dir_path='textures/skybox/', ext='png')
        self.textures['mono'] = self.get_texture(path='objects/monkey/12958_Spider_Monkey_diff.jpg')
        self.textures['gato'] = self.get_texture(path='objects/cat/cat_diffuse.jpg') 
        self.textures['perro'] = self.get_texture(path='objects/dog/Australian_Cattle_Dog_dif.jpg')  

    
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