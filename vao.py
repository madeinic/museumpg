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

        # cubo vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])
        
        # mono vao
        self.vaos['mono'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['mono'])
        
        # gato vao
        self.vaos['gato'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['gato'])
        
        # perro vao
        self.vaos['perro'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['perro'])
        

        
    #obtener vaos
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()