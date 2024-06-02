import glm

#calcular los valores de la perspectica (angulo de vision, plano mas cercano y mas alejado)
FOV = 50#grados
NEAR = 0.1
FAR = 100

class Camera:
    def __init__(self, app):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(2, 3, 3)
        self.up = glm.vec3(0, 1, 0)
        #matriz de vista
        self.m_view = self.get_view_matrix()
        #matriz de proyección
        self.m_proj = self.get_projection_matrix()
        
        
    def get_view_matrix(self):
        return glm.lookAt(self.position, glm.vec3(0), self.up)
        
        
    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
        