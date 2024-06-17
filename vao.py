from vbo import VBO
from shader_program import ShaderProgram


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

    #obtener vaos
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()