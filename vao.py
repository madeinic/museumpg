from vbo import VBO
from shader_program import ShaderProgram

#diver falta importar y las halgas 
class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        #acceder a los vaos
        self.vaos = {}
        
        # Skybox vao
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo = self.vbo.vbos['skybox'])
        
        # advanced_skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.programs['advanced_skybox'],
            vbo=self.vbo.vbos['advanced_skybox'])

        # cubo vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])
        
        # shadow cubo vao
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cube'])
        
        # plataforma vao
        self.vaos['plataforma'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['plataforma'])
        
        # shadow plataforma vao
        self.vaos['shadow_plataforma'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['plataforma'])
        
        # trunk vao
        self.vaos['trunk'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['trunk'])
        
        # shadow trunk vao
        self.vaos['shadow_trunk'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['trunk'])

        # armadillo vao
        self.vaos['armadillo'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['armadillo'])
        
         #shadow armadillo vao
        self.vaos['shadow_armadillo'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['armadillo'])
        # columna vao
        self.vaos['columna'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['columna'])
        
         #shadow columna vao
        self.vaos['shadow_columna'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['columna'])
         # mono vao
        self.vaos['mono'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['mono'])
        
        #shadow mono vao
        self.vaos['shadow_mono'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['mono'])
        
        # gato vao
        self.vaos['gato'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['gato'])
        
        # shadow gato vao
        self.vaos['shadow_gato'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['gato'])
        
        # dino1 vao
        self.vaos['dino1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['dino1'])
        
        # shadow dino1 vao
        self.vaos['shadow_dino1'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['dino1'])
        # dino2 vao
        self.vaos['dino2'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['dino2'])
        
        # shadow dino2 vao
        self.vaos['shadow_dino2'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['dino2'])
        # grass vao
        self.vaos['grass'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['grass'])
        
        # shadow grass vao
        self.vaos['shadow_grass'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['grass'])

        # perro vao
        self.vaos['perro'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['perro'])
        
        # shadow perro vao
        self.vaos['shadow_perro'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['perro'])
        
        # tapir vao
        self.vaos['tapir'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['tapir'])

        # shadow tapir vao
        self.vaos['shadow_tapir'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['tapir'])
        
         # cartel vao
        self.vaos['CartelFinal'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['CartelFinal'])

        # shadow cartel vao
        self.vaos['shadow_CartelFinal'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['CartelFinal'])
        
        # rana vao
        self.vaos['rana'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['rana'])
        
        # shadow rana vao
        self.vaos['shadow_rana'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['rana'])

        # tucan vao
        self.vaos['tucan'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['tucan'])
        
        # shadow tucan vao
        self.vaos['shadow_tucan'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['tucan'])
        
       
        # anaconda vao
        self.vaos['anaconda'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['anaconda'])
        
        # shadow anaconda vao
        self.vaos['shadow_anaconda'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['anaconda'])
        
        # loris vao
        self.vaos['loris'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['loris'])
        
        # shadow loris vao
        self.vaos['shadow_loris'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['loris'])

        # pato mandarin vao
        self.vaos['pato'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['pato'])
        
        # shadow pato mandarin vao
        self.vaos['shadow_pato'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['pato'])
    

        # dragon de mar mandarin vao
        self.vaos['seadragon'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['seadragon'])
        
        # shadow pato mandarin vao
        self.vaos['shadow_seadragon'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['seadragon'])


        # dolphin vao
        self.vaos['dolphin'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['dolphin'])
        
        # shadow dolphinvao
        self.vaos['shadow_dolphin'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['seadragon'])
        
        # camel vao
        self.vaos['camel'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['camel'])
        
        # shadow camel vao
        self.vaos['shadow_camel'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['camel'])
        
        # penguin vao
        self.vaos['penguin'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['penguin'])
        
        # shadow penguin vao
        self.vaos['shadow_penguin'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['penguin'])

        # quetzal vao
        self.vaos['quetzal'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['quetzal'])
        
        #  shadow quetzal vao
        self.vaos['shadow_quetzal'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['quetzal'])
        
         # turkey vao
        self.vaos['turkey'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['turkey'])
        
        #  shadow turkey vao
        self.vaos['shadow_turkey'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['turkey'])

        # seahorse vao
        self.vaos['seahorse'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['seahorse'])
        
        #  shadow seahorse vao
        self.vaos['shadow_seahorse'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['seahorse'])

        # crab vao
        self.vaos['crab'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['crab'])
        
        #  shadow crab vao
        self.vaos['shadow_crab'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['crab'])
        
        # pink fish vao
        self.vaos['pinkfish'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['pinkfish'])
        
        #  shadow pink fish vao
        self.vaos['shadow_pinkfish'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['pinkfish'])

        # diver vao
        self.vaos['diver'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['diver'])
        
        #  shadow diver vao
        self.vaos['shadow_diver'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['diver'])

        # coral vao
        self.vaos['coral'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['coral'])
        
        #  shadow coral vao
        self.vaos['shadow_coral'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['coral'])

    #obtener vaos
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()